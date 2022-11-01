def digitouNumero(x1=0,x2=0,x3=0): # testa se o número é válido
    if x1 or x2 or x3 in(12345678):
        return True
    else:
        return False


def fase1(): # lógica da fase 1
    print('SEJA BEM-VINDO A FASE 1')
    print('Na Fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos:')
    posicoes1=['*','*','-','G'] 
    posicoes2=['R','-','*','*']
    print(posicoes1) # printa na tela a matrix
    print(posicoes2)

    x1=int(input('Em qual posição quer alocar o RATO? ')) # pergunta ao usuário as posições
    x2=int(input('Em qual posição quer alocar o GATO? '))

    if digitouNumero(x1,x2)== False: # testa se digitou números válidos
        resultado=0
        print('Deve digitar apenas números entre 1 e 8')

   
    if x1 == 6 and x2==3: # testa as posições possíveis 

        print('Passou de fase!') # retorna valor para próxima fase
        resultado=2
    else:
        print('Você perdeu!') # retorna informando que perdeu
        resultado=0
    
    return resultado

def fase2(): # lógica da fase 2
    print()
    print()
    print('SEJA BEM-VINDO A FASE 2')
    print('Na Fase 2, o jogador deve alocar CÃO, CÃO E OSSO na seguinte matriz que representa os quartos:')
    posicoes1=['-','*','*','*']
    posicoes2=['*','C','-','-']
    print(posicoes1) # printa na tela a matrix das posições
    print(posicoes2)

    x1=int(input('Em qual posição quer alocar o CÃO? ')) # pergunta ai usuário as posições
    x2=int(input('Em qual posição quer alocar o CÃO? '))
    x3=int(input('Em qual posição quer alocar o OSSO? '))

    if digitouNumero(x1,x2,x3)== False:
        resultado=0
        print('Deve digitar apenas números entre 1 e 8')

   
    if x3==1: # testa as posições possíveis 

        print('Passou de fase!') # retorna valor para proxima fase 
        resultado=3
    else:
        print('Você perdeu!') # informa ao usuário que perdeu
        resultado=0
    
    return resultado

def fase3(): # lógica da fase 3
    print()
    print()
    print('SEJA BEM-VINDO A FASE 3')
    print('Na Fase 3, o jogador deve alocar GATO, RATO E OSSO na seguinte matriz que representa os quartos:')
    posicoes1=['-','*','*','*']
    posicoes2=['-','G','-','-']
    print(posicoes1) # printa na tela as posições 
    print(posicoes2)

    x1=int(input('Em qual posição quer alocar o GATO? ')) # pergunta ao usuário as posições desejadas 
    x2=int(input('Em qual posição quer alocar o RATO? '))
    x3=int(input('Em qual posição quer alocar o OSSO? '))

    if digitouNumero(x1,x2,x3)== False:
        resultado=0
        print('Deve digitar apenas números entre 1 e 8')


    # testa se as posições informadas respeitam as regras
    if (x3==1 and x2==8 and x1==5) or ( x1==1 and x2==8 and x3==5) or (x1==8 and x2==1 and x3==5) or (x3==5 and x1==7 and x2==1) or (x3==7 and x2==8) or (x3==8 and x2==1 and not x1==5):
        print('Passou de fase!') # informa ao usuário que passou de fase e retorna valor para próxima fase
        resultado=4
    else:
        print('Você perdeu!') # informa ao usuário de perdeu e retorna valor 
        resultado=0
    
    return resultado

def fase4(): # lógica da fase 4
    print()
    print()
    print('SEJA BEM-VINDO A FASE 4')
    print('Na Fase 4, o jogador deve alocar QUEIJO, QUEIJO, OSSO na seguinte matriz que representa os quartos:')
    posicoes1=['-','-','-','*']
    posicoes2=['*','R','*','*']
    print(posicoes1) # printa na tela as posições da fase 4
    print(posicoes2)

    x1=int(input('Em qual posição quer alocar o QUEIJO? ')) # pergunta ao usuário as posições desejadas 
    x2=int(input('Em qual posição quer alocar o QUEIJO? '))
    x3=int(input('Em qual posição quer alocar o OSSO? '))

    if digitouNumero(x1,x2,x3)== False:
        resultado=0
        print('Deve digitar apenas números entre 1 e 8')

   
    if x3==2: # testa se a posição respeita a regra 
        print('Você ganhou!') # informa que ganhou e retorna valor 
        resultado=5
    else:
        print('Você perdeu!') # informa que perdeu e retorna valor 
        resultado=0
    
    return resultado

#Programa Principal
print('HOTEL DOS ANIMAIS!') # printa na tela o início 
print('ESPECIFICANDO POSIÇÕES:')
print('[1, 2, 3, 4 ] \n[5, 6, 7, 8 ]') # printa as posições para digitação
print()
print()


resultado=0

while True: # bloco while para passagem de fase ou não 
    if resultado==0:
        resultado=fase1()
        if resultado==2:
            continue
    if resultado==2:
        resultado=fase2()
        if resultado==3:
            continue
    if resultado==3:
        resultado=fase3()
        if resultado==4:
            continue
    if resultado==4:
        resultado = fase4()
        if resultado==5:
            print('VOCÊ VENCEU! PARABENS')
            break






    

