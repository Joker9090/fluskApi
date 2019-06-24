from flask import Flask
import psutil
import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
print(data)

#print(dir(psutil))

app = Flask(__name__)

from controllers import helloController
app.register_blueprint(helloController.bp)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
