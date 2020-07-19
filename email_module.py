# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Import the pathlib to read the html file and read text from it
from pathlib import Path

# Imported it for reading the varibales with $sysmbol subtutite it with variable
from string import Template

message = Template(Path('message.html').read_text())

email = EmailMessage()

email['from'] = 'ddsprasad@gmail.com'
email['to'] = 'ddunga@getdiwo.com'
email['subject'] = 'This is the testing email!'

# email.set_content('I am sending you Test email from my Python Job  \n Thank you!.')
email.set_content(message.substitute({'name': 'ddsprasad'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ddsprasad@gmail.com', 'Orange@99')
    smtp.send_message(email)
    print("Eveything Worked!")
