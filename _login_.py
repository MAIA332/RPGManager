def logar():
    print("====LOGIN====")
    email = input("\n-- Digite seu E-mail: ")
    senha = input("-- Digite sua Senha: ")

    f = open("files/users.txt","r")
    
    for i in f.readlines(): 
        i =  i.split(",")
        if email in i:
            if senha in i:
                return {"Loged":True,"Usuario":i[1]}
            else:
                return {"Loged":False,"Usuario":"None"}
        else:
            return {"Loged":False,"Usuario":"None"}
    
    f.close()

def registrar():
    print("====REGISTRAR====")
    
    email = input("\n-- Digite seu E-mail: ")
    senha = input("-- Digite sua Senha: ")
    nome = input("-- Digite seu nome: ")
    nasc = input("-- Digite sua data de nascimento: ")

    f = open("files/users.txt","a")
    f.writelines(f"\n{nome},{email},{senha},{nasc}")
    f.close()

    return {"Loged":True,"Usuario":email}

