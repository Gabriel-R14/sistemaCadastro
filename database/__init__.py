def cadastroEmail(email):
    arqMail = open('email.txt', 'a')
    arqMail.write(f'{email}\n')

def cadastroName(name):
    arqName = open('name.txt', 'a')
    arqName.write(f'{name}\n')

def cadastroSenha(senha):
    arqPassword = open('senha.txt', 'a')
    arqPassword.write(f'{senha}\n')

def verificaDados():
    while True:
        arqEmailOpen = open('email.txt', 'r')
        arqNameOpen = open('name.txt', 'r')
        mailList = arqEmailOpen.readlines()
        nameList = arqNameOpen.readlines()
        arqPasswordOpen = open('senha.txt', 'r')
        passwordList = arqPasswordOpen.readlines()
        nameEmail = input('Digite seu nome de usuário ou endereço de email: ')
        if nameEmail in mailList:
            password = input('Digite sua senha: ')
            if password in passwordList:
                for e in mailList:
                    for p in passwordList:
                        if mailList.index(nameEmail) == passwordList.index(password):
                            print('Login efetuado com sucesso!')
                            break
                        else:
                            print('Digite sua senha corretamente')
            else:
                while password not in passwordList:
                    print('Por favor digite uma senha válida')
                    password = input('Digite sua senha: ')
            break
        elif nameEmail in nameList:
            password = input('Digite sua senha: ')
            if password in passwordList:
                for n in nameList:
                    for p in passwordList:
                        if nameList.index(nameEmail) == passwordList.index(password):
                            print('Login efetuado com sucesso!')
                            break
                        else:
                            print('Digite sua senha corretamente')
            else:
                print('Por favor digite uma senha válida')
                while password not in passwordList:
                    print('Por favor digite uma senha válida')
                    password = input('Digite sua senha: ')
            break
        else:
            print('Por favor digite um nome de usuário ou e-mail válido')      