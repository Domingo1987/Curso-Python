import pandas as pd
import matplotlib.pyplot as plt


data = {'frutas': ['manzana', 'plátano', 'uva'], 'cantidad': [10, 5, 12]}
df = pd.DataFrame(data)
#print(df)

df.set_index('frutas').plot(kind='bar', title='Cantidad de Frutas', legend=False)
plt.ylabel('Cantidad')
plt.xlabel('Frutas')
plt.tight_layout()
plt.show()