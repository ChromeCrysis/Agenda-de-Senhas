import sqlite3

conn = sqlite3.connect('senhas.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS senhas(
        servico TEXT NOT NULL,
        usuario TEXT NOT NULL,
        senha TEXT NOT NULL
    );
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        login TEXT NOT NULL,
        password TEXT NOT NULL
    );
''')

def menu():
    print("-------------------------------------------------")
    print("Digite l para fazer login e c para fazer cadastro")
    print("-------------------------------------------------")
    op = input("Digite o comando desejado: ")
    if op not in ['c', 'l']:
        print("Comando errado, tente novamente.")
        menu()
    else:
        if op == 'l':
            menu_login()
        if op == 'c':
            cadastro_form()

def menu_principal():
    print("----------------------------------------")
    print("|i : para inserir nova senha           |")
    print("|ls : para listar cadastros já feitos  |")
    print("|rec : para recuperar uma senha        |")
    print("|s : para sair                         |")
    print("----------------------------------------")

def valida_login(login, password):
    '''
        Método sendo criado.
    '''

def menu_login():
    print("----------------------------------------")
    login = input("Login: ")
    password = input("Senha: ")
    print("----------------------------------------")

def cadastro(login, password):
    try:
        conn.execute(f'''
        INSERT INTO usuarios (login, password) VALUES (
            '{login}', '{password}'
        );
        ''')
        conn.commit()
        print("Usuário cadastrado com sucesso. ")
        menu_principal()
    except:
        return print("Não foi possível cadastrar, por favor tente novamente.")
        cadastro()

def cadastro_form():
    print("Cadastrando-se no sistema")
    login = input("Digite o nome de usuário: ")
    password = input("Digite a senha que deseja cadastrar: ")
    cadastro(login, password)

def inserir_senha(servico, usuario, senha):
    cursor.execute(f'''
        INSERT INTO senhas (servico, usuario, senha) VALUES (
            '{servico}', '{usuario}', '{senha}'
        );
    ''')
    conn.commit()

def recuperar_senhas(servico):
    cursor.execute(f'''
        SELECT usuario, senha FROM senhas WHERE servico = '{servico}';
    ''')
    for senhas in cursor.fetchall():
        print(senha)

def listar_cadastros():
    cursor.execute('''
        SELECT servico FROM senhas;
    ''')
    for servico in cursor.fetchall():
        print(servico)