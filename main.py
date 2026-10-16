import mysql.connector

password = input("Введите пароль MySQL: ")

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="maksim_lab1",
        password=password,
        database="shop_lab1_maksim_20261009"
    )
except mysql.connector.Error as error:
    print("Ошибка подключения:", error)
else:
    print("Подключение успешно!")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM categories")
        for row in cursor.fetchall():
            print(row)
    finally:
        cursor.close()
        connection.close()