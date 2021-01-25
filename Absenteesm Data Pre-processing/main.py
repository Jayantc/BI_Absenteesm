import pandas as pd
pd.options.display.max_rows= None
pd.options.display.max_columns= None
raw_csv_data= pd.read_csv("Absenteeism_data.csv")
df= raw_csv_data.copy()
print(df)
print(df.info())


df= df.drop(['ID'], axis=1)
print(df)


print(df['Reason for Absence'])
print(df['Reason for Absence'].max())
print(df['Reason for Absence'].min())
print(df['Reason for Absence'].unique())
print(len(df['Reason for Absence'].unique()))
reason_columns= pd.get_dummies(df['Reason for Absence'], drop_first=True)
print(reason_columns)


df=df.drop(['Reason for Absence'], axis=1)
print(df)
reason_type_1= reason_columns.loc[:, 1:14].max(axis=1)
reason_type_2= reason_columns.loc[:, 15:17].max(axis=1)
reason_type_3= reason_columns.loc[:, 18:21].max(axis=1)
reason_type_4= reason_columns.loc[:, 22:28].max(axis=1)


df= pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis=1)
column_names= ['Date', 'Transportation Expense', 'Distance to Work', 'Age', 'Daily Work Load Average', 'Body Mass Index','Education', 'Children', 'Pets', 'Absenteeism Time in Hours', 'reason_type_1', 'reason_type_2', 'reason_type_3', 'reason_type_4']
df.columns= column_names
print(df)

column_names_reordered= ['reason_type_1', 'reason_type_2', 'reason_type_3', 'reason_type_4', 'Date', 'Transportation Expense', 'Distance to Work', 'Age', 'Daily Work Load Average', 'Body Mass Index','Education', 'Children', 'Pets', 'Absenteeism Time in Hours']
df= df[column_names_reordered]
print(df)


df_reason_mod= df.copy()
df_reason_mod['Date']= pd.to_datetime(df_reason_mod['Date'], format='%d/%m/%Y')
print(df_reason_mod['Date'])

list_of_months=[]
week_day=[]
for i in range(700):
    list_of_months.append(df_reason_mod['Date'][i].month)
    week_day.append(df_reason_mod['Date'][i].weekday())
print(list_of_months)
df_reason_mod= df_reason_mod.drop(['Date'], axis=1)
df_reason_mod['Month value']= list_of_months
df_reason_mod['Week day']= week_day
column_names_reordered= ['reason_type_1', 'reason_type_2', 'reason_type_3', 'reason_type_4', 'Month value', 'Week day', 'Transportation Expense', 'Distance to Work', 'Age', 'Daily Work Load Average', 'Body Mass Index','Education', 'Children', 'Pets', 'Absenteeism Time in Hours']
df_reason_mod= df_reason_mod[column_names_reordered]
print(df_reason_mod)


print(df_reason_mod['Education'].unique())
print(df_reason_mod['Education'].value_counts())
df_reason_mod['Education']= df_reason_mod['Education'].map({1:0, 2:1, 3:1, 4:1})
print(df_reason_mod['Education'].unique())
print(df_reason_mod['Education'].value_counts())

final_preprocessed_df= df_reason_mod.copy()
print(final_preprocessed_df)
