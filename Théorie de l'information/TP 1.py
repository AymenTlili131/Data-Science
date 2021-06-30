import numpy as np
from math import log2
import csv
from scipy.stats import entropy

def read_data(filename):
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        metadata  = next(datareader)
        traindata = []
        for row in datareader:
            traindata.append(row)

    return (metadata, traindata)

def event_sourceX(table_source):
    event_sourceX_items=np.unique(table_source)
    return event_sourceX_items

def probability_xk (table_source, xk):
    probability_xk_value=0
    for x in range(table_source.shape[0]):
        if table_source[x] == xk:
            probability_xk_value += 1
    probability_xk_value = probability_xk_value / table_source.shape[0]

    return probability_xk_value

def probability_sourceX (table_source):
    dist=[]
    items= event_sourceX(table_source)
    for x in range(items.shape[0]):
        probability_xk_value=probability_xk (table_source, items[x])
        dist.append(probability_xk_value)

    return [dist,items]

def probability_xk_sachant_ym (table_source_X, table_source_Y, xk, ym):
    
    table_source = np.array([])
    for i in table_source_Y:
        if yk=i:
            table_source=np.append(i)
    probability_xk_sachant_ym_value= probability_xk(table_source, xk)
    return probability_xk_sachant_ym_value

def probability_sourceX_sachant_ym (table_source_X, table_source_Y, ym):
    itemsX = event_sourceX(table_source_X)
    items=np.array([])
    dist = np.array([])
    for x in range (itemsX.shape[0]):
       items=np.append(items,itemsX[x]+' /'+ ym)
        dist=np.append(dist,probability_xk_sachant_ym (table_source_X, table_source_Y, x, ym))
    return  [dist, items]

def probability_xk_and_ym (table_source_X, table_source_Y, xk,ym):
    count =0
    for x in range (table_source_X.shape[0]):
        if table_source_X[x] == xk and table_source_Y[x] == ym:
            count+=1
    probability_xk_and_ym_value=count/table_source_X.shape[0]
    return probability_xk_and_ym_value

def probability_sourceX_and_sourceY (table_source_X, table_source_Y):

    itemsX = event_sourceX(table_source_X)
    itemsY = event_sourceX(table_source_Y)
    items=np.array([])
    dist = np.array([])
    for x in range (itemsX.shape[0]):
        for y in range (itemsY.shape[0]):
            items=np.append(items,itemsX[x]+' ,'+ itemsY[y])
            probability_xk_and_ym_value= probability_xk_and_ym (table_source_X, table_source_Y, itemsX[x],itemsY[y])
            dist=np.append(dist,probability_xk_and_ym_value)
    return  [dist, items]

def entropie_sourceX (table_source):
    [distX, itemsX] = probability_sourceX(table_source)
    entropie_sourceX_value = entropy(distX, None, 2)
    return entropie_sourceX_value

def entropie_sourceX_and_sourceY(table_source_X, table_source_Y):
    [dist, items]= probability_sourceX_and_sourceY(table_source_X,table_source_Y)
    entropie_sourceX_and_sourceY_value=entropy(dist,None,2)
return entropie_sourceX_and_sourceY_value


def entropie_sourceX_sachant_ym (table_source_X, table_source_Y, ym):
    itemsX = event_sourceX(table_source_X)
    entropie_sourceX_sachant_ym_value=0
    for xk in itemsX :
            entropie_sourceX_sachant_ym_value+=probability_sourceX_sachant_ym (table_source_X, table_source_Y, ym)*information_propre_xk_sachant_ym (table_source_X, table_source_Y, xk, ym)
    return entropie_sourceX_sachant_ym_value

def entropie_sourceX_sachant_sourceY (table_source_X, table_source_Y):
    itemsX = event_sourceX(table_source_X)
    itemsY = event_sourceX(table_source_Y)
    entropie_sourceX_sachant_Y_value=0
    for ym in itemsY:
        entropie_sourceX_sachant_Y_value+=entropie_sourceX_sachant_ym (table_source_X, table_source_Y, ym)*probability_sourceX_sachant_ym(table_source_X, table_source_Y, ym)
    return entropie_sourceX_sachant_Y_value

