from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def result():
    input_url = request.args.get("input-url")
    username = request.args.get("username")
    avatar_url = request.args.get("avatar-url")
    content = request.args.get("content")

    final_msg = {
        'username': username,
        'avatar_url': avatar_url,
        'content': content
    }

    try:
        r = requests.post(input_url, data=final_msg)
        if r.ok:
            return render_template("success.html")
        else:
            return render_template("failed.html")
    except:
        return render_template("failed.html")

if __name__ == "__main__":
    app.run(debug=True, port=5003)