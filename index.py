from flask import Flask, render_template

app= Flask (__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/miguel")
def miguel():
    return render_template("miguel.html")

if __name__=="__main__":
    app.run(debug=True)