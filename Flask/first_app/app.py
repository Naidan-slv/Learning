from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    
    mylist = [10,20,30,40,50]
    return render_template('index.html', mylist=mylist)
    # we can dynamically change this html file
    # pass the value of myvalue and myresult to the html file

@app.route('/other')
def other():
    some_text = "Hello World"
    return render_template('other.html',some_text=some_text)


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, n):
    return s * n

#This is a redirect endpoint, it will redirect to the other endpoint which is other in this case 
@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
