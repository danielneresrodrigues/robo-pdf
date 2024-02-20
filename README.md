# robo-pdf
Imagine a seguinte situação: você possui uma base de dados com várias informações, como nome, data de nascimento, e-mail, endereço, cidade, estado e CEP de diversas pessoas. Agora, você precisa criar um documento em PDF estilizado para cada indivíduo. Como você faria isso de forma rápida e eficiente?

O primeiro passo dessa tarefa é criar um tipo de arquivo “template”, no qual possamos editar apenas as informações necessárias para cada linha da nossa base. Para resolver essa etapa, optei por usar HTML com Bootstrap. Essa escolha se mostrou ideal, pois o HTML é um formato de arquivo de texto fácil de modificar e que permite personalização completa.

O segundo passo é adicionar marcadores a esse template, como {% dado_personalizado %}, que serão substituídos pelos dados reais posteriormente. A ideia é simplesmente utilizar a função replace do Python para alterar os dados personalizados. Por exemplo:

dados = {
    'nome': 'Daniel'
}

conteudo_do_html = '<p> {% nome %} </p>'

for dado in dados:
    conteudo_do_html = conteudo_do_html.replace(f'{{% {dado} %}}', dados[dado])

Nesse exemplo, a variável conteudo_do_html teria o valor ‘{% nome %}’ substituído pela string ‘Daniel’. Entendeu a ideia?

O terceiro passo é colocar isso em prática, lendo o template e gerando um novo HTML com o conteúdo substituído para cada linha da nossa base de dados.

Por fim, o quarto e último passo é utilizar uma biblioteca que converta o HTML para PDF. No meu caso, utilizei a biblioteca pyhtml2pdf, que se mostrou a melhor opção para conversões de HTML para PDF. Diferentemente de outras bibliotecas, ela literalmente renderiza o HTML para gerar um PDF, garantindo que o resultado final seja fiel ao HTML original.
