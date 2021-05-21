from flask import Flask, render_template

app = Flask(__name__)
if __name__=="__main__":
    app.run(debug=True , port=5010)
@app.route(:
    return "/")
def index()render_template("index.html")
