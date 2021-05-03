from random import shuffle,choice
from time import sleep
nome = str(input("Digite seu nome: ")).strip()
if nome.lower() == 'artur':
    print("caramba, o mesmo que o meu!") 
    sleep(2)
print("Seja bem vindo {}!".format(nome)) 
while True:
    qual = int(input("Como você quer sortear?\n Por ordem (1)\n Versus(2)\n Uma pessoa dentre várias(3)\n")) 
    quantos = int(input('Quantas pessoas você quer sortear? (2,3,4,5,6,7,8) obs: o Versus só funciona com números pares\n')) 
    if quantos == 2:
        pessoa1 = str(input("Digite o nome da primeira pessoa:\n")).strip().lower().title() 
        pessoa2 = str(input("Digite o nome da segunda pessoa:\n")).strip().lower().title()
        sorteados = [pessoa1,pessoa2] 
        shuffle(sorteados)
        if qual == 1:
            print("A primeira pessoa foi {}\nA segunda pessoa foi {}".format(sorteados[0],sorteados[1]))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair?(2)\n"))
            if final == 2:
                sleep(2)
                break                  
        elif qual == 2:
            print("O versus é meio óbvio com 2 pessoas") 
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(2)
                break
        elif qual == 3:
            print("O escolhido foi o {}".format(choice(sorteados))) 
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(2)
                break    

    elif quantos == 3:
        pessoa1 = str(input("Digite o nome da primeira pessoa:\n")).strip().lower().title()
        pessoa2 = str(input("Digite o nome da segunda pessoa:\n")).strip().lower().title() 
        pessoa3 = str(input("Digite o nome da terceira pessoa:\n")).strip().lower().title() 
        sorteados = [pessoa1,pessoa2,pessoa3] 
        shuffle(sorteados) 
        if qual == 1:
            print("A primeira pessoa foi {}\nA segunda pessoa foi {}\nA terceira pessoa foi {}".format(sorteados[0],sorteados[1],sorteados[2]))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(2)
                break
        elif qual == 2:
            print("O programa não é capaz de fazer versus com número impar, creio que não só o programa rsrsrs, então se esperar 5 segundos o programa se alto resetará e você poderá consertar")
            sleep(5) 
        elif qual == 3:
            print("A pessoa escolhida foi {}".format(choice(sorteados)))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(2)
                break

    elif quantos == 4:
        pessoa1 = str(input("Digite o nome da primeira pessoa:\n")).strip().lower().title()
        pessoa2 = str(input("Digite o nome da segunda pessoa:\n")).strip().lower().title()
        pessoa3 = str(input("Digite o nome da terceira pessoa:\n")).strip().lower().title() 
        pessoa4 = str(input("Digite o nome da quarta pessoa:\n")).strip().lower().title() 
        sorteados = [pessoa1,pessoa2,pessoa3,pessoa4] 
        shuffle(sorteados)
        if qual == 1:
            print("A primeira pessoa foi {}\nA segunda pessoa foi {}\nA terceira pessoa foi{}\nA quarta pessoa foi {}".format(sorteados[0],sorteados[1],sorteados[2],sorteados[3]))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(2)
                break
        if qual == 2:
            print("{} versus {}\n {} versus {}".format(sorteados[0],sorteados[1],sorteados[2],sorteados[3]))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(2)
                break
        if qual == 3:
            print("A pessoa escolhida foi {}".format(choice(sorteados)))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(2)
                break    

    elif quantos == 5:
        pessoa1 = str(input("Digite o nome da primeira pessoa:\n")).strip().lower().title() 
        pessoa2 = str(input("Digite o nome da segunda pessoa:\n")).strip().lower().title() 
        pessoa3 = str(input("Digite o nome da terceira pessoa:\n")).strip().lower().title() 
        pessoa4 = str(input("Digite o nome da quarta pessoa:\n")).strip().lower().title()
        pessoa5 = str(input("Digite o nome da quinta pessoa:\n")).strip().lower().title()
        sorteados = [pessoa1,pessoa2,pessoa3,pessoa4,pessoa5] 
        shuffle(sorteados)
        if qual == 1:
            print("A primeira pessoa foi {}\nA segunda pessoa foi {}\nA terceira pessoa foi {}\nA quarta pessoa foi {}\nA quinta pessoa foi {}".format(sorteados[0],sorteados[1],sorteados[2],sorteados[3],sorteados[4]))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(2)
                break
        elif qual == 2:
            print("O programa não é capaz de fazer versus com número ímpar, creio que não só o programa rsrsrs, então se esperar 5 segundos o programa se alto resetará e você poderá consertar")
            sleep(5)
        elif qual == 3:
            print("A pessoa escolhida foi {}".format(choice(sorteados)))
            sleep(2)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(3)
                break
    elif quantos == 6:
        pessoa1 = str(input("Digite o nome da primeira pessoa:\n")).strip().lower().title() 
        pessoa2 = str(input("Digite o nome da segunda pessoa:\n")).strip().lower().title() 
        pessoa3 = str(input("Digite o nome da terceira pessoa:\n")).strip().lower().title() 
        pessoa4 = str(input("Digite o nome da quarta pessoa:\n")).strip().lower().title()
        pessoa5 = str(input("Digite o nome da quinta pessoa:\n")).strip().lower().title()
        pessoa6 = str(input("Digite o nome da sexta pessoa:\n")).strip().lower().title()
        sorteados = [pessoa1,pessoa2,pessoa3,pessoa4,pessoa5,pessoa6]
        shuffle(sorteados)
        if qual == 1:
            print("A primeira pessoa foi {}\nA segunda pessoa foi {}\nA terceira pessoa foi {}\nA terceira pessoa foi {}\nA quarta pessoa foi {}\nA quinta pessoa foi {}\nA sexta pessoa foi".format(sorteados[0],sorteados[1],sorteados[2],sorteados[3],sorteados[4],sorteados[5]))
            sleep(2)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(3)
                break
        elif qual == 2:
            print("{} versus {}\n{} versus {}\n{} versus {}".format(sorteados[0],sorteados[1],sorteados[2],sorteados[3],sorteados[4],sorteados[5]))
            sleep(2)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(3)
                break
        elif qual == 3:
            print("A pessoa escolhida foi {}".format(choice(sorteados)))
            sleep(2)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(3)
                break

    elif quantos == 7:
        pessoa1 = str(input("Digite o nome da primeira pessoa:\n")).strip().lower().title()
        pessoa2 = str(input("Digite o nome da segunda pessoa:\n")).strip().lower().title() 
        pessoa3 = str(input("Digite o nome da terceira pessoa:\n")).strip().lower().title() 
        pessoa4 = str(input("Digite o nome da quarta pessoa:\n")).strip().lower().title()  
        pessoa5 = str(input("Digite o nome da quinta pessoa:\n")).strip().lower().title()
        pessoa6 = str(input("Digite o nome da sexta pessoa\n")).strip().lower().title()
        pessoa7 = str(input("Digite o nome da sétima pessoa:\n")).strip().lower().title()
        sorteados = [pessoa1,pessoa2,pessoa3,pessoa4,pessoa5,pessoa6,pessoa7]
        shuffle(sorteados)
        if qual == 1:
            print("A primeira pessoa foi {}\nA segunda pessoa foi {}\nA terceira pessoa foi {}\nA quarta pessoa foi {}\nA quinta pessoa foi {}\nA sexta pessoa foi{}\nA sétima pessoa foi {}".format(sorteados[0],sorteados[1],sorteados[2],sorteados[3],sorteados[4],sorteados[5],sorteados[6]))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(2)
                break
        elif qual == 2:
            print("O programa não é capaz de fazer versus com número ímpar, creio que não só o programa rsrsrs, então se esperar 5 segundos o programa se auto resetará e você poderá consertar")
            sleep(5)
        elif qual == 3:
            print("A pessoa escolhida foi {}".format(choice(sorteados)))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)\n"))
            if final == 2:
                sleep(2)
                break    
    elif quantos == 8:
        pessoa1 = str(input("Digite o nome da primeira pessoa:\n")).strip().lower().title()
        pessoa2 = str(input("Digite o nome da segunda pessoa:\n")).strip().lower().title()
        pessoa3 = str(input("Digite o nome da terceira pessoa:\n")).strip().lower().title()
        pessoa4 = str(input("Digite o nome da quarta pessoa:\n")).strip().lower().title()
        pessoa5 = str(input("Digite o nome da quinta pessoa:\n")).strip().lower().title()
        pessoa6 = str(input("Digite o nome da sexta pessoa:\n")).strip().lower().title()
        pessoa7 = str(input("Digite o nome da sétima pessoa:\n")).strip().lower().title()
        pessoa8 = str(input("Digite o nome da oitava pessoa:\n")).strip().lower().title()
        sorteados = [pessoa1,pessoa2,pessoa3,pessoa4,pessoa5,pessoa6,pessoa7,pessoa8]
        shuffle(sorteados)
        if qual == 1:
            print("A primeira pessoa foi {}\nA segunda pessoa foi {}\nA terceira pessoa foi {}\nA quarta pessoa foi {}\nA quinta pessoa foi {}\nA sexta pessoa foi {}\nA sétima pessoa foi {}\nA oitava pessoa foi {}".format(sorteados[0],sorteados[1],sorteados[2],sorteados[3],sorteados[4],sorteados[5],sorteados[6],sorteados[7]))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)"))
            if final == 2:
                sleep(2)
                break
        elif qual == 2:
            print("{} versus {}\n{} versus {}\n{} versus {}\n{} versus {}".format(sorteados[0],sorteados[1],sorteados[2],sorteados[3],sorteados[4],sorteados[5],sorteados[6],sorteados[7]))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)"))
            if final == 2:
                sleep(2)
                break                
        elif qual == 3:
            print("A pessoa escolhida foi {}".format(choice(sorteados)))
            sleep(3)
            final = int(input("Você quer fazer outra operação(1)\nVocê quer sair(2)"))
            if final == 2:
                sleep(2)
                break
        
        




