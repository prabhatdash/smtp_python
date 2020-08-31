import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('noreply@apsjorhat.org','noreply@12345')
message="Hello Testing SMTP from Python"
s.sendmail("noreply@apsjorhat.org","prabhat@apsjorhat.org",message)
s.quit()