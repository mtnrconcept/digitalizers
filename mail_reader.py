from imap_tools import MailBox
import os
from dotenv import load_dotenv

load_dotenv()

def get_emails(limit=10):
    emails = []
    with MailBox(os.getenv("IMAP_HOST")).login(os.getenv("IMAP_USER"), os.getenv("IMAP_PASSWORD")) as mailbox:
        for msg in mailbox.fetch(limit=limit, reverse=True):
            emails.append({
                "from": msg.from_,
                "subject": msg.subject,
                "text": msg.text or msg.html or "",
                "date": msg.date
            })
    return emails
