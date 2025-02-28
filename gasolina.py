import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.get_dataset_names()
sns.set_theme(style="darkgrid")
gasolina = pd.read_csv('gasolina.csv')

grafico=sns.lineplot(data=gasolina,x='dia', y='venda', palette='pastel')

plt.savefig('gasolina.png')
