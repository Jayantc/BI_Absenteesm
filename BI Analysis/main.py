from absenteeism_module import *
print(pd.read_csv('Absenteeism_new_data.csv'))

model= absenteeism_model('model', 'scaler')
model.load_and_clean_data('Absenteeism_new_data.csv')
print(model.predicted_outputs())

import mysql.connector
conn= mysql.connector.connect(database= 'predicted_outputs', user= 'root', password='***', auth_plugin='mysql_native_password')
cursor= conn.cursor()

df_new_obs= model.predicted_outputs()

insert_query= 'INSERT INTO predicted_outputs VALUES'
for i in range(df_new_obs.shape[0]):
    insert_query += '('
    for j in range(df_new_obs.shape[1]):
        insert_query += str(df_new_obs[df_new_obs.columns.values[j]][i]) + ', '
    insert_query = insert_query[:-2] + '), '
insert_query = insert_query[:-2] + ';'
print(insert_query)
print(cursor.execute(insert_query))
conn.commit()
conn.close()