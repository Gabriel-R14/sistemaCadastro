import smtplib as gmail
import random
from database import cadastroEmail, cadastroName, cadastroSenha, verificaDados

server = gmail.SMTP_SSL('smtp.gmail.com', 465)
de = 'email'
server.login(de, 'codigo')

menu = int(input('[ 1 ] Registrar\n[ 2 ] Login\n[ 3 ] Sair\n--> '))
while menu not in (1, 2, 3):
    print('Por favor escolha uma opção válida')
    menu = int(input('[ 1 ] Registrar\n[ 2 ] Login\n[ 3 ] Sair\n--> '))

if menu == 1:
    username = input('Crie um nome de usuário: ')
    email = input('Digite um email: ')
    senha = input('Crie uma senha com no mínimo 8 caracteres: ')
    while len(senha) < 8:
        print('Utilize no minímo 8 caracteres')
        senha = input('Crie uma senha com no mínimo 8 caracteres: ')
    senhaConfirma = input('Confirme sua senha: ')
    while senhaConfirma != senha:
        print('Por favor confirme sua senha corretamente')
        senhaConfirma = input('Confirme sua senha: ')
    v2fcode = str(random.randint(100000, 999999))
    para = email
    msg = v2fcode
    server.sendmail(de, para, msg)
    server.quit()
    v2f = input('Conta cadastrada, digite o código enviado no seu email para continuar: ')
    while v2f != v2fcode:
        print('Falha ao verificar código, tente novamente')
        v2f = input('Conta cadastrada, digite o código enviado no seu email para continuar: ')
    print('Conta criada com sucesso, volte ao menu para realizar o login')
    cadastroEmail(email)
    cadastroName(username)
    cadastroSenha(senha)

elif menu == 2:
    verificaDados()
    
elif menu == 3:
    print('Obrigado por utilizar nosso sistema')
    exit()
