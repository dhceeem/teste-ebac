
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos desde el archivo CSV
df_gasolina = pd.read_csv("gasolina.csv")

# Crear el gráfico de líneas con algunas modificaciones
plt.figure(figsize=(12, 7))
sns.lineplot(data=df_gasolina, x="dia", y="venda", marker="o", color="green", linewidth=2, linestyle='--')

# Personalizar el gráfico
plt.title("Precio Promedio de Venta de Gasolina - São Paulo, Julio 2021", fontsize=14)
plt.xlabel("Día del Mes", fontsize=12)
plt.ylabel("Precio de Venta (R$)", fontsize=12)
plt.grid(True)

# Guardar el gráfico en un archivo PNG
plt.savefig("gasolina.png")

# Mostrar el gráfico
plt.show()
