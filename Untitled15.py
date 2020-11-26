#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pyodbc


if __name__ == '__main__':
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-52RKDC0\SQLEXPRESS;'
                          'Database=WideWorldImporters-Full;'
                          'Trusted_Connection=yes;')
                          
    before_chang = "select PersonID, FullName, PreferredName from Application.People where PersonID=3"
                          
    try:
        conn.autocommit = False
        cursor = conn.cursor()
        after_changing = "update Application.People set FullName = 'adel' where PersonID=3"
        cursor.execute(after_changing)  
        conn.commit()
        print('commited')
                          
    except Exception:
        conn.rollback()
        print('rollback')
        #Transaction
                          
    finally:
        cursor.execute(before_chang)
        for r in cursor.fetchall():
            print(r)
        cursor.close()
        conn.close()
        print("connection is closed")

