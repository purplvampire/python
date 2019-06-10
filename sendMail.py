import smtplib
# Load Password from pwd.txt
pwd = []
with open('pwd.txt', 'r') as f:
    for word in f:
        pwd.append(word)
# Create a SMTP Object.
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# Test Server Echo
x = smtpObj.ehlo()
print(x)
# Build TLS session
x = smtpObj.starttls()
print(x)
# Login by account
x = smtpObj.login('purplvampire@gmail.com', pwd[0])
print(x)
# Send an test mail, Subject and Content must seperate by \n.
src = 'purplvampire@gmail.com'
desc = 'purplvampire@yahoo.com.tw'
content = 'Subject: Test.\nTest'
x = smtpObj.sendmail(src, desc, content)
print(x)
# Quit Service
smtpObj.quit()