import mysql.connector
import hashlib

db = mysql.connector.connect(
    host="sql8.freemysqlhosting.net",
    user="sql8704546",
    password="pc8GgA2wtJ",
    database="sql8704546",
    port=3306,
)

cursor = db.cursor()

def sisselogimine():
    user = input("Kasutajanimi: ")
    password = input("Parool: ")
    md5_password = hashlib.md5(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM users WHERE user = %s AND password = %s", (user, md5_password))
    result = cursor.fetchall()
    if len(result) == 1:
        print("Sisselogimine õnnestus")
    else:
        print("Sisselogimine ebaõnnestus")

if __name__ == "__main__":
    sisselogimine()

