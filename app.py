from flask import Flask, render_template, request, redirect, session, jsonify
from db import collection, alerts_collection

app = Flask(__name__)
app.secret_key = "secret123"

# 🔐 Dummy users (later MongoDB me bhi rakh sakti ho)
users = {
    "user@gmail.com": "1234",
    "admin@gmail.com": "admin"
}

# 🔐 LOGIN
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if users.get(email) == password:
            session["user"] = email
            return redirect("/")
    
    return render_template("login.html")

# 🔐 LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

# 🏠 HOME (PROTECTED)
@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")

    data = list(collection.find().sort("_id", -1).limit(10))
    data.reverse()

    alerts = list(alerts_collection.find().sort("_id", -1).limit(5))

    return render_template("index.html", data=data, alerts=alerts)

# 📊 API
@app.route("/data")
def data_api():
    data = list(collection.find().sort("_id", -1).limit(10))
    data.reverse()

    return jsonify({
        "cpu": [d["cpu"] for d in data],
        "memory": [d["memory"] for d in data],
        "labels": [d["time"] for d in data]
    })

app.run(host="0.0.0.0", port=5000, debug=True)


