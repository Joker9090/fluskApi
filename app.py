from flask import Flask
import psutil
import json
#print(dir(psutil))

app = Flask(__name__)

@app.route('/')
def hello():
    return json.dumps({ 'cpu_stats': psutil.cpu_stats()})

if __name__ == '__main__':
    app.run()
