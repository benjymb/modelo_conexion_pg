from conexion import ConexionPG


def main():
    conexion_pg = ConexionPG(
        direccion_servidor='127.0.0.1',  # localhost
        usuario='postgres',
        contrasena='yoursecurepassword',
        base_datos='example'
    )
    conexion_pg.crear_tabla()
    conexion_pg.insertar_datos(
       input('Escriba un nombre: ')
    )
    conexion_pg.eliminar_registro(1)
    conexion_pg.leer_datos()
main()
