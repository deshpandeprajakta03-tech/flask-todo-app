# 📝 Flask To-Do App

A simple, clean To-Do web app built with Python + Flask. Ready to run locally in VS Code, push to GitHub, and deploy on Azure.

---

## 📁 Project Structure

```
flask-todo-app/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Procfile                # For Azure/Gunicorn deployment
├── .gitignore
├── templates/
│   └── index.html          # UI template
├── static/
│   └── style.css           # Styling
└── .github/
    └── workflows/
        └── azure-deploy.yml  # Auto-deploy to Azure on git push
```

---

## 🚀 Run Locally (VS Code)

### 1. Open in VS Code
```bash
cd flask-todo-app
code .
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

Open your browser at: **http://localhost:5000**

---

## 🐙 Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Flask To-Do App"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

---

## ☁️ Deploy on Azure

### Option A — Azure Portal (easiest first time)

1. Go to [portal.azure.com](https://portal.azure.com)
2. Create a **Web App** → choose Python 3.11 → Linux
3. In **Deployment Center** → choose GitHub → authorize → select your repo + `main` branch
4. Azure auto-generates the workflow and deploys on every push ✅

### Option B — GitHub Actions (already configured)

1. In Azure Portal → your Web App → **Get Publish Profile** → download the `.PublishSettings` file
2. In your GitHub repo → **Settings → Secrets → Actions** → add:
   - `AZURE_WEBAPP_NAME` → your Azure app name (e.g. `my-todo-app`)
   - `AZURE_PUBLISH_PROFILE` → paste the full contents of the `.PublishSettings` file
3. Push to `main` — GitHub Actions deploys automatically 🚀

---

## ✅ Features
- Add tasks
- Mark tasks as done / undo
- Delete tasks
- Task counter (X / Y completed)
- Data stored in `todos.json` (no database needed)
