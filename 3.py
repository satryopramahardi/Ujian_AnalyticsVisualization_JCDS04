import sqlalchemy as db
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

engine = db.create_engine('mysql://root:admin@localhost/world')
connection = engine.connect()

asean_df = pd.read_sql_query("select * from country inner join asean on country.name=asean.negara", connection)

sns.set_style("darkgrid")
bar = sns.barplot(x='Name', y='GNP', data=asean_df,palette="muted")
bar.set(xlabel='Negara', ylabel='Gross National Product (US$)')
bar.set_xticklabels(bar.get_xticklabels(),rotation=30)
bar.tick_params(labelsize=8)
plt.title('Pendapatan Bruto Nasional ASEAN')

for p in bar.patches:
    bar.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()),fontsize=8, color='gray', ha='center', va='bottom')

plt.show()