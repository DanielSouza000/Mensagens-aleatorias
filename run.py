import mysql.connector
import random

mydb = mysql.connector.connect(
  host="sql10.freemysqlhosting.net",
  user="sql10665476",
  password="nGBLE49Flp",
  database="sql10665476"
)
mycursor = mydb.cursor()

def enviar():
  sql = "INSERT INTO Messages (Name, Message) VALUES (%s, %s)"
  nome = input("Escreva seu nome: ")
  mensagem = input("Escreva sua mensagem: ")
  val = (nome, mensagem)


  if nome.strip() == "" or mensagem.strip() == "":
    check = input("Você não escreveu um nome ou uma mensagem.")
    check = ""
  elif len(nome) > 25 or len(mensagem) > 100:
    check = input("O nome excedeu o limite (25), ou a mensagem excedeu o limite (100)")
    check = ""
  else:
    mycursor.execute(sql, val)

    mydb.commit()

    print("Sua mensagem foi enviada")

def ver():
  mycursor.execute("SELECT Name, Message FROM Messages")

  myresult = mycursor.fetchall()

  random_int = random.randint(0, len(myresult)-1)

  nome_aleatorio = myresult[random_int][0]
  men_aleatorio = myresult[random_int][1]

  print("\"",men_aleatorio,"\"\n","-",nome_aleatorio,"\n")


while True:
  opção = input("Digite o número 1 para enviar uma mensagem\nDigite o número 2 para ver uma mensagem aleatória\nDigite o número 3 para sair do programa\n")

  if opção.strip() == "1":
    enviar()
  elif opção.strip() == "2":
    ver()
  elif opção.strip() == "3":
    break

