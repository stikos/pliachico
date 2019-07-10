import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def notify(data=None):
    # get fb account creds
    if os.environ["PATH"].startswith("/home/konstantinos/"):
        import configparser
        local_config = configparser.ConfigParser()
        local_config.read('data.ini')
        email = local_config["CREDS"]["email"]
        passwrd = local_config["CREDS"]["pass"]
    else:
        email = os.environ["email"]
        passwrd = os.environ["pass"]

    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    # TODO: Add receivers
    receiver_email = ["liosis_c@hotmail.com"]

    message = MIMEMultipart("alternative")
    message["Subject"] = "Hot Tips Incoming"
    message["From"] = email
    message["To"] = ';'.join(receiver_email).strip(';')

    html = """\
        <html>
          <body>
            <p>Μαζί,<br>
               Θα φέρουμε τη βροχή<br>
               <img src="https://www.aiobot.com/wp-content/uploads/2018/12/money-with-sneaker-bot.png" alt="Pliachico" 
                    height="100" width="100"></img><br> 
               Πλιάτσικας
            </p>
          </body>
        </html>
        """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(html, "html")

    message.attach(part1)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email, passwrd)
        for addr in receiver_email:
            server.sendmail(email, addr, message.as_string())
