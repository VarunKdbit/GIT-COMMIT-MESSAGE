# ⚡ AI Git Commit Generator

A lightweight full-stack web application that analyzes `git diff` output and automatically generates clean, professional Conventional Commit messages.

Built using **Flask (Python backend)** and a simple **HTML + CSS + JavaScript frontend**, this tool helps developers save time and maintain better commit history without relying on paid APIs or external AI services.

It intelligently detects added functions, classes, UI changes, documentation updates, and line changes to generate meaningful Conventional Commit messages automatically.

---

## 🚀 Features

- Paste raw `git diff` output
- Automatically detects:
  - Added functions
  - Added classes
  - HTML/UI changes
  - CSS changes
  - Documentation updates
  - Test file changes
  - Number of added lines
  - Number of removed lines
  - Number of files changed
- Generates professional Conventional Commit messages like:

```bash
feat: add UserService class

Changes: +45 -12 lines

. Shows quick project stats
. No API keys required
. Runs fully on localhost
. Fast, lightweight, and beginner-friendly

🛠 Tech Stack
Backend
Python
Flask
Regex (for diff analysis)
Frontend
HTML
CSS
JavaScript
Version Control Standard
Conventional Commits

📁 Project Structure

ai-git-commit-generator/
│
├── app.py                  # Flask backend logic
│
├── templates/
│   └── index.html          # Frontend UI
│
├── requirements.txt        # Python dependencies
│
└── README.md

⚙️ Installation & Setup

1. Clone the Repository
git clone https://github.com/yourusername/ai-git-commit-generator.git
cd ai-git-commit-generator

2. Create Virtual Environment (Optional but Recommended)
Windows :
python -m venv venv
venv\Scripts\activate

Mac/Linux :
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
python app.py
You will see:
🚀 Running at http://127.0.0.1:5000
Now open this URL in your browser.


💻 How to Use
Step 1
Run this command inside your project:
git diff
Copy the complete output

Step 2
Paste the git diff output into the textarea of the web app.

Step 3
Click on:
Generate Commit

Step 4
The system analyzes:

. Added functions
. Added classes
. File type changes
. UI updates
. Documentation updates
. Added and removed lines

Then it generates an automatic commit message like:
feat: add analyze_diff function

Changes: +28 -5 lines


🧠 How It Works :

The backend uses regex-based parsing to analyze git diff content.

It Detects:
Added Functions

Example:

+ def analyze_diff():
Added Classes

Example:

+ class UserService:
UI Changes

Detects:

.html
.htm
.jsx
.tsx
CSS Changes

Detects:

.css
.scss
Documentation Changes

Detects:

.md
.txt
Test File Changes

Detects files containing:

test
Code Statistics

Calculates:

Total files changed
Total added lines
Total removed lines
🧾 Commit Message Logic
Change Type	Generated Commit Type
Added Class	feat
Added Function	feat
HTML/UI Changes	style
Documentation Changes	docs
Other General Changes	fix

This follows the Conventional Commits Standard used in professional development workflows.

📌 Example
Input
+ def process_data():
+ class UserService:
Output
feat: add UserService class

Changes: +2 -0 lines
🔥 Future Improvements
GitHub Integration
VS Code Extension
Multiple Commit Suggestions
Copy Button for Commit Message
Improved UI Design
Dark / Light Theme Toggle
Deployment on Render / Railway
Docker Support
Branch-aware Commit Suggestions
AI-powered Smarter Commit Classification
👨‍💻 Author

Built for developers who want faster, cleaner, and more professional Git commits.

Designed especially for students, beginners, and developers who want to maintain better GitHub repositories without depending on paid AI APIs.

Made with ❤️ using Flask + Python

⭐ Support

If you like this project, give it a star on GitHub.

It helps a lot and motivates future improvements.