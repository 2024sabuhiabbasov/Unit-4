from flask import Flask, render_template, request

app = Flask(__name__) # create an instance of the Flask class


@app.route('/home')
def home():
    return 'This is my home page'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/requests_example', methods=["GET", "POST"])
def requests_example():
    result = ""
    result2 = ""
    if request.method == "GET":
        # currency converter
        usd_value = request.args.get("usd_value")
        if usd_value:
            jpy = int(usd_value)*132.615294
            result = f"{usd_value} USD is {jpy:.2f} JPY"
    elif request.method == "POST":
        # password checker
        check_pass = request.form["check_pass"]
        if check_pass:
            if len(check_pass) > 8:
                result2 = "Strong password"
            else:
                result2 = "Unsafe password"
    return render_template('requests_example.html', data=result, data2=result2)

if __name__ == '__main__':
    app.run()
