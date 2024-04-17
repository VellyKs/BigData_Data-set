# BigData_Data-set

Membros:
* Alyson Henrique
* Débora Ramos
* Evellyn Karla
* Júlia Menezes
* Radássila Rebeka
* Vanessa Carolina

## 1. Pesquisa e Detalhamento do Dataset:

### Seleção do Dataset:

Dataset escolhido: 2023 - Perfil das Pessoas Vacinadas - Covid-19
Área: Saúde

Escolhemos o Dataset acima devido não só a exploração da quantidade de pessoas vacinadas, como também a noção quantitativa das não vacinadas, tendo o controle e monitoramento necessário para estes casos. Contudo, se torna válido a subtração da quantidade de pessoas dentro dos parâmetros de vacinação do Recife em relação as pessoas que foram vacinadas, como resultado obteríamos a quantidade de pessoas que não se vacinaram na época. Além disso, esses dados são extremamente relevantes para acompanhar a eficácia da vacina, dado o acompanhamento da propagação da doença pelos profissionais da saúde. Nosso Dataset responderia perguntas como: qual foi a faixa etária com o maior e menor número de vacinação? Quais cnes mais vacinaram? Além de inserir no banco de dados novos casos de vacinação e servir como parâmetro de comparação com outros municípios.

## 2. Apresentação do Dicionário de Dados:

### Definição:

nome | tipo | observação
---------|--------|---------
id|Numérico | apresenta autoincrement para cada caso cadastrado
faixa_etaria|Categórico | apresenta intervalos padrões entre idades
idade|Numérico | apresenta exatidão da idade cadastrada
sexo|Categórico | limitado a quantidade de gênero
raca_cor|Categórico | limitado a quantidade de raça
municipio|Texto | apresenta unicidade, pois há apenas "Recife" entre os municípios
grupo|Categórico | limitado a categorias gerais ou específicas (público geral, pessoas com comorbidade)
categoria|Categórico | voltado  a diferenciação de pessoas que se insiram em um grupo com especificidade (demais casos não específicos|nulos)
lote|Texto | codificação do lote da vacina ofertada
vacina_fabricante|Categórico | especificação da vacina ofertada (código padrão/ nome padrão)
descricao_dose|Categórico | numeração da dose da vacina aplicada (1º, 2º, 3º ou 4º dose)
cnes|Numérico | localidade de aplicação da vacina
sistema_origem|Categórico | sistema de origem da vacina
data_vacinacao|Data | separada por ano/mês/dia

