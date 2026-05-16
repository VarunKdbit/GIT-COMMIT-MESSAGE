from flask import Flask, jsonify, render_template, request
import re
import os

app = Flask(__name__)


# ---------------- DIFF ANALYZER ---------------- #

def analyze_diff(diff_text):
    analysis = {
        "added_functions": [],
        "added_classes": [],
        "removed_functions": [],
        "html_changes": False,
        "css_changes": False,
        "test_changes": False,
        "config_changes": False,
        "doc_changes": False,
        "added_lines": 0,
        "removed_lines": 0,
        "files_changed": [],
    }

    current_file = ""
    for line in diff_text.splitlines():

        # detect files
        if line.startswith("diff --git"):
            match = re.search(r"b/(.+)$", line)
            if match:
                current_file = match.group(1)
                analysis["files_changed"].append(current_file)

                ext = os.path.splitext(current_file)[1].lower()
                if ext in (".html", ".htm", ".jsx", ".tsx"):
                    analysis["html_changes"] = True
                if ext in (".css", ".scss"):
                    analysis["css_changes"] = True
                if "test" in current_file.lower():
                    analysis["test_changes"] = True
                if ext in (".md", ".txt"):
                    analysis["doc_changes"] = True

        elif line.startswith("+") and not line.startswith("+++"):
            analysis["added_lines"] += 1
            content = line[1:].strip()

            fn_match = re.match(r"(def |function |const )(\w+)", content)
            if fn_match:
                analysis["added_functions"].append(fn_match.group(2))

            cls_match = re.match(r"(class )(\w+)", content)
            if cls_match:
                analysis["added_classes"].append(cls_match.group(2))

        elif line.startswith("-") and not line.startswith("---"):
            analysis["removed_lines"] += 1

    return analysis


# ---------------- COMMIT GENERATOR ---------------- #

def generate_commit_message(analysis):
    added_fns = list(set(analysis["added_functions"]))[:3]
    added_cls = list(set(analysis["added_classes"]))[:2]

    if added_cls:
        subject = f"add {' & '.join(added_cls)} class"
        commit_type = "feat"
    elif added_fns:
        subject = f"add {' & '.join(added_fns)} function"
        commit_type = "feat"
    elif analysis["html_changes"]:
        subject = "update UI layout"
        commit_type = "style"
    elif analysis["doc_changes"]:
        subject = "update documentation"
        commit_type = "docs"
    else:
        subject = "update codebase"
        commit_type = "fix"

    header = f"{commit_type}: {subject}"
    body = f"\n\nChanges: +{analysis['added_lines']} -{analysis['removed_lines']} lines"

    return header + body


# ---------------- ROUTES ---------------- #

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-commit", methods=["POST"])
def generate_commit():
    data = request.get_json()
    diff = data.get("diff", "").strip()

    if not diff:
        return jsonify({"success": False, "error": "No diff provided."})

    analysis = analyze_diff(diff)
    message = generate_commit_message(analysis)

    return jsonify({
        "success": True,
        "message": message,
        "diff_preview": "\n".join(diff.splitlines()[:40]),
        "stats": {
            "files_changed": len(analysis["files_changed"]),
            "added_lines": analysis["added_lines"],
            "removed_lines": analysis["removed_lines"],
            "functions_added": len(analysis["added_functions"]),
            "classes_added": len(analysis["added_classes"]),
        }
    })


if __name__ == "__main__":
    print("🚀 Running at http://127.0.0.1:5000")
    app.run(debug=True)