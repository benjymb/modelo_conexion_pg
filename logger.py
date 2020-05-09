def escribir_al_log(excepcion, texto):
    with open('error.log', 'a+') as archivo_log:
        archivo_log.write('----------------------------------------------------------------\n')
        archivo_log.write(str(excepcion))
        archivo_log.write(texto)
        archivo_log.write('----------------------------------------------------------------\n')