import imghdr
import smtplib
from email.message import EmailMessage

PASSWORD = "********"
SENDER = "sztymperjan@gmail.com"
RECEIVER = "sztymperjan@gmail.com"


def send_email(image_path):
	print("send_email function started")
	email_message = EmailMessage()
	email_message["Subject"] = "Opryszek Detected"
	email_message.set_content("Hey, opryszek has been detected close to your computer!!!")

	with open(image_path, "rb") as file:
		content = file.read()

	email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

	gmail = smtplib.SMTP("smtp.gmail.com", 587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(SENDER, PASSWORD)
	gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
	gmail.quit()
	print("send_email function ended")
