import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/victo/Downloads/analise_dados_avancada/dados.xlsx')
print(df)

ini = pd.to_datetime(df['DATA_VENDA']).dt.date.min()
fim = pd.to_datetime(df['DATA_VENDA']).dt.date.max()
print(f'o período dos Dados é {ini} até {fim}')

df.info()
df.describe()

# Calculando as Medidas De Posição(Média, Mediana e Moda)

media = df['VALOR'].mean()
print(f' a Média é {media:.4f}')

mediana = df['VALOR'].median()
print(f' a Mediana é {mediana}')

moda = df['VALOR'].mode()
print(f' a Moda é {moda[0]}')

#  Calculando as Medidas De Dispersão(Variância e Desvio Padrão)

variancia = df['VALOR'].var()
print(f' a Variância é {variancia}')

desvio = df['VALOR'].std()
print(f' o Desvio Padrão é {desvio:.4f}')

#  Calculando a Assimetria e Curtose

assimetria = df['VALOR'].skew()
print(f' a Assimetria é {assimetria:.4f}')

curtose = df['VALOR'].kurtosis()
print(f' a Curtose é {curtose:.4f}')

# Total de valores únicos de cada variável

valores_unicos = []
for i in df.columns[0:14].tolist():
    print(i, ':', len(df[i].astype(str).value_counts()))
    valores_unicos.append(len(df[i].astype(str).value_counts()))

# Observar a quantidade de registros por tipo de transmissao

df.groupby(['TRANSMISSAO']).size()

# Identificando os modelos mais vendidos

x = df['MODELO'].value_counts().values
y = df['MODELO'].value_counts().index
sns.barplot( x=x, y=y)
plt.show()

# Observamos quais são os Modelos com mais Cavalos

dt=df.sort_values(['CAVALOS'], axis=0,ascending=False)
print(dt[['MODELO','CAVALOS']])

# Criando um Histograma (exibe a forma e distribuição de dados amostrais discretos ou contínuos.)

sns.histplot(df['VALOR'])
plt.show()

# Criando um Gráfico de Dispersão (usado para observar como as variaveis se relacionam)

sns.scatterplot(data=df, x='CAVALOS', y='VALOR')
plt.show()

# Convertendo o campo DATA_VENDA para DateTime

df['DATA_VENDA'] = pd.to_datetime(df['DATA_VENDA'], format='%d/%m/%Y')

# Selecionando apenas as Vendas de 2020

df_2020 = df[df['DATA_VENDA'].dt.year == 2020]
print(df_2020)

# Selecionando apenas as Vendas de 2021

df_2021 = df[df['DATA_VENDA'].dt.year == 2021]
print(df_2021)

# Comparativo de Lucro Bruto por Mês

df_2020.groupby(df_2020['DATA_VENDA'].dt.month)['VALOR'].sum().plot(color='green', label='Ano 2020')
df_2021.groupby(df_2021['DATA_VENDA'].dt.month)['VALOR'].sum().plot(color='orange', label='Ano 2021')
plt.title('Vendas x Mês')
plt.ylabel('Valor')
plt.xlabel('Mês')
plt.legend()
plt.show()
