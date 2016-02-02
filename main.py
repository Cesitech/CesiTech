import sqlite3

fichierDonne = "./data.sq3"

conn = sqlite3.connect(fichierDonne)
cur = conn.cursor()
cur.execute("CREATE TABLE membres (age INTEGER, nom TEXT, taille REAL) ")
conn.commit()

cur.close()
conn.close()
