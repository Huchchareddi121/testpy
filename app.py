from flask import Flask
app = Flask(__name__)
@app.route('/docker')
def docker():
    return {'result':'True','response':'application is running continuouly'}


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug = True)
