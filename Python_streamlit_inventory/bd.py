import mysql.connector

connection = mysql.connector.connect(
      host="estoque-crud-aws.c4nldr8vi3mq.sa-east-1.rds.amazonaws.com",
      user="admin",
      password="D7nI9z7wMNH?",
      database="estoque_crud"
  )

cursor = connection.cursor()
