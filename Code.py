import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import serial
import time
import os.path

ser = serial.Serial('COM17', 9600)
time.sleep(2)
P=0


while True:
    b = (ser.readline().strip())         # read a byte string
    string_n = b.decode('utf-8')  # decode byte string into Unicode  
    #string = string_n.rstrip() # remove \n and \r
    I = float(string_n)# convert string to float
    p=I*230
    P=P+p
    print(P)
    if (P>=500):
        f= open("bill.txt","w+")
        f.write("This is your bill %d\r\n" % P)
        f.close()
        P=0
        email = 'dsith384@gmail.com'
        password = '8460307190'
        send_to_email = 'meet1536@gmail.com'
        subject = 'This is your Electricity Bill' # The subject line
        message = 'bil'
        file_location = 'C:\\Users\\meet1\\OneDrive\\Desktop\\viren\\bill.txt' 

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

 # Attach the message to the MIMEMultipart object
        msg.attach(MIMEText(message, 'plain'))

        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Attach the attachment to the MIMEMultipart object
        msg.attach(part)



        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
        server.sendmail(email, send_to_email, text)
        server.quit()

        print("viren")

    # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()



    
    
