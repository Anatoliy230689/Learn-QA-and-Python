import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
print(type(smtpObj))
smtpObj.login('maklabas23@gmail.com', '12345Qqq.')

smtpObj.sendmail('maklabas23@gmail.com','anatoliy.babiy1@gmail.com', 'Test email' )
smtpObj.quit()
