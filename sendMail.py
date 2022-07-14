import os 
import smtplib #import the library

py_mail = os.environ.get("PY_MAIL")
py_pass = os.environ.get("PY_PASS")

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:   #context manager to close connection automatically
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(py_mail, py_pass)

    subject = input("Please enter the subject: ")
    body = input("Please enter the mail body: ")

    msg = f'Subject:{subject}\n\n{body}'   #Subject on top, body on bottom

    smtp.sendmail(py_mail,"pynebster@gmail.com",msg) #smtp.sendmail(SENDER, RECEIVER, msg)

