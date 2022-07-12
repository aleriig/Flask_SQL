import sqlite3

class DBManager:
    def __init__(self, ruta):
        self.ruta = ruta

    def consulta_SQL(self, consulta):
        # 1. conectar con DB
        conexion = sqlite3.connect(self.ruta)

        # 2. abrir un cursor
        cursor = conexion.cursor()

        # 3. ejecutar consulta SQL
        cursor.execute(consulta)

        # 4. tratar los datos
            # 4.1 obtengo nombres de columna
            # 4.2 pedir todos los datos
            # 4.3 recorrer los resultados
                # 4.3.1 crear un diccionario
                        # - recorro la lista de nombres de columna
                        # - para cada columna: nombre + valor
                # 4.3.2 guardar en la lista de movimientos
        #   [   {'nomb_col1' : 'val_col1',......}   ]

        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            nombres_columnas.append(desc_columna[0])
        # nombres_columnas = ['id', 'fecha', 'tipo', 'cantidad']

        datos = cursor.fetchall()
        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre]=dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        conexion.close()

        return self.movimientos

    def borrar(self, id):
        consulta = "DELETE FROM movimientos WHERE id=?"
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        # muy importante validar datos para evitar daños de una fuente externa
        try:
            cursor.execute(consulta, (id, ))
            # hacemos un commit para guardar los datos, en este caso los borrar elementos
            conexion.commit()
            resultado = True
        except:
            # con el rollback podemos recuperar los datos
            conexion.rollback()
            conexion.close()
        return resultado