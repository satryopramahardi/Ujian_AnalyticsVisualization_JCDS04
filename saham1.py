import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

xl_df = pd.read_csv('data/EXCL.JK.csv')
fr_df = pd.read_csv('data/FREN.JK.csv')
id_df = pd.read_csv('data/ISAT.JK.csv')
tk_df = pd.read_csv('data/TLKM.JK.csv')
# print(xl_df.head())

sns.set_style("darkgrid")
x = xl_df['Date']
# line = sns.lineplot(x="Date",y="Close", data=xl_df)
fig, ax = plt.subplots()
plt.plot(x, xl_df['Close'] , label='PT XL Axiata Tbk')
plt.plot(x, fr_df['Close'] , label='PT Smartfren Telecom Tbk')
plt.plot(x, id_df['Close'] , label='PT Indosat Tbk')
plt.plot(x, tk_df['Close'] , label='PT Telekomunikasi Indonesa Tbk')
plt.xticks(x, x, rotation='20', fontsize=7)

plt.title('Harga Historis Saham Provider Telco Indonesia')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
ax.xaxis.set_major_locator(MultipleLocator(7))
plt.legend(loc='lower center',frameon=False,ncol=4,bbox_to_anchor=(0.5, -0.02))
plt.show()