from flask import Flask, request
from flask import make_response
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    response = make_response()
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream'

    return response

@app.route('/get_put', methods=['POST','GET'])
def get_put():
    #("Using curl -X GET http:// we can get this message")
    # you need to run flask in one terminal and then in another use the command
    if request.method == 'POST':
        return 'You are using POST\n'
    else:
        return 'You are using GET\n'

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}!"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"The sum is {num1 + num2}"

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}!'
    else:
        return 'You did not provide the correct parameters'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# GET - When you want to get information
# POST - When you want to send information
# PUT - When you want to update information
