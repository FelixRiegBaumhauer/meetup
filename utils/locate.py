#THIS IS WHERE THE LOACTION FXNS AND SO ON WILL GO
#making this show all locations for now

import sqlite3

def retUsers():
    db=sqlite3.connect("data/users.db")
    c=db.cursor()
    c.execute('SELECT * FROM users;')
    return c.fetchall()[::-1]

