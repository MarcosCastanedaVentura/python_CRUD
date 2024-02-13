from pymysql import connect
    
def conexion():
    try:
        conexion = connect(
            host="localhost",
            user="root",
            password="",
            database="CRUD"
        )
        print("Conexión establecida.")
        return conexion
    except connect.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
        
        
def tabla(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mae_empleados (
                    codigo VARCHAR(4) NOT NULL PRIMARY KEY,
                    nombre VARCHAR(30) NOT NULL,
                    apellidos VARCHAR(45) NOT NULL,
                    nif VARCHAR(9) NOT NULL,
                    departamento VARCHAR(15) NOT NULL,
                    num_hijos INT NOT NULL
                )
            """)
        print("La tabla ha sido creada con éxito.")
    except Exception as e:
        print(f"No se ha podido crear la tabla: {e}")


def dar_de_alta(conexion):
    try:
        with open("entrada/altas_mysql.txt", "r") as archivo:
            empleados = archivo.readlines()
        
        altas_correctas = []
        altas_erroneas = []
        
        with conexion.cursor() as cursor:
            for empleado in empleados:
                codigo, nombre, apellidos, nif, departamento, num_hijos = empleado.strip().split(";")
                try:
                    cursor.execute(f"""
                        INSERT INTO mae_empleados (codigo, nombre, apellidos, nif, departamento, num_hijos)
                        VALUES ("{codigo}", "{nombre}", "{apellidos}", "{nif}", "{departamento}", {int(num_hijos)})
                    """)
                    conexion.commit()
                    altas_correctas.append(empleado)
                except Exception as e:
                    altas_erroneas.append(empleado)
                    conexion.rollback()
        
        with open("salida/altas_correctas_mysql.txt", "w") as archivo_correctas:
            archivo_correctas.writelines(altas_correctas)
        
        with open("salida/altas_erroneas_mysql.txt", "w") as archivo_erroneas:
            archivo_erroneas.writelines(altas_erroneas)
        
        print("Proceso de inserción finalizado.")
    except Exception as e:
        print(f"Error al procesar el archivo de altas: {e}")



if __name__ == "__main__":
    conexion = conexion()
    tabla(conexion)
    dar_de_alta(conexion)
    if conexion is not None:
        conexion.close()