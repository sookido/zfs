import smtplib, ssl, sys
from email.mime.text import MIMEText

gmail_account = "{MAIL}@gmail.com"
gmail_password = "{PASSWORD"
mail_to = "{TOMAIL}"

subject = "zfs error"
body = sys.stdin.read()

msg = MIMEText(body, "html")
msg["Subject"] = subject
msg["To"] = mail_to
msg["From"] = gmail_account

server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
    context=ssl.create_default_context())
server.login(gmail_account, gmail_password)
server.send_message(msg)
