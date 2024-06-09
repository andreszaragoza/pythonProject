import pandas as pd
import matplotlib.pyplot as plt

# Crear un conjunto de datos ficticio
data = {
    'Nombre': ['Alasne', 'Carlos', 'Valentina', 'Daniela', 'Belen', 'Fernando', 'Luis'],
    'Edad': [28, 34, 29, 45, 31, 41, 38],
    'Departamento': ['Ventas', 'IT', 'IT', 'Ventas', 'RRHH', 'Ventas', 'IT'],
    'Salario': [50000, 62000, 52000, 58000, 47000, 60000, 54000]
}

df = pd.DataFrame(data)

# Añadir el símbolo de la moneda euro (€) a los salarios
df['Salario (€)'] = df['Salario'].apply(lambda x: f"{x} €")


# Mostrar las primeras filas del DataFrame
print(df.head())

# Explorar los datos
print(df.info())
print(df.describe())

# Operaciones básicas
salario_promedio = df.groupby('Departamento')['Salario'].mean()
print(salario_promedio)

empleados_por_departamento = df['Departamento'].value_counts()
print(empleados_por_departamento)

# Visualización de datos
plt.figure(figsize=(8,5))
salario_promedio.plot(kind='bar')
plt.title('Salario promedio por departamento')
plt.xlabel('Departamento')
plt.ylabel('Salario promedio')
plt.show()

plt.figure(figsize=(8,5))
empleados_por_departamento.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribución de empleados por departamento')
plt.ylabel('')
plt.show()
