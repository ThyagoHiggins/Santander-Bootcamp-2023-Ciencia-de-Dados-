#confesso que tive dificuldades. As aulas não 
#trouxeram ferramentas para um CRUD.


import csv

analise = list()

saldo = open('Projeto IA/cliente.csv')
tabela = csv.reader(saldo)

for saldos in saldo:
    if saldos[3] == 'sem saldo':
        saldos.append('Você precisa de recursos')
        analise.append(saldo)
    elif saldo[3] =='saldo positivo':    
        saldos.append('sem obs')
        analise.append(saldo)
    elif saldo[3] == 'saldo negativo':
        saldos.append('Você está usando o cheque especial')
        analise.append(saldo)
    elif saldo[3] == 'saldo para investimento':
        saldos.append('vamos investir?')
        analise.append(saldo)

nova_tabela = open('cliente.csv','w',newline ='')
dica= csv.writer(nova_tabela, delimiter=',')
dica.writerows(analise)

nova_tabela.close()
saldo.close()
