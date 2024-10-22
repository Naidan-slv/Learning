from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    
    mylist = [10,20,30,40,50]
    return render_template('index.html', mylist=mylist)
    # we can dynamically change this html file
    # pass the value of myvalue and myresult to the html file

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
