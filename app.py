from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        expression = request.form['expression']
        operation = request.form['operation']

        if operation == 'add':
            result = eval(expression)  # For simplicity, using eval, but be cautious in real projects

        elif operation == 'subtract':
            result = eval(expression)

        elif operation == 'multiply':
            result = eval(expression)

        elif operation == 'divide':
            result = eval(expression)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)