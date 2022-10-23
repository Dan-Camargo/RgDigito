import time

print('Verificador de dígito do RG, feito por Daniel Alves. \n')

rg = list(input('Digite o número do RG sem o dígito e sem pontuações: '))

caracteres = len(rg)

#Pedir para inserir novamente se a quantidade de números estiver errada
while caracteres != 8:
    print('ERRO! Digite a quantidade certa de números (8) \n ')
    rg = list(input('Número do RG sem o dígito e sem pontuações: '))
    caracteres = len(rg)

#Transformar a lista de números em strings em uma lista de integers

rg = [int(rg) for rg in rg]

#Somar tudo na regra do RG Brasileiro

total = (rg[0]*2 + rg[1]*3 + rg[2]*4 + rg[3]*5 + rg[4]*6 + rg[5]*7 + rg[6]*8 + rg[7]*9)

#Transformando 10 e 11 em X e 0 respectivamente, pra depois mostrar o resultado
print('Aguarde... \n')
time.sleep(1)
digito = (11 - total%11)
if digito <= 9:
    print('O Dígito é:', 11 - total%11)
else:
    if digito == 10:
       digito = ("X")
       print('O Dígito é:', digito)
    else:
       if digito == 11:
          digito = ("0")
          print ('O Dígito é:', digito, '\n')
k=(input('Deseja checar mais algum RG? [S/N] '))
if k == ('s'):
    print('ok')
#DESCOBRIR COMO REINICIAR O CÓDIGO DESDE O COMEÇO PRA CALCULAR MAIS UM RG
else:
     print('Ok, até mais! :)')
     time.sleep(1.5)
     quit()


