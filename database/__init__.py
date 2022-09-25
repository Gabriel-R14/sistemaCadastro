def cadastroEmail(email):
    arqMail = open('email.txt', 'a')
    arqMail.write(f'{email}\n')

def cadastroName(name):
    arqName = open('name.txt', 'a')
    arqName.write(f'{name}\n')

def cadastroSenha(senha):
    arqPassword = open('senha.txt', 'a')
    arqPassword.write(f'{senha}\n')
