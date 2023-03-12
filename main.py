import smtplib
from email.mime.text import MIMEText

with open('email.txt', 'r') as f:
    emails = f.read().splitlines()

subject = '¡Hi! Check my new Stealer.'

msg = MIMEText('Buy Prysmax FUD Stealer cheapp!!! @Lawxsz.')

msg['Subject'] = subject
msg['From'] = 'yo@gmail.com'
msg['To'] = ', '.join(emails)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('yo@gmail.com', 'amazinpassword123') # u password here
server.sendmail('yo@gmail.com', emails, msg.as_string())
server.quit()
