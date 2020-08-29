from flask import Flask, render_template, request, redirect, url_for, session

calc = Flask('__name__')
calc.secret_key = '123'


@calc.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == 'GET':
        return render_template('indexcalc.html')
    else:
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operation == 'add':
            r = num1 + num2
            result = str(r)
        elif operation == 'subtract':
            r = num1 - num2
            result = str(r)
        elif operation == 'multiply':
            r = num1 * num2
            result = str(r)
        elif operation == 'division':
            r = num1 / num2
            result = str(r)
        else:
            return redirect(url_for('homepage'))
        session['result'] = result
        return redirect(url_for('results'))


@calc.route('/results/', methods=['GET'])
def results():
    result = session['result']
    return render_template('resultcalc.html', x=result)


if __name__ == '__main__':
    calc.run(debug=True)
