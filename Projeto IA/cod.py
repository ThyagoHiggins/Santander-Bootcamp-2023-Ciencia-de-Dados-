import pandas as pd 
import requests
import json 

df = pd.read_csv(
    'Projeto IA/cliente.csv',
     encoding= 'utf-8',
     #sep=';' usado quando separação for ;
     #index_col= 'nome'quando quer transformar index

)

for saldo in df: 
    if saldo[2] < '0':
        print("Saldo negativo")
        saldo.append('Sem Grana')
        df[3].append(0)


#for negativo in df:
    #saldo = negativo.filter({'saldo'})
    #print(saldo)
    
    #if negativo['saldo']< 0:
        #negativo['Obs'] = 'ATENÇÃO USANDO CHEQUE ESPECIAL'
        
#print(df.head())