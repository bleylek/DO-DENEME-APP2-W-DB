from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Models burada tanımlayalım (circular import'u önlemek için)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Uygulama başladığında tabloları oluştur
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for("index"))

    users = User.query.all()
    return render_template("index.html", users=users)

@app.route("/delete/<int:id>")
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
