import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Título
st.title("🏡 Dashboard de Análisis de Precios de Casas")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")
    df = df[["OverallQual", "GrLivArea", "GarageCars", "TotalBsmtSF", "SalePrice"]].dropna()
    return df

df = load_data()

# Mostrar datos
st.subheader("📊 Exploración de Datos")
st.write(df.head())

# Visualización de correlaciones
st.subheader("📈 Matriz de Correlación")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# Entrenar modelo de predicción
st.subheader("🔍 Predicción de Precios")
X = df.drop(columns=["SalePrice"])
y = df["SalePrice"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)
mae = mean_absolute_error(y_test, predicciones)

st.write(f"📌 **Error Medio Absoluto:** {mae:.2f} USD")

# Interfaz para predicciones personalizadas
st.subheader("🎯 Predice el Precio de una Casa")
overall_qual = st.slider("Calidad General", 1, 10, 5)
gr_liv_area = st.number_input("Área Habitable (pies²)", 500, 5000, 1500)
garage_cars = st.slider("Capacidad del Garaje", 0, 4, 2)
total_bsmt_sf = st.number_input("Área del Sótano (pies²)", 0, 3000, 500)

input_data = pd.DataFrame([[overall_qual, gr_liv_area, garage_cars, total_bsmt_sf]], 
                          columns=X.columns)
predicted_price = modelo.predict(input_data)[0]
st.write(f"💰 **Precio Estimado:** ${predicted_price:,.2f} USD")
