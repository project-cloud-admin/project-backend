'''FlaskApp'''
from flask import Flask, request, render_template, escape

app = Flask(__name__)
'''
endpoint
'''
@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"
@app.route('/hello', methods=['POST', 'GET'])
def hello():
    '''get'''
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {escape(name)}'
    return render_template('form.html')

if __name__ == "__main__":
    app.run()
    
