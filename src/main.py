from flask import Flask
from src.addingform import adding

app = Flask(__name__)
app.register_blueprint(adding)

@app.route('/')
def status():
    status = {'status' : 200}
    return status

#if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=5000)

