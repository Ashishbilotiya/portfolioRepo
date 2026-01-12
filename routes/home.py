
from flask import render_template,Blueprint, request, redirect, url_for, flash
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
import os
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv

load_dotenv()

home_page = Blueprint("home",__name__)

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
GOOGLE_REFRESH_TOKEN = os.getenv("GOOGLE_REFRESH_TOKEN")



def get_gmail_service():
    creds = Credentials(
        token=None,
        refresh_token=GOOGLE_REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        scopes=["https://www.googleapis.com/auth/gmail.send"]
    )
    return build("gmail", "v1", credentials=creds)




def send_email(name, email, message):
    service = get_gmail_service()

    body = f"""
    Name: {name}
    Email: {email}

    Message:
    {message}
    """

    msg = MIMEText(body)
    msg["to"] = EMAIL_RECEIVER
    msg["subject"] = "New Portfolio Contact Message"

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    service.users().messages().send(
        userId="me",
        body={"raw": raw}
    ).execute()



@home_page.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        name = str(request.form.get("name"))
        email = str(request.form.get("email"))
        message = str(request.form.get("message"))
        if name and email and message:
            try:
                send_email(name, email, message)
                flash("Message sent successfully! I will contact you soon.", "success")
            except Exception as e:
                print(e)
                flash("Error! Message could not be sent.", "danger")
            return  redirect(url_for("home.home",_anchor="contact"))
    return render_template("home/home.html")


