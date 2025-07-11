# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:34:43 2024

@author: marianna cecyn
"""

## Created by Marianna Cecyn 
## github: https://github.com/mariannacecyn 
## orcid: https://orcid.org/0000-0002-4995-7482
## linkedin: https://www.linkedin.com/in/mariannacecyn 


import pandas as pd
import numpy as np
import os

##I suggest you use the Spyder IDE within the anaconda environment
## You should use Anaconda environment to update the packages, this path is easier for beginners.


    
def MatrizTransicaoCont(array):
    #this function creates an counting matrix of transitions for each animal
    matrixcont = pd.crosstab(
        pd.Series(array[:-1], name='from'), #row
        pd.Series(array[1:], name='to'), #column
        margins=True)
    return matrixcont


def MatrizTransicaoProb(array):
    #this function creates an Matrix of Markov for each animal  
    matrixprob = pd.crosstab(
        pd.Series(array[:-1], name='from'), ##row
        pd.Series(array[1:], name='to'), ##column
        normalize="columns",
        margins=True)
    return matrixprob
    

def Frequencias(array):
    #this fuction counts the frequencies of Boris ethogram behaviors
    ##### KEY POINT OF ATTENCION:
    #It is very important to check that the dictionary 
    #has exactly the same behavior as your ethogram 
    #and that the spelling is exactly the same with upper and lower case letters, 
    #spacing, special characters, etc. 
    i=0
    #######LDB 
    Frequencies = {'Light side entrance':0, 'Dark side entrance':0, 'Rearing': 0, 'Stretching NO-GO': 0, 'Head out NO-GO': 0, 'Grooming': 0, 'Sniffing': 0, 'Walking': 0, 'Stretching GO': 0, 'Head out GO': 0}
 
    #if you change this dictionary, 
    #you should update the Prob dictionary for Probabilidades()
    #and run combinations code to update the transitions for Transicoes()
    while i < array.size:  
      Key = array[i] 
     
      if Key in Frequencies:
          Frequencies[Key] = Frequencies[Key] + 1 
      else:
          Frequencies[Key] = 1 
      i = i+1

    dfFreq = pd.DataFrame.from_dict(Frequencies, orient ='index') 
    dfFreqt = dfFreq.T
    return dfFreqt

def Probabilidades(array):
    #this function created the State Vector for Markov Chain 
    Probabilities = {'Light side entrance':0, 'Dark side entrance':0, 'Rearing': 0, 'Stretching NO-GO': 0, 'Head out NO-GO': 0, 'Grooming': 0, 'Sniffing': 0, 'Walking': 0, 'Stretching GO': 0, 'Head out GO': 0} 
    i = 0
    while i < array.size:  
      Key = array[i] 
     
      if Key in Probabilities:
          Probabilities[Key] = Probabilities[Key] + 1 
      else:
          Probabilities[Key] = 1 
      i = i+1

    for key in Probabilities:
        Probabilities[key] /= contBehavior
    dfProb = pd.DataFrame.from_dict(Probabilities, orient ='index')
    dfProbt = dfProb.T
    return dfProbt

    
           
def Transicoes(array):

    AllTransitions = {'Dark side entrance - Dark side entrance':0, 
                      'Dark side entrance - Grooming':0, 
                      'Dark side entrance - Head out NO-GO':0,
                      'Dark side entrance - Light side entrance':0, 
                      'Dark side entrance - Rearing':0, 
                      'Dark side entrance - Sniffing':0, 
                      'Dark side entrance - Stretching NO-GO':0, 
                      'Dark side entrance - Walking':0, 
                      'Dark side entrance - Head out GO':0, 
                      'Dark side entrance - Stretching GO':0, 
                      'Grooming - Dark side entrance':0, 
                      'Grooming - Grooming':0, 
                      'Grooming - Head out NO-GO':0, 
                      'Grooming - Light side entry':0, 
                      'Grooming - Rearing':0, 
                      'Grooming - Sniffing':0, 
                      'Grooming - Stretching NO-GO':0, 
                      'Grooming - Walking':0, 
                      'Grooming - Head out GO':0, 
                      'Grooming - Stretching GO':0, 
                      'Head out NO-GO - Dark side entrance':0, 
                      'Head out NO-GO - Grooming':0, 
                      'Head out NO-GO - Head out NO-GO':0, 
                      'Head out NO-GO - Light side entrance':0, 
                      'Head out NO-GO - Rearing':0, 
                      'Head out NO-GO - Sniffing':0, 
                      'Head out NO-GO - Stretching NO-GO':0, 
                      'Head out NO-GO - Walking':0, 
                      'Head out NO-GO - Head out GO':0, 
                      'Head out NO-GO - Stretching GO':0, 
                      'Light side entrance - Dark side entrance':0, 
                      'Light side entrance - Grooming':0,
                      'Light side entrance - Head out NO-GO':0, 
                      'Light side entrance - Light side entrance':0, 
                      'Light side entrance - Rearing':0, 
                      'Light side entrance - Sniffing':0, 
                      'Light side entrance - Stretching NO-GO':0, 
                      'Light side entrance - Walking':0,
                      'Light side entrance - Head out GO':0, 
                      'Light side entrance - Stretching GO':0, 
                      'Rearing - Dark side entrance':0, 
                      'Rearing - Grooming':0, 
                      'Rearing - Head out NO-GO':0, 
                      'Rearing - Light side entrance':0, 
                      'Rearing - Rearing':0, 
                      'Rearing - Sniffing':0, 
                      'Rearing - Stretching NO-GO':0, 
                      'Rearing - Walking':0, 
                      'Rearing - Head out GO':0, 
                      'Rearing - Stretching GO':0, 
                      'Sniffing - Dark side entrance':0, 
                      'Sniffing - Grooming':0, 
                      'Sniffing - Head out NO-GO':0, 
                      'Sniffing - Light side entrance':0, 
                      'Sniffing - Rearing':0, 
                      'Sniffing - Sniffing':0, 
                      'Sniffing - Stretching NO-GO':0, 
                      'Sniffing - Walking':0, 
                      'Sniffing - Head out GO':0, 
                      'Sniffing - Stretching GO':0, 
                      'Stretching NO-GO - Dark side entrance':0, 
                      'Stretching NO-GO - Grooming':0, 
                      'Stretching NO-GO - Head out NO-GO':0, 
                      'Stretching NO-GO - Light side entrance':0, 
                      'Stretching NO-GO - Rearing':0, 
                      'Stretching NO-GO - Sniffing':0, 
                      'Stretching NO-GO - Stretching NO-GO':0, 
                      'Stretching NO-GO - Walking':0, 
                      'Stretching NO-GO - Head out GO':0, 
                      'Stretching NO-GO - Stretching GO':0, 
                      'Walking - Dark side entrance':0, 
                      'Walking - Grooming':0, 
                      'Walking - Head out NO-GO':0, 
                      'Walking - Light side entrance':0, 
                      'Walking - Rearing':0, 
                      'Walking - Sniffing':0, 
                      'Walking - Stretching NO-GO':0, 
                      'Walking - Walking':0, 
                      'Walking - Head out GO':0, 
                      'Walking - Stretching GO':0, 
                      'Head out GO - Dark side entrance':0, 
                      'Head out GO - Grooming':0, 
                      'Head out GO - Head out NO-GO':0, 
                      'Head out GO - Light side entrance':0, 
                      'Head out GO - Rearing':0, 
                      'Head out GO - Sniffing':0, 
                      'Head out GO - Stretching NO-GO':0, 
                      'Head out GO - Walking':0, 
                      'Head out GO - Head out GO':0, 
                      'Head out GO - Stretching GO':0,
                      'Stretching GO - Dark side entrance':0, 
                      'Stretching GO - Grooming':0, 
                      'Stretching GO - Head out NO-GO':0,
                      'Stretching GO - Light side entrance':0, 
                      'Stretching GO - Rearing':0, 
                      'Stretching GO - Sniffing':0, 
                      'Stretching GO - Stretching NO-GO':0, 
                      'Stretching GO - Walking':0, 
                      'Stretching GO - Head out GO':0,
                      'Stretching GO - Stretching GO':0}
                       #thanks copilot for these combinations, to make you combinations, use the code in comment below.
    
    
    
    
    
    AnimalTransitions = {} #Thank Fernando Cecyn for that strategy for each animal behavior combinations 
    i=0
    while i < contBehavior:
            
        Key = str(array[i-1]) + " - " + str(array[i]) 
        if Key in AnimalTransitions:
              AnimalTransitions[Key] = AnimalTransitions[Key] + 1 
        else:
              AnimalTransitions[Key] = 1 
        i = i+1
        
    
    Transitions = {**AllTransitions, **AnimalTransitions} #to combine both dictionaries 

    dfTrans = pd.DataFrame.from_dict(Transitions, orient ='index')
    dfTranst = dfTrans.T
    return dfTranst
##############################
##if you need to create your combinations and combination dictionary, use the following code:
    
##List of behaviors
#comportamentos = ['Light side entry', 'Close side entry', 'Rearing', 'Stretching', 'Head out', 'Grooming', 'Sniffing', 'Walking', 'stretch risk', 'head risk']


#combinacoes = []

##Generate all possible combinations of twos where order matters and the same element can occur with itself
#for comportamento1 in comportamentos:
#    for comportamento2 in comportamentos:
#        combinacoes.append(f"{comportamento1} - {comportamento2}")

##Sort the combinations alphabetically
#combinacoes_ordenadas = sorted(combinacoes)

## Turn the list of combinations into a Python dictionary
#AllTransitions = {i: combinacao for i, combinacao in enumerate(combinacoes_ordenadas)}
#print(AllTransiotions)
##I suggest running this code separately and then pasting your AllTransitions dictionary into the main code.
################################
    


#INICIANDO...

print("\n================================")
print("App for Behavior Data Processing 3.0 \n Created by Marianna Cecyn \n Please cite  \n github: https://github.com/mariannacecyn  \n orcid: https://orcid.org/0000-0002-4995-7482 \n linkedin: https://www.linkedin.com/in/mariannacecyn")
print("\n================================")   
#if you want to use console, use this code
##folder = input("Paste here the full path of the data folder you would like to process: ") ##if you prefer use the Spyder console 
##path = folder

#if you want to directly use the code, use this:
folder = r"C:\Users\maria\Desktop\Myrna\BORIS\LDB\Planilhas LDB\novo\TUDO"
#remember that you should change "\" by "/" to use this.

path = folder
files = os.listdir(path)
files_xlsx = [path + '/' + f for f in files if f[-5:] == '.xlsx' ]
animals = [a[-12:-5] for a in files if a[-5:] == '.xlsx'] 
#here you must change a string depending your file name lenght
print("\n================================")
#datasubj = pd.DataFrame(animals)
#databaseBehaviors = pd.DataFrame()
#databaseTrans = pd.DataFrame()

for f in files_xlsx:
          

    
    df_original = pd.read_excel(f) #transformei o excel num objeto do python que ele consegue mostrar como Dataframe
    
    arr = df_original["Behavior"].values #criado um array com a sequencia de comportamentos
    #print(arr)        
    
    for i in arr:


        if i == "Start of test":
            arr = np.delete(arr, np.where(arr == i))
        if i == "End of test":
            arr = np.delete(arr, np.where(arr == i))
    
        else: arr = arr
    contBehavior = np.size(arr)
    

 
        
    

    
    ##Usando o ExcelWriter, cria um doc .xlsx, usando engine='xlsxwriter'
    ## you need to create a folder and copy the path here
    writer = pd.ExcelWriter(r"C:\Users\maria\Desktop\Myrna\BORIS\LDB\Planilhas LDB\novo\python" + '/python' + f[-12:], engine='xlsxwriter')
    #remember that you should change "\" by "/" to use this. You should review the lenght of names.
    
    
    df_original.to_excel(writer, sheet_name='Boris')
    pd.DataFrame(arr).to_excel(writer, sheet_name='SeqBehaviors')
    Frequencias(arr).to_excel(writer, sheet_name='FreqBehaviors')
    Probabilidades(arr).to_excel(writer, sheet_name='ProbBehaviors')
    Transicoes(arr).to_excel(writer, sheet_name='TransCont')
    MatrizTransicaoCont(arr).to_excel(writer, sheet_name='ContMatrix')
    MatrizTransicaoProb(arr).to_excel(writer, sheet_name='ProbMatrix')
    

    writer.close()
    

   


