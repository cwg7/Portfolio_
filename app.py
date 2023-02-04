from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume")
def resume():
    try:
        return send_file("C:\\Users\\cwins\Documents\\resumeWebPage\\cwgResume2023.pdf", as_attachment=True)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run()