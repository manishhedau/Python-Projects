# Email sender program 

# To send the email our email system is not allow to use less secure app for sending email
# so run the program you need to allow 'less secure app access' in your gmail 
import smtplib

To = input('Enter the Email of recipent : \n')

content = input('Enter the content : \n')
    
def sendEmail(To,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('hedaumanish@gmail.com','redmi@4x')
    server.sendmail('hedaumanish@gmail.com',To,content)