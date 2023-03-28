from flask import Flask, render_template

app = Flask(__name__) # create an instance of the Flask class


@app.route('/home')
def home():
    return 'This is my home page'

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
