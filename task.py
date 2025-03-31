from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Task Model
class Task(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)  # Fixed completed column

# Create Database
with app.app_context():
    db.create_all()

# Home Route - Show All Tasks
@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)  # Fixed indentation

# Add Task Route
@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    if title: 
        new_task = Task(title=title)  # Fixed variable name
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("index"))  # Fixed indentation

# Mark Task as Completed
@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = not task.completed  # Toggle completed status
        db.session.commit()
    return redirect(url_for("index"))  # Fixed indentation

# Delete Task Route
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get(task_id)  # Fixed incorrect query
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("index"))  # Fixed indentation

if __name__ == "__main__":
    app.run(debug=True)
