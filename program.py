#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:04:22 2024

@author: danielneresrodrigues
"""

# Importa os módulos necessários
import os
import pandas as pd
from datetime import datetime
from pyhtml2pdf import converter

# Define o caminho da pasta do projeto
path = '/home/danielneresrodrigues/Documentos/RoboPDF/'

# Lê o arquivo csv com os dados
df = pd.read_csv(os.path.join(path, 'dados.csv'), sep=';', encoding='utf-8')

# Define uma função para converter a data de nascimento para o formato dd/mm/yyyy
def converteData(data):
    data = datetime.strptime(data, '%Y-%m-%d')
    return data.strftime('%d/%m/%Y')

# Aplica a função na coluna data_de_nascimento do dataframe
df['data_de_nascimento'] = df['data_de_nascimento'].apply(converteData)

# Abre o arquivo html com o modelo do documento
arquivo_html = open(os.path.join(path, 'index.html'), mode='r', encoding='utf-8')
conteudo_html = arquivo_html.read()
arquivo_html.close()

# Itera sobre as linhas do dataframe
for i in range(df.shape[0]):
    
    # Copia o conteúdo html para uma variável auxiliar
    conteudo_html_aux = conteudo_html
    
    # Cria um dicionário com os dados da linha atual
    dados = {
        'identificador': df.loc[i, 'identificador'],
        'nome': df.loc[i, 'nome'],
        'nascimento': df.loc[i, 'data_de_nascimento'],
        'rua': df.loc[i, 'rua'],
        'cidade': df.loc[i, 'cidade'],
        'estado': df.loc[i, 'estado'],
        'cep': df.loc[i, 'cep'],
    }
    
    # Define os nomes dos arquivos html e pdf com o identificador do dado
    identificador = dados['identificador']
    html_file = f'{identificador}.html'
    pdf_file = f'{identificador}.pdf'
    
    # Substitui os dados personalizados no conteúdo html
    for dado in dados:
        conteudo_html_aux = conteudo_html_aux.replace(f'{{% {dado} %}}', f'{dados[dado]}')

    # Cria um arquivo html com o conteúdo personalizado
    arquivo = open(os.path.join(path, 'formularios', html_file), mode='w', encoding='utf-8')
    arquivo.write(conteudo_html_aux)
    arquivo.close()

    # Define o caminho do arquivo html
    path_html = os.path.join(path, 'formularios', html_file)

    # Converte o arquivo html em pdf
    converter.convert(f'file:///{path_html}', os.path.join(path, 'formularios/formularios_gerados', pdf_file))
    
    # Remove o arquivo html
    os.remove(path_html)