def information_propre_xk (table_source, xk):
   probability_xk_value=probability_xk(table_source, xk)
   if probability_xk_value==0 :
       print ('line 111')
       return -1
   information_propre_xk_value=log2(1/probability_xk_value)
   return information_propre_xk_value

def information_propre_xk_sachant_ym (table_source_X, table_source_Y, xk, ym):
    probability_xk_sachant_ym_value=probability_xk_sachant_ym(table_source_X, table_source_Y, xk, ym)
    if probability_xk_sachant_ym_value == 0:
        print('a Vérifier')
        return -1
    information_propre_xk_sachant_ym_value = log2(1 / probability_xk_sachant_ym_value)
    return information_propre_xk_sachant_ym_value

def information_mutuelle_xk_and_ym (table_source_X, table_source_Y, xk,ym):

    information_mutuelle_xk_and_ym_value= information_propre_xk (table_source_X, xk) - information_propre_xk_sachant_ym (table_source_X, table_source_Y, xk, ym)

    return information_mutuelle_xk_and_ym_value

def information_mutuelle_sourceX_and_sourceY (table_source_X,table_source_Y):
    information_mutuelle_sourceX_and_sourceY=0
    itemsX=event_sourceX(table_source_X)
    itemsY=event_sourceX(table_source_Y)
   for x in range (itemsX.shape[0]):
       for y in range (itemsY.shape[0]):
            probability_xk_and_ym_value=probability_xk_and_ym (table_source_X, table_source_Y, x,y)
            if probability_xk_and_ym_value !=0:
                information_mutuelle_sourceX_and_sourceY+=information_mutuelle_xk_and_ym (table_source_X, table_source_Y, x,y)
    return information_mutuelle_sourceX_and_sourceY

#lecture du fichier csv et formatage des données d'entrée
metadata, traindata = read_data("C:\\Users\\Aymen\\Downloads\\tennisdata.csv")    #à compléter (Question 2)
data = np.array(traindata)
P=probability_sourceX (data[:,1])
print('P(',metadata[:,1],'= Tiede) =', P )


#à compléter

[dist,items]=probability_sourceX (data[:,3])
for i in range (items.shape[0]):
    print('P(',metadata[3],'=', , ') =',dist[i])


#a compléter

[dist,items]=probability_sourceX_sachant_ym (data[:,4], data[:,0], "Ensoleille")
for i in range (items.shape[0]):
    print('P(',metadata[4],'|', items[0],'=','Ensoleille) =',dist[i])



#calcul de l'entropie de la source principale
#à compléter

entropy_value=entropie_sourceX(data[:,4])
print('H(',metadata[:,4],') est égale à', entropy_value)


#calcul de l'entropie conditionnelle élémentaire H(X/Y=ym)
#puis calcul de l'entropie conditionnelle moyenne
#à compléter

itemsX = event_sourceX(data[:,4])


for x in range (len(metadata)-1):

    itemsY = event_sourceX(data[:, x])
    for y in range(len(itemsY)):
       entropy_value_conditionnelle_elementaire =entropie_sourceX_sachant_ym (data[:,4], x, y)
       print('H(', metadata[len(metadata)-1], '/',metadata[x], '=', itemsY[y], ') est égale à', entropy_value_conditionnelle_elementaire)

    entropie_conditionnelle_moyenne+=entropy_value_conditionnelle_elementaire
    print('--> H(', metadata[len(metadata)-1], '/',metadata[x], ') =',entropie_conditionnelle_moyenne)


    print('--> I(', metadata[len(metadata)-1], ';',metadata[x], ') =',information_mutuelle_sourceX_and_sourceY(data[:,len(metadata)-1], data[:,x]))
    print('******')

