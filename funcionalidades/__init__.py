def verificaDados():
    arqEmailOpen = open('email.txt', 'r')  
    arqNameOpen = open('name.txt', 'r')
    arqPasswordOpen = open('senha.txt', 'r')
    mailList = arqEmailOpen.readlines()
    for c in range(0, len(mailList)):
        mailList[c] = mailList[c].replace('\n', '')
    nameList = arqNameOpen.readlines()
    for c in range(0, len(nameList)):
        nameList[c] = nameList[c].replace('\n', '')
    passwordList = arqPasswordOpen.readlines()
    for c in range(0, len(passwordList)):
        passwordList[c] = passwordList[c].replace('\n', '')
    nameEmail = input('Digite seu nome de usuário ou endereço de email: ')
    password = input('Digite sua senha: ')
    while True:
        if nameEmail in mailList:
            if password in passwordList:
                if mailList.index(nameEmail) == passwordList.index(password):
                    print('Login efetuado com sucesso!') 
                    break
                else:
                    print('Sua senha, nome de usuário ou email estão incorretos, digite-os novamente')
                    nameEmail = input('Digite seu nome de usuário ou endereço de email: ')
                    password = input('Digite sua senha: ')
            else:
                print('Sua senha, nome de usuário ou email estão incorretos, digite-os novamente')
                nameEmail = input('Digite seu nome de usuário ou endereço de email: ')
                password = input('Digite sua senha: ')
        elif nameEmail in nameList:
            if password in passwordList:
                if nameList.index(nameEmail) == passwordList.index(password):
                    print('Login efetuado com sucesso!')
                    break
                else:
                    print('Sua senha, nome de usuário ou email estão incorretos, digite-os novamente')
                    nameEmail = input('Digite seu nome de usuário ou endereço de email: ')
                    password = input('Digite sua senha: ')
            else:
                print('Sua senha, nome de usuário ou email estão incorretos, digite-os novamente')
                nameEmail = input('Digite seu nome de usuário ou endereço de email: ')
                password = input('Digite sua senha: ')
        else:
            print('Sua senha, nome de usuário ou email estão incorretos, digite-os novamente')
            nameEmail = input('Digite seu nome de usuário ou endereço de email: ')
            password = input('Digite sua senha: ')