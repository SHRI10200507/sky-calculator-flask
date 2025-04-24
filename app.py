from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/skycalculator', methods=['GET', 'POST'])
def sky_calculator():
    result = None
    expression = ''
    if request.method == 'POST':
        expression = request.form['expression']
        try:
            result = eval(expression)
        except ZeroDivisionError:
            result = "Error: Division by zero"
        except Exception:
            result = "Invalid Expression"
    return render_template('index.html', result=result, expression=expression)

@app.route('/', methods=['GET'])
def index():
    # You can keep this as a default landing page if you want,
    # or you can remove it if 'skycalculator' is your main entry point.
    return "Welcome to the Sky!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)