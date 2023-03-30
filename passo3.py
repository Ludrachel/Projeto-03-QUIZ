print('''
Q1 - No Python, como se chama uma 'caixa' usada para
armazenar dados?

a - texto
b - variavel
c - uma caixa de sapatos
''')

resposta = input("Sua resposta : ").lower()
if resposta == "a":
    print(" NÃO , texto é um tipo de dado :( ")
elif resposta == "b":
    print("CORRETO !!  :) ")
elif resposta == "c":
    print(" NÃO SEJA BOBINHO ! :( ")
else:
    print(" VOÇÊ NÃO ESCOLHEU a , b ou c :( ")
