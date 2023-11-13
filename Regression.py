import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r'c:\Users\dev\Downloads\NHANES.txt',sep='\\t')
a=['Education','Race','Sex','Sex']
b=['Poverty','Poverty','Weight','BMI']

#Daten konfigurieren und in numpyArray überführen

#for column in a:



#Daten konfigurieren und in numpyArray überführen


a=['Education','Race','Sex','Sex']
b=['Poverty','Poverty','Weight','BMI']
for k in range(len(a)):
 w = data[a[k]].unique().tolist()
 print(w)
 enddata=[]
 for i in w:
    fast_fertig = data[data[a[k]] == i]
    fertig= fast_fertig[b[k]].fillna(data[b[k]].median())
    enddata.append(fertig)
    print(len(enddata),'Lääänngeee')
 fig = plt.figure(figsize =(10, 7))
 ax = fig.add_subplot(111)
 bp = ax.boxplot(enddata, patch_artist=True,notch=True,vert=1,widths=0.9)
 farben=['green','blue','orange','yellow','violet'] 
 print(len(bp['boxes']),'Boxenlänge')
    
 for i in range(len(bp['boxes'])):
       print(i)
       bp['boxes'][i].set_facecolor(farben[i])
       

 for i in range(len(bp['whiskers'])):
     bp['whiskers'][i].set(color='red')

 for i in range(len(bp['caps'])):
      bp['caps'][i].set(color='red',linewidth = 2)

 for i in range(len(bp['medians'])):
      bp['medians'][i].set(color='red',linewidth=3)
 ax.set_ylim([0,data[b[k]].max()+1])
 plt.title('Relationship '+b[k] +' and ' + a[k])
 
 ax.set_xticklabels(w)
 plt.show()

#Spielerei

 








Hs=data[data['Education']=='HS incl GED']
less_HS = data[data['Education']=='Less than HS']
more_HS = data[data['Education']== 'More than HS']

end_HS = Hs['Poverty'].fillna(data['Poverty'].median())
end_less_HS = less_HS['Poverty'].fillna(data['Poverty'].median())
end_more_HS =more_HS['Poverty'].fillna(data['Poverty'].median())
print(end_HS)
enddata = [end_less_HS,end_HS, end_more_HS]

#Fenster erstellen und Achsen ausrichten
#fig, ax = plt.subplots(figsize=(6,3))#leeres Hauptfenster und Achse wird erstellt
#ax = fig.add_axes([0,0,1,1])#achse hinzugefügt die die figur abdeckt#plt.ylim(data['Waist'].min(),data['Waist'].max())

#Mal gemacht
#ax.get_xaxis().tick_bottom()
#ax.get_yaxis().tick_left()
#print(less_HS['Poverty'].median())
#print(Hs['Poverty'].median())
#print(more_HS['Poverty'].median())