from altas_empleados_mysql import conexion, tabla

def modificar(conexion):
    try:
        with open("entrada/modificaciones_mysql.txt", "r") as archivo:
            modificaciones = archivo.readlines()
        
        modificaciones_correctas = []
        modificaciones_erroneas = []
        
        with conexion.cursor() as cursor:
            for modificacion in modificaciones:
                codigo, nombre, apellidos, nif, departamento, num_hijos = modificacion.strip().split(";")
                try:
                    cursor.execute(f"""
                        UPDATE mae_empleados 
                        SET nombre="{nombre}", apellidos="{apellidos}", nif="{nif}", departamento="{departamento}", num_hijos={int(num_hijos)}
                        WHERE codigo="{codigo}"
                    """)
                    if cursor.rowcount > 0:
                        conexion.commit()
                        modificaciones_correctas.append(modificacion)
                    else:
                        modificaciones_erroneas.append(modificacion)
                        conexion.rollback()
                except Exception as e:
                    modificaciones_erroneas.append(modificacion)
                    conexion.rollback()
        
        with open("salida/modificaciones_correctas_mysql.txt", "w") as archivo_correctas:
            archivo_correctas.writelines(modificaciones_correctas)
        
        with open("salida/modificaciones_erroneas_mysql.txt", "w") as archivo_erroneas:
            archivo_erroneas.writelines(modificaciones_erroneas)
        
        print("Proceso de modificación finalizado.")
    except Exception as e:
        print(f"Error al procesar el archivo de modificaciones: {e}")


if __name__ == "__main__":
    conexion = conexion()
    tabla(conexion)
    modificar(conexion)
    if conexion is not None:
        conexion.close()