from flask import Flask
from flask import render_template
from flask import request
import sqlite3
app = Flask(__name__)


#con = sqlite3.connect("employee.db")
#print("Database opened successfuly")
#con.execute("create table Employees (id INTEGER PRIMERY KEY, name TEXT NOT NULL, email TEXT NOT NULL, address TEXT NOT NULL)")
#print("Table created successfuly")

#@app.route("/")
#def index():
#	con = sqlite3.connect("employee.db")
#	con.row_factory = sqlite3.Row
#	cur = con.cursor()
#	cur.execute("WITH CTE1 (F1) AS(SELECT SUM(q11.Index_proc) FROM Climate q11 ),CTE2 (F2) AS(SELECT SUM(q22.Index_proc) FROM Climate q22)SELECT(F1/F2) AS REZ FROM CTE1,CTE2")
#	rows = cur.fetchall()
#	return render_template("index.html", rows=rows)

@app.route("/")
def index():
	con = sqlite3.connect("employee.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("WITH CTE1 AS(SELECT * FROM Territory q1),CTE2 AS(SELECT * FROM Climate q2),CTE3 AS(SELECT * FROM Gas q3),CTE4 AS(SELECT * FROM Product q4),CTE5 AS(SELECT * FROM Revenue q5)select q11.RF AS RF,SUM(q55.index_revenue*q44.name_product/q33.index_proc/q22.Index_proc) AS REZ from CTE1 q11 INNER JOIN CTE2 q22 ON q22.id_climate=q11.id_climate INNER JOIN CTE3 q33 ON q33.id_gas=q11.id_gas INNER JOIN CTE4 q44 ON q44.id_product=q11.id_product INNER JOIN CTE5 q55 ON q55.id_revenue=q11.id_revenue group by q11.RF")
	rows = cur.fetchall()
	return render_template("index.html", rows=rows)


if __name__ == '__main__':
	app.run(debug=True)