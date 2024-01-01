import smtplib
from email.message import EmailMessage

server = smtplib.SMTP("smtp.gmail.com" , 587)
server.starttls()

server.login("tekulapellil2003@gmail.com" , "Sridurga@132003")

msg = EmailMessage()
msg["Form"] = "tekulapellil2003@gmail.com"
msg["To"] = "keerthivardhantekulapelli@gmail.com"
msg["Subject"] = "test mail"
msg.set_content("this is trial mail")

server.send_message(msg)

server.quit()
