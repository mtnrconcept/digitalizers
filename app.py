from flask import Flask, render_template
from mail_reader import get_emails
from llm import classify_email

app = Flask(__name__)

@app.route("/")
def index():
    raw_emails = get_emails(limit=10)
    classified = []
    for email in raw_emails:
        category = classify_email(email["text"][:1000])  # on tronque si trop long
        email["category"] = category
        classified.append(email)
    
    return render_template("index.html", emails=classified)
    
if __name__ == "__main__":
    app.run(debug=True)
