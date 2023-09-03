import _login_,_mundos_,os

def menuDeLogin()->None:
    while True:
        os.system("CLS")
            
        print("=======SEJA BEM VINDO======== \n \n -- Vamos começar? \n \n| FAZER LOGIN (1) | REGISTRAR-SE (2) |")
        op = input("\nop:> ")

        if op == "1":
            
            obj = _login_.logar()
            #print(obj)

            if obj["Loged"] == True:
                print("Logando...")
                #print(obj["Usuario"])
                return obj
            else:
                print("Credenciais incorretas")

        elif op == "2":
            obj = _login_.registrar()
            print("\nRegistrando...")
            return obj
        
        else:
            print("Desculpe, não entendi :(")

def menuDeMundos(login_obj)->None:
    while True:
        os.system("CLS")
        print("=======MENU DE MUNDOS======== \n \n| CRIAR NOVO MUNDO (1) | VER MEUS MUNDOS (2) | DELETAR MUNDO (3) | SELECIONAR MUNDO (4) |")
        op = input("\n op:> ")

        if op == "1":
            _mundos_.criarNovo(login_obj["Usuario"])
        elif op=="2":
            _mundos_.verMundos(login_obj["Usuario"])
        elif op=="3":
            _mundos_.delMundos(login_obj["Usuario"])

        elif op=="4":
            _mundos_.playMundo(login_obj["Usuario"])

login_obj = menuDeLogin()
menuDeMundos(login_obj)
