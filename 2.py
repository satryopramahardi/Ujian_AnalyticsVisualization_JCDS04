import sqlalchemy as db
import pandas as pd
import matplotlib.pyplot as plt

engine = db.create_engine('mysql://root:admin@localhost/world')
connection = engine.connect()

asean_df = pd.read_sql_query("select * from country inner join asean on country.name=asean.negara", connection)

labels = asean_df['Name']
sizes = asean_df['Population']

pie = plt.subplot()
pie.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0)
pie.set_title('Presentase Penduduk ASEAN')
pie.axis('equal')

plt.show()
