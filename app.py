from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World! :)<h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name="Lachlan Arboit"):
    return f"<h1>Hello {name}<h1>"


@app.route('/f-c/<fahrenheit>')
def conv_fahrenheit_to_celsius(fahrenheit=32.0):
    """Convert Fahrenheit to Celsius."""
    return f"<h2>F: {fahrenheit}° C: {5 / 9 * (float(fahrenheit) - 32)}°</h2>"


@app.route('/c-f/<celsius>')
def conv_celsius_to_fahrenheit(celsius=0.0):
    """Convert Celsius to Fahrenheit."""
    return f"<h2>C: {celsius}° F: {float(celsius) * 9.0 / 5 + 32}°</h2>"


if __name__ == '__main__':
    app.run()
