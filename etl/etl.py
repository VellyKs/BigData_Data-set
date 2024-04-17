# -*- coding: utf-8 -*-
"""data-setBigData.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1js_ikxoCrVr8DoxRhlNExZ9s5Lthyzw_

Para começar, vamos criar o banco de dados "vacinados", utilizando os dados da API do data-set escolhido.
"""

import requests
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def create_vacinados_db():
    # URL da API
    url = f"http://dados.recife.pe.gov.br/api/3/action/datastore_search?&resource_id=ca7fb968-3a2c-44ff-a2e8-730d1a689407&limit=300000"

    # Fazer a requisição à API
    response = requests.get(url)
    data = response.json()

    if 'result' in data and 'records' in data['result']:
        vacinados = data['result']['records']
    else:
        print("Erro: Não foi possível obter os dados da API.")
        return


    # Criar ou conectar ao banco de dados SQLite
    conn = sqlite3.connect('vacinados.db')
    c = conn.cursor()

    # Criar a tabela, se não existir
    c.execute('''
    CREATE TABLE IF NOT EXISTS vacinados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faixa_etaria TEXT,
    idade NUMERIC,
    sexo TEXT,
    raca_cor TEXT,
    municipio TEXT,
    grupo TEXT,
    categoria TEXT,
    lote TEXT,
    vacina_fabricante TEXT,
    descricao_dose NUMERIC,
    cnes TEXT,
    sistema_origem TEXT,
    data_vacinacao TIMESTAMP
    );
    ''')



    # Inserir dados no banco de dados
    for vacina in vacinados:
        c.execute('''
        INSERT INTO vacinados (faixa_etaria, idade, sexo, raca_cor, municipio, grupo, categoria, lote, vacina_fabricante, descricao_dose, cnes, sistema_origem, data_vacinacao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', (
            vacina.get('faixa_etaria', ''),
            vacina.get('idade', 0),
            vacina.get('sexo', ''),
            vacina.get('raca_cor', ''),
            vacina.get('municipio', ''),
            vacina.get('grupo', ''),
            vacina.get('categoria', ''),
            vacina.get('lote', ''),
            vacina.get('vacina_fabricante', ''),
            vacina.get('descricao_dose', 0),
            vacina.get('cnes', ''),
            vacina.get('sistema_origem', ''),
            vacina.get('data_vacinacao', '')
        ))

    # Commitar as mudanças e fechar a conexão
    conn.commit()
    conn.close()

# Exemplo de uso chamando a função para criar com todos os registros da API
create_vacinados_db()

"""Agora vamos criar uma nova conexão com o banco de dados para fazermos consultas:"""

connection = sqlite3.connect('vacinados.db')

# Criando uma variavel que recebe todo o valor da leitura
vc = pd.read_sql_query("select * from vacinados", connection)

"""Vamos começar nossa análise exploratória:"""

vc.info()
# um comando que vai dar as informações gerais da nossa base de dados, valores nulos e tipos de dados.

"""Agora outro comando que nos fornece um resumo estatistico do nosso banco:

Contagem (count): número de observações não nulas.

Média (mean): média aritmética dos valores.

Desvio padrão (std): medida de dispersão em torno da média.

Valor mínimo (min): menor valor na variável.

Quartis (25%, 50%, 75%): valores que dividem a distribuição em quartis, representando o primeiro quartil (Q1), mediana (Q2) e terceiro quartil (Q3).

Valor máximo (max): maior valor na variável.
"""

vc.describe()

"""Agora vamos utilizar o comando display para mostrar os 5 primeiros e os 5 últimos dados e também a quantidade de informações que temos:"""

display(vc)

"""Agora para visualizar o periodo da analise:"""

inicio = pd.to_datetime(vc['data_vacinacao']).dt.date.min()
print("Data de inicio", inicio)
fim = pd.to_datetime(vc['data_vacinacao']).dt.date.max()
print("Data final", fim)

vc_municipio = vc.municipio.value_counts().head(10)
vc_municipio.plot(kind='bar')
plt.xlabel('Nome do Município')
plt.ylabel('Número de Vacinados')
plt.show()
