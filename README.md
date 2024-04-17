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

Área: saúde

Escolhemos o Dataset acima devido não só a exploração da quantidade de pessoas vacinadas, como também das não vacinadas, tendo o controle e monitoramento necessário para estes casos. Além disso, se torna válido a subtração da quantidade de pessoas dentro dos parâmetros de vacinação do Recife em relação as pessoas que foram vacinadas, como resultado obteríamos a quantidade de pessoas que não se vacinaram na época. Além disso, esses dados são extremamente relevantes para acompanhar a eficácia da vacina, dado o acompanhamento da propagação da doença pelos profissionais da saúde. Nosso Dataset responderia perguntas como: qual foi o a faixa etária com o maior e menor número de vacinação? Quais cnes mais vacinaram? Além de inserir no banco de dados novos casos de vacinação e servir como parâmetro de comparação com outros municípios.

## 2. Análise Exploratória:

Quantidade de registros: 300.000 registros

Variáveis disponíveis: id, faixa_etaria, idade, sexo, raca_cor, municipio, grupo, categoria, lote, vacina_fabricante, descricao_dose, cnes, sistema_origem, data_vacinacao

Possíveis lacunas nos dados: valores nulos

## 3. Apresentação do Dicionário de Dados:

### Definição:

nome | tipo
---------|--------
id | Numérico
faixa_etaria| Categórico
idade| Numérico
sexo| Categórico
raca_cor| Categórico
municipio| Texto
grupo| Categórico
categoria| Categórico
lote| Texto
vacina_fabricante| Categórico
descricao_dose| Categórico
cnes| Numérico
sistema_origem| Categórico
data_vacinacao| Data

