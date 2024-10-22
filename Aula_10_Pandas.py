###AULA09 - 17/10/2024###
#FUNÇÕES (continuação)

#ATIVIDADE ASSISTIDA: (criação de um módulo personalizado)

# Criem quatro funções para cada uma das operações aritméticas fundamentais (soma, subtração, multiplicação e divisão). Cada função
# deve receber dois números como parâmetros e retornar o resultado apropriado.

# Em seguida, todas as funções devem ser integradas em um único programa: criem uma nova função para gerar números aleatórios e aplicá-los 
# às operações anteriores.

#Resolução:
 
#Funções Matemáticas:

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b != 0:
        return a/b
    else:
        return "Divisões por zero não são permitidas."

print(somar(40,20))
print(subtrair(40,20))
print(multiplicar(40,20))
print(int(dividir(40,20))) #toda divisão em python, por padrão, nos fornece um resultado float.

import random

def gerando_numeros(quantidade,valor_minimo,valor_maximo): #for na forma 'condensada' ou 'compacta'
    return [random.randint(valor_minimo,valor_maximo) for i in range(quantidade)]

# def doisnum_aleatorios(qtd,numero_minimo,numero_maximo): #for na forma 'tradicional'
#     for i in range(qtd):
#         return random.randint(numero_minimo,numero_maximo)

numeros=gerando_numeros(2,1,100)
n1,n2= numeros[0],numeros[1]

print(numeros)
print(f"Números gerados:{n1} e {n2}.")
print(f"Soma:{somar(n1,n2)}")
print(f"Subtração:{subtrair(n1,n2)}")
print(f"Multiplicação:{multiplicar(n1,n2)}")
print(f"Divisão:{dividir(n1,n2)}")

#####################
(arquivo calculadora.py)
import random

def gerando_numeros(quantidade,valor_minimo,valor_maximo):
    return [random.randint(valor_minimo,valor_maximo) for i in range(quantidade)]

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b != 0:
        return a/b
    else:
        return "Divisões por zero não são permitidas."
#####################

(testando o módulo num arquivo externo qualquer.py)
import calculadora
from calculadora import somar
print(somar(2,5))

##################################################################################################

#TRATAMENTO DE EXCEÇÕES (TRY e EXCEPT)

#Reformulando a função de divisão:
def dividir(a,b):
    try:
        resultado=a/b
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero!")
    else:
        print(f"O resultado da divisão é {resultado}.")
    finally:
        print("Operação finalizada.")

#Testando a função reformulada:
dividir(20,2)
dividir(20,0)
dividir(2,5)

#ATIVIDADE: (github)

#Leia três pares de números inteiros fornecidos pelo usuário, calcule e imprima a soma de cada par separadamente. Utilize 
#tratamento de erros para garantir que os valores inseridos sejam válidos e, se o número for ÍMPAR, ter uma exceção personalizada.

#####
#####

#TRATAMENTO DE EXCEÇÕES (TRY e EXCEPT)

#Reformulando a função de divisão:
def dividir(a,b):
    try:
        resultado=a/b
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero!")
    else:
        print(f"O resultado da divisão é {resultado}.")
    finally:
        print("Operação finalizada.")

#Testando a função reformulada:
dividir(20,2)
dividir(20,0)
dividir(2,5)

#ATIVIDADE: (github)

#Leia três pares de números inteiros fornecidos pelo usuário, calcule e imprima a soma de cada par separadamente. Utilize 
#tratamento de erros para garantir que os valores inseridos sejam válidos e, se o número for ÍMPAR, ter uma exceção personalizada.
#####

###AULA10 - 18/10/2024###
#
# Pandas (pandas.pydata.org)
#
import pandas as pd #(pd=alias)
print(pd.__version__)

#CRIAÇÃO DE UM DATASET:

data = {'Cargo': ['Analista', 'Gerente', 'Estagiário'],
        'Salário': [4500, 9000, 2000]}
cargos_salarios = pd.DataFrame(data)
print(cargos_salarios)

#CRIAÇÃO DE UMA SÉRIE:

cargos = pd.Series(['Analista', 'Gerente', 'Estagiário'], index=[1, 2, 3])
print(cargos)

#ATIVIDADE ASSISTIDA:

#Crie um dataset de 3 colunas com as seguintes informações: 'nome de um filme', 'ano de lançamento' e 'gênero'.

#Resolução:
import pandas as pd

data_cinema={'Título':['Cidade de Deus','Divertidamente 2','Uma Linda Mulher'],
        'Ano de Lançamento':[2002, 2024, 1990],
        'Gênero':['Drama', 'Animação','Romance']
}
cinema=pd.DataFrame(data_cinema)
print(cinema)

#ACESSO À DATASETS EXTERNOS:

https://www.kaggle.com/datasets/thebumpkin/700-classic-disco-tracks-with-spotify-data


import pandas as pd #(pd=alias)
print(pd.__version__)

df_custo_de_cursos = pd.read_csv('custo de cursos no exterior.csv')
print(df_custo_de_cursos.head())  # Exibe as primeiras linhas
print(df_custo_de_cursos.tail())  # Exibe as cinco últimas linhas

#Leitura de Arquivos e Filtragem:

print(df_custo_de_cursos.to_string()) #Exibe o DataFrame completo como uma string, útil para visualização.


pd.set_option('display.max_rows',3)  #Define o número máximo de linhas a ser exibido.

#Filtragem de Dados: #Exemplo de filtragem por colunas e linhas específicas:

df_filtrado = df_custo_de_cursos[df_custo_de_cursos['custo de cursos no exterior.csv'] == 'custo de cursos no exterior.csv']
print(df_filtrado)

#Criação de Novas Colunas: adicionar colunas derivadas

import pandas as pd #(pd=alias)
print(pd.__version__)
df_custo_de_cursos['custo_mensal'] = df_custo_de_cursos['FEES']
print(df_custo_de_cursos.head())

#Leitura de Arquivos Excel e Outros Formatos:
df_disco_2 = pd.read_excel('seuarquivo.xlsx')
df_disco_3 = pd.read_json('seuarquivo.json')
df_disco_4 = pd.read_html('seuarquivo.html')
df_disco_5 = pd.read_sql('seuarquivo.sql')

#Atividade Prática:
#
#Através do Kaggle, procurem outros datasets e apliquem os comandos trabalhados anteriormente.




