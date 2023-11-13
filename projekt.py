import pandas as pd
import matplotlib as plt
data = pd.read_csv(r'c:\Users\dev\Downloads\NHANES.txt',sep='\\t')
print(data.columns)
print(data.dtypes) # alles Typen werden angezeigt
print(data.select_dtypes(include = ['int', 'float'])) # alle float/ints in Theorie quantitativ werden angezeigt
print(data.select_dtypes(include = ['object']))# alle Objekte--> qualitativ werden angezeigt
#Liste der quantitativen Merkmale:
#Age,F_income,((Poverty??)) n Weight, Height, BMI, Waist, Pulse, Calcium_mol, Cholest_mol, Glucose_mol, Sodium, Potassium, ((H_income?)), AgefistSex??
# Liste der qualitativen Merkmale
#Sex, Race, education, Mariatal, Sexorient
#Liste der Mekrmale bei denen unsicher: Poverty, H_income, Agefirstsex
#for i in data['Age','F_income','Weight','Height','BMI','Waist','Pulse','Calcium_mol','Cholest_mol','Glucose_mol','Sodium','Potassium']:
   # print(i.median(),'\n',i.max(),'\n',i.min() )
quantitative_columns = data.select_dtypes(include = ['int','float'])
for column in quantitative_columns:
  print('Spalte:', column)
  print('Durchschnitt beträgt: {} '.format(round(data[column].mean(),1)))
  print('Median beträgt:       {}'.format(data[column].median()))
  print('Maximum beträgt:      {}'.format(data[column].max()))
  print('Minimum beträgt:      {}\n'.format(data[column].min()))
qualitative_columns = data.select_dtypes(include = ['object'])
for column in qualitative_columns:
  print('Die Klassen von '+column+' in ihrer Häufigkeit:')
  klassen_anzahl = data[column].value_counts()
  for klasse,anzahl in klassen_anzahl.items():
    print(klasse+':', anzahl)





    