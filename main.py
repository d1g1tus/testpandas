import pandas as pd
import numpy as np

data = pd.read_csv('Data.csv')

# ====================================================================================
# EJERCICIO 1: Devuelve la cantidad total de transacciones
# ====================================================================================
# todo -> sumar todos los valores de la lista entre si iterando dentro de ella

'''num_trans = data["trans_quantity"]
suma = 0
for i in range(len(num_trans)):
    suma += num_trans[i]

print(suma)'''

'''num_trans = data["trans_quantity"].sum()
print(num_trans)'''

# ====================================================================================
# EJERCICIO 2: Cuál es el mes y el día de la primera compra. Guardalo como tupla
# ====================================================================================
# todo -> almacenar como tupla el primer valor de dos listas respectivamente

'''first_date = (data["trans_month"][0], data["trans_day"][0])
print(first_date)
first_date = (int(data["trans_month"].head(1)), int(data["trans_day"].head(1)))
print(first_date)'''

# ====================================================================================
# EJERCICIO 3: Cuál es el mes y el día de la última compra. Guardalo como tupla
# ====================================================================================
# todo -> almacenar como tupla el último valor de dos listas respectivamente

'''last_date = (data["trans_month"][len(data["trans_month"])-1], data["trans_day"][len(data["trans_day"])-1])
print(last_date)
last_date = (int(data["trans_month"].tail(1)), int(data["trans_day"].tail(1)))
print(last_date)'''

# ====================================================================================
# EJERCICIO 4: ¿Cuál es el tipo de producto más popular?
# ====================================================================================
# todo -> iterar dentro de una lista y contar el valor más repetido dentro de esta

'''most_pop = data['prod_animal_type'].value_counts().idxmax()
print(most_pop)'''

# ====================================================================================
# EJERCICIO 5: Sumar solo dinero ganado en enero
# ====================================================================================
# todo -> iterar dentro de una lista y sumar todos los valores de esta con la condición de que el índice de B
# todo -> coincida con el índice de A si este tiene un valor concreto asignado

'''jan_rev = 0

for i in range(len(data["trans_month"])):
    if data["trans_month"][i] == 1:
        jan_rev += data["total_sales"][i]

print(jan_rev)'''

# ====================================================================================
# EJERCICIO 6: Sumar solo dinero ganado en junio
# ====================================================================================
# todo -> iterar dentro de una lista y sumar todos los valores de esta con la condición de que el índice de B
# todo -> coincida con el índice de A si este tiene un valor concreto asignado

'''june_rev = 0

for i in range(len(data["trans_month"])):
    if data["trans_month"][i] == 6:
        june_rev += data["total_sales"][i]

print(june_rev)'''

# ====================================================================================
# EJERCICIO 7: Devolver promedio de productos comprados
# ====================================================================================
# todo -> iterar dentro de una lista y devolver el valor promedio de sus valores

'''avg_num_items = data["trans_quantity"].mean()
print(avg_num_items)'''

# ====================================================================================
# EJERCICIO 8: Top 10 Productos más vendidos por títulos de mayor a menor
# ====================================================================================
# todo -> iterar dentro de dos listas cuyos indices sean el mismo y sumar datos equivalentes entre si
# todo -> asegurándose de que el índice coincida, para despúes devolver los datos organizados de mayor
# todo -> a menor repetición

'''
top_num_sales = (data.groupby(['prod_title'])['trans_quantity']).sum().sort_values(ascending=False).head(10)
print(top_num_sales)'''


# ====================================================================================
# EJERCICIO 9: Top 10 Productos más vendidos por dinero ganado de mayor a menor
# ====================================================================================
# todo -> iterar dentro de dos listas cuyos indices sean el mismo y sumar datos equivalentes entre si
# todo -> asegurándose de que el índice coincida, para despúes devolver los datos organizados de mayor
# todo -> a menor repetición

'''top_tot_sales = (data.groupby(['prod_title'])['total_sales']).sum().sort_values(ascending=False).head(10)
print(top_tot_sales)'''

# ====================================================================================
# EJERCICIO 10: Calcular la proporción de clientes que vuelven
# ====================================================================================
# todo -> Sacar el valor promedio de los ids repetidos en comparativa con los no repetidos

'''prop_returning = data['cust_id'].duplicated(keep=False).sum().mean()
print(prop_returning)'''