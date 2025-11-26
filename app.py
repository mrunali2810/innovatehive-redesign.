from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    # TODO: In real app, save to DB or send email
    print(f"[CONTACT] {name} <{email}>: {message}")

    return jsonify({"status": "success", "message": "Thanks for reaching out! We will get back to you soon."}), 200

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
