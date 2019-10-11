from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='Loan Payment Calculator')

@app.route('/calculate', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
        form = request.form
        A = int(form['A'])
        n = int(form['nperiod']) * int(form['nyears'])
        i = int(form['i']) / int(form['nperiod'])
        D =  ((( 1 + i ) ^n ) - 1 ) / ( i ( 1+ i) ^n)
        P = A/D
        return render_template('index.html', display=P, Discount=D, pageTitle='Loan Payment Calculator')

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)