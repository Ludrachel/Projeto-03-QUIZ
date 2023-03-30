# DESAFIO - QUIZ - MÚLTIPLA ESCOLHA
score = 0
print('''
QUESTÃO 1 - O QUE É PYTHON ?

A - um objeto
B - um computador
C - uma linguagem de programação
''')

resposta = input("Sua resposta : ").upper()
if resposta == "C":
    print(" SIM !! , PYTHON É UMA LIGUAGEM DE PROGRAMAÇÃO ! :) ")
    score = score + 1
else:
    print("OPS, TENTE NOVAMENTE :( ! ")
print(" ")
resposta = input("Sua resposta : ").upper()
if resposta == "C":
    print(" SIM !! , PYTHON É UMA LIGUAGEM DE PROGRAMAÇÃO ! :) ")
    
else:
    print(" oh que pena :( ")

print('''
QUESTÃO 2 - QUANTO É 10 + 90 ?

A - 100
B - 110
C - 120
''')

resposta = input("Sua resposta : ").upper()
if resposta == "A":
    print(" CORRETO :) ")
    score = score + 1
else:
    print("OPS , TENTE NOVAMENTE :( ")
resposta = input("Sua resposta : ").upper()
if resposta == "A":
    print(" CORRETO :) ")
    
else:
    print(" OH QUE PENA :( ")

print(f' FIM DO QUIZ... \n PONTUAÇÃO TOTAL:{score}/2') 
