import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar a base de dados
df = pd.read_excel("Copy of base_ev.xlsx", sheet_name="Plan1")

# ==========================
# a) GRÁFICO DE SETORES
# ==========================
top5_marcas = df['Make'].value_counts().head(5)

plt.figure(figsize=(8,8))
plt.pie(
    top5_marcas,
    labels=top5_marcas.index,
    autopct='%1.1f%%',
    colors=['skyblue', 'lightgreen', 'orange', 'pink', 'gold']
)
plt.title('Percentual das 5 Marcas de Veículos Elétricos Mais Frequentes')
plt.legend(title='Marcas')
plt.show()

# ==========================
# b) GRÁFICO DE BARRAS
# ==========================
plt.figure(figsize=(10,6))
plt.bar(
    top5_marcas.index,
    top5_marcas.values,
    color='steelblue',
    label='Quantidade de Veículos'
)

plt.title('Quantidade de Veículos por Marca (Top 5)')
plt.xlabel('Marca')
plt.ylabel('Quantidade')
plt.legend()
plt.show()

# ==========================
# c) HISTOGRAMA
# ==========================
plt.figure(figsize=(10,6))
plt.hist(
    df['Electric Range'].dropna(),
    bins=20,
    color='purple',
    edgecolor='black'
)

plt.title('Distribuição da Autonomia Elétrica')
plt.xlabel('Autonomia Elétrica (milhas)')
plt.ylabel('Frequência')
plt.show()

# ==========================
# d) BOXPLOT
# ==========================
plt.figure(figsize=(10,6))
sns.boxplot(
    x=df['Electric Range'],
    color='lightblue'
)

plt.title('Boxplot da Autonomia Elétrica')
plt.xlabel('Autonomia Elétrica (milhas)')
plt.ylabel('Valores')
plt.show()




# SEGUNDA PARTE

# Carregar a planilha
df = pd.read_excel("Copy of base_ev.xlsx", sheet_name="Plan1")

# ==========================
# ANÁLISE 1 - Electric Range
# ==========================

print("===== ELECTRIC RANGE ====")

# Medidas de Tendência Central
print("Média:", df['Electric Range'].mean())
print("Mediana:", df['Electric Range'].median())
print("Moda:", df['Electric Range'].mode()[0])

# Medidas de Dispersão
print("Amplitude:", df['Electric Range'].max() - df['Electric Range'].min())
print("Variância:", df['Electric Range'].var())
print("Desvio Padrão:", df['Electric Range'].std())

# Medidas Separatrizes
print("Q1:", df['Electric Range'].quantile(0.25))
print("Q2 (Mediana):", df['Electric Range'].quantile(0.50))
print("Q3:", df['Electric Range'].quantile(0.75))

# ==========================
# ANÁLISE 2 - Model Year
# ==========================

print("\n===== MODEL YEAR ====")

# Medidas de Tendência Central
print("Média:", df['Model Year'].mean())
print("Mediana:", df['Model Year'].median())
print("Moda:", df['Model Year'].mode()[0])

# Medidas de Dispersão
print("Amplitude:", df['Model Year'].max() - df['Model Year'].min())
print("Variância:", df['Model Year'].var())
print("Desvio Padrão:", df['Model Year'].std())

# Medidas Separatrizes
print("Q1:", df['Model Year'].quantile(0.25))
print("Q2 (Mediana):", df['Model Year'].quantile(0.50))
print("Q3:", df['Model Year'].quantile(0.75))