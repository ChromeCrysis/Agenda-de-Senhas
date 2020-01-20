import sqlite3

conn = sqlite3.connect('senhas.db')

from funcoes import *

while True:
    menu()
    op = input("O que deseja fazer?")
    if op not in ['i', 'ls', 'rec', 's']:
        print("Opção inválida!")
        continue

    if op == 's':
        break

    if op == 'i':
        print("Insira os dados:\n ")
        servico = input("Digite o serviço que utiliza esta senha: ")
        usuario = input("Digite o nome de usuario: ")
        senha = input("Digite a senha: ")
        inserir_senha(servico, usuario, senha)

    if op == 'ls':
        listar_cadastros()
    
    if op == 'rec':
        servico = input("Digite qual o serviço que utiliza a senha que vai recuperar: ")
        recuperar_senhas(servico)

conn.close()