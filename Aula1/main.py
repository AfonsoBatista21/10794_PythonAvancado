#n = "Nome"
#ano = 2026
#print(n)

#print(f"Olá, {n}")
#print("Olá, " + n)
#print("Olá,", n)

# Outras formas de formatar strings
#print("Olá, {}".format(n))
#print("Olá", + n + "em" + str(ano))

#print(".............................")
# Operações matemáticas
#n1 = 10
#n2 = 10.0

#soma = n1 + n2
#print(soma)

#sub = n1 - n2
#print(sub)

#div = n1 / n2
#print(div)

#mult = n1 * n2  
#print(mult)

#print(".............................")
#condiçoes

# if - elif -else
# match - case

#idade = 10
#if idade <= 18:
    #print("Menor de idade")
#else:
    #print("Maior de idade")

#idade2 = 18
#if idade2 >= 18:
    #print("Adulto")
#elif idade2 >=12:
   # print("Adolescente")
#else:
    #print("Criança")

#crie uma app que receba 2 notas de um aluno 
#se as duas notas forem positivias (mais de 10) o aluno está aprovado
#se apenas uma das notas for positiva, o aluno pode fazer recuperação
#se nenhuma das notas for positiva, o aluno está reprovado

#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))

#if nota1 >= 10 and nota2 >= 10:
    #print("Aluno aprovado")

#elif nota1 > 10 or nota2 > 10:
    #print("Aluno em recuperação")   
#else:
    #print("Aluno reprovado")

#Crie um menu com 3 opções
# na opt 1 mostre a msg "Ola Mundo"
# na opt 2 mostre a msg "Bom dia"
# na opt 3 mostre a msg "Boa noite"
# se a opt for inválida mostre que a opt e inválida
while True:
    print("Menu:")
    print("1 - Olá Mundo")
    print("2 - Bom dia")
    print("3 - Boa noite")
    print("0 - Sair")

    escolha = int(input("Escolha uma opção: "))

    match escolha : 
        case 1:
            print("Olá Mundo")
        case 2:
            print("Bom dia")
        case 3:
            print("Boa noite")
        case 0:
            print("Saindo do programa.")
            break
        case _:
            print("Opção inválida")

#loops

#faça uma app que mostre o resultado da tabuada
#deve pedir um num da tabuada



#num = int(input("Escreve o numero da tabuada (1-10): "))
#if num < 1 or num > 10:
 #   print("Numero invalido")
#else:
    #for i in range(1, 11):
        #resultado = num * i
        #print(f"{num} x {i} = {resultado}")

#adapte o seu menu para este sempre pedir uma opção ate ser inserido o valor 

while True:
    
    num = int(input("Escreve o numero da tabuada (1-10) ou 0 para sair: "))

    if num == 0:
        print("Programa terminado.")
        break
    elif num < 1 or num > 10:
        print("Numero invalido\n")
    else:
        for i in range(1, 11):
            resultado = num * i
            print(f"{num} x {i} = {resultado}")
        print()

lst = ["elm1", "elm2", "elm3"]
print(lst)
lst.append("elm4")
print(lst)
lst.append(30)
print(lst)
lst.remove("elm4")
lst.pop(0)
print(lst)

cnt = lst.count("elm1")
print(cnt)

print(len(lst))
print(lst.__len__())

nome = "João"
print(nome.__len__())

print(lst[0])

# crie um programa que peça ao utilizador 5 nomes, mostre a lista dos nomes pedidos
nomes = []
for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)
print("Nomes inseridos:", nomes)

# crie um programa que peça ao utilizador nomes até ser inseriod "0"
# e mostre os nomes pedidos, deve mostrar um nome por linha 
#nomes1 = []
#while True:
   # nome = input("Digite um nome (ou 0 para sair): ")
  #  if nome == "0":
 #       break
   # nomes1.append(nome)
#print("Nomes inseridos:")
#for n in nomes1:
#    print(n)

#for elm in lst.__reversed__():
    #print(elm)

# dict 

aluno = {
    "nome": "Afonso",
    "media": 18,
    "estado": "aprovado"}

print(aluno)

aluno["escola"] = "ATEC"

print(aluno)

aluno["escola"] = "IEFP"

print(aluno)

aluno.pop("escola")

print(aluno)

aluno.popitem()
print(aluno)

def nome():
    print("antes")
    pass
    print("depois")

nome()

def soma(val1, val2):
    return val1 + val2

resultado = soma(10, 20)
print(resultado)

def soma2(val1: int, val2: int)-> int:
    return val1 + val2

res2= soma(val1=121, val2=12)
print(res2)

def demo (num: int, num2):
    pass