import random
import os
import pymysql
import pymysql.cursors

timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="mensagensaleatorias",
    host="mysql-1b8e19e2-mensagensaleatorias.d.aivencloud.com",
    password="xVN<znE38HR9]-MJsrBU(W",
    read_timeout=timeout,
    port=13649,
    user="newuser",
    write_timeout=timeout,
)
def enviar():
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `mensagens` (`nome`, `mensagem`) VALUES (%s, %s)"
            nome = input("Escreva seu nome: ")
            mensagem = input("Escreva sua mensagem: ")
            val = (nome, mensagem)
            if nome.strip() == "" or mensagem.strip() == "":
                check = input("Você não escreveu um nome ou uma mensagem.")
                check = ""
            elif len(nome) > 40 or len(mensagem) > 200:
                check = input("O nome excedeu o limite (40), ou a mensagem excedeu o limite (200)")
                check = ""
            else:
                cursor.execute(sql, val)
                connection.commit()

def ver():
    with connection.cursor() as cursor:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT nome, mensagem FROM mensagens")
        myresult = cursor.fetchall()
        random_int = random.randint(0, len(myresult)-1)
        print("\"",myresult[random_int]["nome"],"\"\n","-",myresult[random_int]["mensagem"],"\n")
        check = input("Pressione Enter para continuar")
        check = ""

while True:
  os.system('cls')
  
  opção = input("Digite o número 1 para enviar uma mensagem\nDigite o número 2 para ver uma mensagem aleatória\nDigite o número 3 para sair do programa\n")

  if opção.strip() == "1":
    enviar()
  elif opção.strip() == "2":
    ver()
  elif opção.strip() == "3":
    break
