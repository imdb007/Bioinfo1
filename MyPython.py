import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data = pd.read_csv(r'c:\Users\Wieland Menke\Downloads\NHANES.txt',sep='\\t')

#Variante des Codes von ...
x = ['BMI','Waist','BMI','Glucose_mol','BMI','Age','F_Income','Poverty']
l=[]
for i,w in zip(x[0::2],x[1::2]):# zip wird verwendet um mit zwei elementen die liste zu durchlaufen
#for j in range(0,len(x),2):
   # i = x[j]
   # w=x[j+1] gerne so gelöst, aber Error
    print(i)
    #w=x[(x.index(i)+1)]#code in chat gtp, irgendein fehler drin
    print(w)
    print(data.shape)#gibt Zeilen und Spalten an 
    print(data.columns)# gibt Spaltennamen an 
    data[i].fillna(data[i].mean(), inplace=True)#füllt alle fehlenden werte mit durchschnitt
    data[(w)].fillna(data[(w)].mean(), inplace=True) #inplace= True verändert ursprüngliche Datenstruktur, gibt also keine Kopie zurück 
    x = pd.DataFrame(data[i]) #wandelt Spalte i in Dataframe, für Methode fit
    y = pd.DataFrame(data[w])
    model = LinearRegression()# ((objekt der Klasse LinearRegression erstellt))
    model.fit(x,y)#modell mit daten von x und y gefüttert, soll linearen Zusammenhang suchen 
    #Methoden nachschauen, musst verstehen
    intercept =model.intercept_[0] # abhängigie Variable Y wird extrahiert, ist der Wert der erwartet wird, wenn x null ist, also wenn die y-Achse geschnitten wird

    print('HIERHIERHIER')
    print(intercept)
    slope = model.coef_[0,0] #steigung der regressionsgeraden aus model wird in slope gespeichert
    r_sq=model.score(x,y)
    l.append('das Bestimmtheitsmaß von '+i+' und '+w+' ist: '+str(round(r_sq,5)))
    print('bestimmtheitsmaß:', round(r_sq,5))
    
    plt.scatter(data[i], data[w])# streudiagramm wird erstellt
    plt.title(i +'/'+(w)) #beschriftung model
    plt.xlabel(i)
    plt.ylabel(w)
    t = np.array([min(x.loc[:, i]), max(x.loc[:, i])]) #array wird erstellt, dass die werte für unabhängiges i abdeckt, min und max von i
    t = t.reshape(-1,1)#array wird in Spalte umgewandelt
    plt.plot(t,model.predict(t),'-r')#Regressionsgerade wird in rot gezeichnet im bereich t des modells 
    plt.show()#diagramm wird gezeigt
for i in range(len(l)):
    print(l[i])
print('es wurde auf 5 Nachkommastellen gerundet')
#data['Age'].hist(bins = 8)
#plt.show()
#data['Sodium'].hist(bins=8)
#plt.show()
#data['Height'].hist(bins = 6)
#plt.show()
#data['F_Income'].hist(bins=20)
#plt.show()  
#plt.scatter(data['BMI'],data['Waist'])
#plt.show()
