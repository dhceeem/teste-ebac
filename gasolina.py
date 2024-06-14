
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos desde el archivo CSV
df_gasolina = pd.read_csv("gasolina.csv")

# Crear el gráfico de líneas
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_gasolina, x="dia", y="venda", marker="o", color="blue", linewidth=2)

# Personalizar el gráfico
plt.title("Precio promedio de venta de gasolina en São Paulo - Julio 2021")
plt.xlabel("Día")
plt.ylabel("Precio de venta (R$)")

# Guardar el gráfico en un archivo PNG
plt.savefig("gasolina.png")

# Mostrar el gráfico
plt.show()
