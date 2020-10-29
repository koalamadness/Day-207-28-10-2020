import mysql.connector 

bd = mysql.connector.connect(user='pol', password='12345678', database='nopalito')

cursor = bd.cursor()

while True:
    print("1) Agregar usuario")
    print("2) Mostrar usuarios")
    print("0) Salir")
    op = input()

    if op == '1':
        correo = input("Correo: ")
        nombre = input("Nombre: ")
        contra = input("Contraseña: ")

        consulta = "INSERT INTO usuario (nombre, correo, contrasena) " \
                    "VALUES(%s, %s, %s)"

        cursor.execute(consulta, (nombre, correo, contra))
        bd.commit()

        if cursor.rowcount:
            print("Se agregó usuario")
        else:
            print("Error")

    if op == '2':
        consulta = "SELECT * FROM usuario"

        cursor.execute(consulta)

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("nombre: ", row[1])
            print("correo: ", row[2])
            print("contraseña: ", row[3])
    elif op == '0':
        break