




from flask import *
app=Flask(__name__)

@app.route('/')
def Rasool():
    return 'hello rasool'

@app.route('/about')
def about():
    return 'this is the about of my website'

@app.route('/total')
def total():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)