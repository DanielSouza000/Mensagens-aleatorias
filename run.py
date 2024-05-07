import mysql.connector
import random
import os

timeout = 10
mydb = mysql.connector.connect(
  charset="utf8mb4",
  host="mysql-1b8e19e2-mensagensaleatorias.d.aivencloud.com",
  user="newuser",
  password="xVN<znE38HR9]-MJsrBU(W",
  database="mensagensaleatorias",
  port=13649)

mycursor = mydb.cursor()

def enviar():
  sql = "INSERT INTO mensagens (nome, mensagem) VALUES (%s, %s)"
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
    mycursor.execute(sql, val)

    mydb.commit()

    print("Sua mensagem foi enviada")
    check = input("Pressione Enter para continuar")
    check = ""

def ver():
  mycursor.execute("SELECT nome, mensagem FROM mensagens")

  myresult = mycursor.fetchall()

  random_int = random.randint(0, len(myresult)-1)

  nome_aleatorio = myresult[random_int][0]
  men_aleatorio = myresult[random_int][1]

  print("\"",men_aleatorio,"\"\n","-",nome_aleatorio,"\n")
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