from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)
DATA_FILE = "todos.json"

def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f)

@app.route("/")
def index():
    todos = load_todos()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("task", "").strip()
    if text:
        todos = load_todos()
        todos.append({"id": len(todos) + 1, "task": text, "done": False})
        save_todos(todos)
    return redirect(url_for("index"))

@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = not t["done"]
    save_todos(todos)
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todos = [t for t in load_todos() if t["id"] != todo_id]
    save_todos(todos)
    return redirect(url_for("index"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
