from flask import render_template, session
from app import app

@app.route("/customer_landingpage")
def customer_landingpage():
    fullname = session.get("fullname", "Guest")
    return render_template("customer/customer_landingpage.html", username=fullname)

@app.route("/customer_aboutpage")
def customer_aboutpage():
    fullname = session.get("fullname", "Guest")
    return render_template("customer/customer_aboutpage.html", username=fullname)

@app.route("/customer_howitworks")
def customer_howitworks():
    fullname=session.get("fullname", "Guest")
    return render_template("customer/customer_howitworks.html", username=fullname)
