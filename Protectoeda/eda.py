import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv("train.csv")

# Mostrar primeras filas
print("Primeras filas del dataset:")
print(df.head())

# Verificar información general
print("\nInformación del dataset:")
print(df.info())

# Resumen estadístico
print("\nResumen estadístico:")
print(df.describe())

# Verificar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum().sort_values(ascending=False))

# Visualizar distribución del precio de venta
plt.figure(figsize=(8,5))
sns.histplot(df["SalePrice"], bins=30, kde=True, color="blue")
plt.title("Distribución de Precios de Venta")
plt.xlabel("Precio de Venta")
plt.ylabel("Frecuencia")
plt.show()

# Matriz de correlación (solo primeras 10 variables para claridad)
plt.figure(figsize=(10,8))
# Filtrar solo las columnas numéricas antes de calcular la correlación
numeric_df = df.select_dtypes(include=["number"])  

plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr().iloc[:10, :10], annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlación")
plt.show()

plt.title("Matriz de Correlación")
plt.show()

# Relación entre superficie y precio
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["GrLivArea"], y=df["SalePrice"], alpha=0.5)
plt.title("Relación entre Superficie y Precio")
plt.xlabel("Área habitable (pies²)")
plt.ylabel("Precio de Venta")
plt.show()
