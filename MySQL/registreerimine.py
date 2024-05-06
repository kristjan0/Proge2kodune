import mysql.connector

db = mysql.connector.connect(
    host="sql8.freemysqlhosting.net",
    user="sql8704546",
    password="pc8GgA2wtJ",
    database="sql8704546",
    port=3306,
)

cursor = db.cursor()

def registreerimine():
    user = input("Kasutajanimi: ")
    if check_user(user):
        print("Kasutaja on juba olemas")
        return
    password = input("Parool: ")
    cursor.execute("INSERT INTO users (user, password) VALUES (%s, md5(%s))", (user, password))
    db.commit()
    print("Registreerimine õnnestus")

def check_user(user):
    cursor.execute("SELECT * FROM users WHERE user = %s", (user,))
    result = cursor.fetchall()
    if len(result) >= 1:
        return True
    return False
    
if __name__ == "__main__":
    registreerimine()