# ⚡ GitMessage — AI Commit Generator

A full-stack web app that generates professional Conventional Commit messages from your `git diff` using Claude AI.

---

## Project Structure

```
git-commit-generator/
├── backend/
│   └── app.py          # Flask API server
├── frontend/
│   └── index.html      # Single-file UI (served by Flask)
├── requirements.txt
└── README.md
```

---

## Setup & Run

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the server

```bash
cd backend
python app.py
```

The app runs at **http://localhost:5000**

### 3. Use the app

1. Open http://localhost:5000 in your browser
2. Enter your **Anthropic API key** (`sk-ant-…`)
3. Paste the output of `git diff --staged` or `git diff HEAD`
4. Click **Generate Commit Message**

---

## API Endpoints

| Method | Endpoint        | Description                         |
|--------|-----------------|-------------------------------------|
| GET    | `/`             | Serves the frontend                 |
| POST   | `/api/generate` | Generate commit from diff           |
| GET    | `/api/types`    | List supported commit types         |
| GET    | `/api/health`   | Health check                        |

### POST `/api/generate`

**Request body:**
```json
{
  "api_key": "sk-ant-…",
  "diff": "diff --git a/…"
}
```

**Response:**
```json
{
  "success": true,
  "commit": {
    "raw": "feat: add user authentication with bcrypt\n\n- Replace plain-text password storage with bcrypt hashing\n- Add login attempt logging",
    "title": "feat: add user authentication with bcrypt",
    "type": "feat",
    "body": "",
    "bullets": [
      "Replace plain-text password storage with bcrypt hashing",
      "Add login attempt logging"
    ]
  }
}
```

---

## Conventional Commit Types

| Type       | When to use                        |
|------------|------------------------------------|
| `feat`     | New feature                        |
| `fix`      | Bug fix                            |
| `docs`     | Documentation changes              |
| `style`    | Formatting, no logic change        |
| `refactor` | Code restructuring, no behavior Δ  |
| `perf`     | Performance improvement            |
| `test`     | Tests added or modified            |
| `chore`    | Maintenance / config / deps        |

---

## Getting an Anthropic API Key

1. Sign up at [console.anthropic.com](https://console.anthropic.com)
2. Go to **API Keys** → **Create Key**
3. Copy the key (starts with `sk-ant-`)

---

## Custom Port

```bash
PORT=8080 python app.py
```
