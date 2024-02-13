from altas_empleados_mysql import conexion, tabla

def consultar(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM mae_empleados")
            empleados = cursor.fetchall()
        
        with open("salida/consulta_mysql.txt", "w") as archivo:
            for empleado in empleados:
                archivo.write(";".join(str(dato) for dato in empleado) + "\n")
                
        print("Proceso de consulta finalizado.")
    except Exception as e:
        print(f"Error al realizar la consulta: {e}")


if __name__ == "__main__":
    conexion = conexion()
    tabla(conexion)
    consultar(conexion)
    if conexion is not None:
        conexion.close()
