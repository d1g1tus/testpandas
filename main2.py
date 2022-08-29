import pandas as pd
import numpy as np

data = pd.read_csv('Data2.csv')

# ====================================================================================
# EJERCICIO 1: Devuelve la cantidad total de valores repetidos sin contar el primero
# ====================================================================================
# todo -> sumar todos los valores duplicados de la lista entre iterando dentro de ella

'''dup_rows = data.duplicated(keep='first').sum()
print(dup_rows)'''

# ====================================================================================
# EJERCICIO 2: Elimina las entradas duplicadas y devuelve sólo la primera
# ====================================================================================
# todo -> sumar todos los valores duplicados de la lista entre iterando dentro de ella
# todo -> después concatena y devuelve sólo los valores cuyo índice represente la primera
# todo -> vez que aparecieron

'''df_cleaned = data.drop_duplicates(keep='first')
print(df_cleaned)'''

# ====================================================================================
# EJERCICIO 3: Resuelve las inconsistencias en la sección de "estados"
# ====================================================================================
# todo -> iteramos dentro de los valores de un diccionario, y por cada valor sustituimos A por B
# todo -> en toda la lista objetivo. Para ello se puede iterar o en el diccionario o en la lista

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

'''for i in range(len(data['cust_state'])):
    if data['cust_state'][i] in states:
        data['cust_state'][i] = states[data['cust_state'][i]]

print(data['cust_state'])

for key in states:
    data['cust_state'] = data['cust_state'].replace(regex=[key], value=states[key])

print(data['cust_state'])'''

# ====================================================================================
# EJERCICIO 4: Valida los datos de la columna X
# ====================================================================================
# todo -> No sé a qué se refiere con validar datos

# ====================================================================================
# EJERCICIO 5: Resuelve las inconsistencias en la sección de "estados"
# ====================================================================================