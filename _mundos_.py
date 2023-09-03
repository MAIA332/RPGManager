import os
def criarNovo(user):
    mundo = {
        "apelido":input("\n--Digite um nome para o mundo: "),
        "usuario":user,
        "ativo":True,
        "Contexto":"",
        "personagens": []
    }

    c = getContext()

    mundo["Contexto"] = c

    try:
        resp="s"
        while resp == "s":
            p = criarPersonagens()
            mundo["personagens"].append(p)
            resp = input("Deseja cadastrar outro personagem? (s/n): ")
            if resp != "s" and resp !="n":
                print("\nDesculpe não entendi :(")
                os.system("PAUSE")
        
        f = open("files/mundos/mundos_index.txt","a")
        f.writelines(f"{mundo['apelido']},{mundo['ativo']},{mundo['usuario']}\n")
        f.close()
   

        n = f"files/mundos/{mundo['apelido']}.txt"

        with open(n, 'w') as f:
            for key, value in mundo.items(): 
                f.write('%s?%s\n' % (key, value))
            f.close()

    except Exception as e:
        print("\nOps não funcionou, tente novamente")
        os.system("PAUSE")

    #print(f"criado {mundo}")

def getContext():
    contextos = {
        "CYBERPUNK":{
            "nome":"Cyberpunk 2077",
            "Desc":"As mega corporacoes conseguiram se tornar tao poderosas que tem mais poderes que alguns paises. Pessoas vivem em pessimas condicoes de vida e tem que se virar do jeito que podem. A internet evoluiu a ponto de pessoas se conectarem a ela com a mente, o mundo é perigoso e cheio de vigaristas e drogados. A principal localização é uma cidade chamada de Night City, que fica no estado da California. Sua luta e contra grandes corporacoes e o governo em um mundo de crimonosos e desajustados.",
        },
        "POSAPOCALIPTICO":{
            "nome":"Encased",
            "Desc":"A Guerra Fria acabou quando a Dome apareceu, todas as nações se uniram para descobrir os segredos desta estrutura e não tão secretamente enriquecer à custa dos recursos e artefactos encontrados dentro da mesma. Para isso, foi criada uma espécie de força internacional destinada a explorar a Dome, nomeada CRONUS, sendo que qualquer pessoa no mundo se pode inscrever na mesma. Esta decisão pode parecer uma forma fácil de enriquecer e viver uma vida de aventura mas é também ume decisão sem retorno.",
        },
        "UCRONICA":{
            "nome":"Man In The High Castle",
            "Desc":"O que teria acontecido com o mundo se as Forças Aliadas tivessem perdido a Segunda Guerra Mundial? Vinte anos após a derrota, o planeta agora está dividido entre Japão e Alemanha, os maiores Estados Hegemônicos. À medida que a tensão entre essas duas hegemonias cresce, e isso gera consequências drásticas nos Estados Unidos e nos Estados opositores, se aventura entre as forças rebeldes e lute contra a ditadura.",
        }
    }

    try:

        c="n"
        while c == "n":
        
            print("Qual contexto deseja escolher? Digite um dos nomes")
            
            for i in contextos.keys():
                print(f"--{i}")

            op = input("op:> ").upper()
            
            print(contextos[op]["nome"])
            print(contextos[op]["Desc"])

            c = input("\nDeseja manter esse contexto? (s/n): ")
            if c != "s" and c !="n":
                print("\nDesculpe não entendi :(")
                os.system("PAUSE")

        return contextos[op]

    except Exception as e:
        print("\nOps não funcionou, tente novamente")
        os.system("PAUSE")


def criarPersonagens():
    classes = {
        "CAÇADOR":{
            "Forca":"10",
            "Velocidade":"20",
            "Resistencia":"10",
            "Destreza":"15",
            "Vida":"100"  
        },
        "BRUTAMONTES":{
            "Forca":"20",
            "Velocidade":"10",
            "Resistencia":"15",
            "Destreza":"10",
            "Vida":"100"  
        },
        "ENGENHEIRO":{
            "Forca":"10",
            "Velocidade":"10",
            "Resistencia":"10",
            "Destreza":"25",
            "Vida":"100"  
        }
    }
    personagem = {
        "nome":input("\n--Digite um nome para o personagem: "),
        "classe":""
    }

    try:

        print("Qual Classe deseja escolher? Digite um dos nome")
        
        for i in classes.keys():
            print(f"--{i}")

        op = input("op:> ").upper()

        personagem["classe"] = classes[op]
        return personagem
    
    except Exception as e:
        print("\nOps não funcionou, tente novamente")
        os.system("PAUSE")
    
def verMundos(user):
    try:
        f = open("files/mundos/mundos_index.txt","r")
        for i in f.readlines(): 
            i =  i.split(",")
            if "True" in i[1]:
                if user in i[2]:
                    print(i[0])
        f.close()
    
    except Exception as e:
        print("\nOps não funcionou, tente novamente")
        os.system("PAUSE")

    os.system("PAUSE")

def playMundo(user):

    try:
        
        print("\nQual mundo deseja selecionar hoje? Digite o nome como aparece!!")
        verMundos(user)
        op = input("Nome Do Mundo:> ")

        dictionary = {}

        with open(f"files/mundos/{op}.txt") as file:
            for line in file:
                (key, val) = line.split("?")
                dictionary[key] = val
        
        for key,value in dictionary.items():
            print(f"{key}:{value}\n")
    
    except Exception as e:
        print("\nOps não funcionou, tente novamente")
        os.system("PAUSE")

    os.system("PAUSE")
    


def delMundos(user):

    try:
        print("\nQual mundo deseja deletar? Digite o nome como aparece!!")
        verMundos(user)
        op = input("Nome Do Mundo:> ")
        
        c = input("\nTem certeza que deseja deletar? (s/n): ")

        if c == "s":

            f = open("files/mundos/mundos_index.txt","r+")
            temp = []

            for i in f.readlines(): 
            
                i =  i.split(",")
            
                if op == i[0]:
                    if user in i[2]:
                        i[1] = "False"

                temp.append(i)

            print(temp)

            f.seek(0)
            for i in temp:
                f.write(f"{i[0]},{i[1]},{i[2]}")

            f.truncate()
        
            f.close()

            os.remove(f"files/mundos/{op}.txt")

            print("Arquivo deletado com sucesso")
            os.system("PAUSE")

        elif c == "n":
            print("\nOk, vamos voltar")
            os.system("PAUSE")
   
    except Exception as e:
        print("\nOps não funcionou, tente novamente")
        os.system("PAUSE")

