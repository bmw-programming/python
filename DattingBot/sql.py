# -*- coding: utf-8 -*-
import sqlite3
class sql:
    def __init__(self):
        pass
    def select(self, id):
        x = False
        sqlconnect = sqlite3.connect("Base1.db")
        c = sqlconnect.cursor()
        c.execute('SELECT TelegramID FROM Users')
        rows = c.fetchall()     
        for row in rows:
            if(row[0] == id):
                x = True
        sqlconnect.commit()
        sqlconnect.close()
        return x
    def regisrt(self,id):
        sqlconnect = sqlite3.connect('Base1.db')
        c = sqlconnect.cursor()
        c.execute(("""INSERT INTO 'Users' (TelegramID,CityReg) 
                            VALUES ('%s','%s');
                            """) % (id,0))
        sqlconnect.commit()
        sqlconnect.close()
    def statistika(self):
        x = 0
        sqlconnect = sqlite3.connect('Base1.db')
        c = sqlconnect.cursor()
        c.execute('SELECT TelegramID FROM Users')
        rows = c.fetchall()
        sqlconnect.commit()
        sqlconnect.close()
        return len(rows)
    
    def cityregret(self,id):
        sqlconnect = sqlite3.connect('Base1.db')
        c = sqlconnect.cursor()
        c.execute('SELECT CityReg FROM Users WHERE TelegramID='+str(id))
        rows = c.fetchone()
        sqlconnect.commit()
        sqlconnect.close()
        return rows[0]
    def addcity(self,id, city):
        sqlconnect = sqlite3.connect('Base1.db')
        c = sqlconnect.cursor()
        c.execute('UPDATE Users SET City =:bal WHERE TelegramID =:id', {"id": id, "bal": city})
        sqlconnect.commit()
        sqlconnect.close()
        return
    def zerotoone(self,id):
        sqlconnect = sqlite3.connect('Base1.db')
        c = sqlconnect.cursor()
        c.execute('UPDATE Users SET CityReg =:bal WHERE TelegramID =:id', {"id": id, "bal": 1})
        sqlconnect.commit()
        sqlconnect.close()
        return
        
    
    
    
    
    
    
    
    