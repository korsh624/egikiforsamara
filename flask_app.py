from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/plice")
def plice():
    return render_template('item.html')


if __name__=="__main__":
    app.run(debug=True)