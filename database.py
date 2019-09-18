import psycopg2

#psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
#psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

databases = {}

class Database():
  def __init__(self, name):
    global databases
    if name not in databases:
      conn = psycopg2.connect(database=name, user='postgres')
      cursor = conn.cursor()
      databases[name] = (conn, cursor)
    self.conn, self.cursor = databases[name]
  def __del__(self):
    global databases
    if False:
      cursor.close()
      cursor = None
      conn.close()
      conn = None
  def execute(self,sql):
    self.cursor.execute(sql.encode('utf-8'))
  def lastval(self):
      self.execute('SELECT LASTVAL()')
      return self.fetchone()[0]
  def fetchone(self):
    return self.cursor.fetchone()
  def fetchall(self):
    return self.cursor.fetchall()
  def rollback(self):
    return self.conn.rollback()
  def commit(self):
    return self.conn.commit()
