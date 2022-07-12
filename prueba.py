from balance.models import DBManager

manager = DBManager('data/balance.db')
sql = "SELECT id, fecha, concepto, tipo, cantidad FROM movimientos ORDER BY cantidad DESC"
manager.consulta_SQL(sql)
