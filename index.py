import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('system.gen.noreply@gmail.com','apsj#12345678')
message="\nHello Testing SMTP from Python"
s.sendmail("noreply@apsjorhat.org","prabhat@apsjorhat.org",message)
s.quit()
