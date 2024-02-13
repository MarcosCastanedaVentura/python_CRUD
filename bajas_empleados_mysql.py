from altas_empleados_mysql import conexion, tabla

def dar_de_baja(conexion):
    try:
        with open("entrada/bajas_mysql.txt", "r") as archivo:
            codigos = archivo.readlines()
        
        bajas_correctas = []
        bajas_erroneas = []
        
        with conexion.cursor() as cursor:
            for codigo in codigos:
                codigo = codigo.strip()
                try:
                    cursor.execute(f"""
                        DELETE FROM mae_empleados WHERE codigo = "{codigo}"
                    """)
                    if cursor.rowcount > 0:
                        conexion.commit()
                        bajas_correctas.append(codigo + "\n")
                    else:
                        bajas_erroneas.append(codigo + "\n")
                        conexion.rollback()
                except Exception as e:
                    bajas_erroneas.append(codigo + "\n")
                    conexion.rollback()
        
        with open("salida/bajas_correctas_mysql.txt", "w") as archivo_correctas:
            archivo_correctas.writelines(bajas_correctas)
        
        with open("salida/bajas_erroneas_mysql.txt", "w") as archivo_erroneas:
            archivo_erroneas.writelines(bajas_erroneas)
        
        print("Proceso de eliminación completado.")
    except Exception as e:
        print(f"Error al procesar el archivo de bajas: {e}")


if __name__ == "__main__":
    conexion = conexion()
    tabla(conexion)
    dar_de_baja(conexion)
    if conexion is not None:
        conexion.close()

