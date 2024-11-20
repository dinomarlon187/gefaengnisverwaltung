import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files["prison_database.db"])
  cursor = conn.cursor()
  res = list(cursor.execute('''
  SELECT Name,GID FROM tblGefaengnis;
  '''))
  conn.close()
  return res

@anvil.server.callable
def get_direktor(GID):
  conn = sqlite3.connect(data_files["prison_database.db"])
  cursor = conn.cursor()
  res = list(cursor.execute('''
  SELECT Direktor FROM tblVerwaltung WHERE fk_GID = ?
  ''', (str(GID))))
  return res[0][0]

@anvil.server.callable
def get_freieZellen(GID):
  conn = sqlite3.connect(data_files["prison_database.db"])
  cursor = conn.cursor()
  res = list(cursor.execute('''
  SELECT freie_Zellen from tblVerwaltung WHERE fk_GID = ?
  ''', (str(GID))))
  return res[0][0]

@anvil.server.callable
def get_ZellenData(GID):
  data = []
  conn = sqlite3.connect(data_files["prison_database.db"])
  cursor = conn.cursor()
  res = list(cursor.execute('''
  SELECT ZID from tblZelle WHERE fk_GID = ?
  ''', (str(GID))))
  
  for item in res:
    print(item[0])
    check = list(cursor.execute(f'''
    SELECT COUNT(ZHID) AS Count FROM tblZelleHaeftling WHERE Auszug = NULL & fk_ZID = {item[0]}
    '''))
    
  data.append((check[0][0],item[0]))
  print(data)
  return data
  

