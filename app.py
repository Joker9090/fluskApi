from flask import Flask
from flask_mysqldb import MySQL
import psutil
import json

#print(dir(psutil))

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

mysql = MySQL(app)

@app.route('/')
def hello():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM exchange_symbols")
    result = cur.fetchall()
    items = []
    for row in result:
        items.append({ 'id': row[0], 'internalSymbol': row[4] })
    cur.close()
    return json.dumps({ 'items': items })

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
