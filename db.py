# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:34:39 2023

@author: ASHOK
"""

import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql='''
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
            )
        '''
        
        self.cur.execute(sql)
        self.con.commit()
        
    #Insert Function
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute('insert into employees values(NULL,?,?,?,?,?,?,?)',
                         (name,age,doj,email,gender,contact,address))
        self.con.commit()
        
    # Fetch all data from DB
    def fetch(self):
        self.cur.execute('SELECT DISTINCT * FROM EMPLOYEES')
        rows=self.cur.fetchall()
        return rows
        
    # Delete a Record in DB
    def remove(self,id):
        self.cur.execute('delete from employees where id=?',(id,))
        self.con.commit()
 
    # Update a record in DB
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.con.execute('update employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?',
                         (name,age,doj,email,gender,contact,address,id))
        self.con.commit()
        
        
#o=Database('Employee.db')
#o.insert('Ram','25','12-10-2020','ram@gmail.com','male','6733929820','Cherry Road,Salem')
#o.insert('Sam','25','12-11-2020','sam@gmail.com','male','7846932451','Gandhi Road,Salem')

#o.update('2','sam kumar','35','12-12-2020','samkumar@gmail.com','male','5638288922','test road,salem')
#print(o.fetch())