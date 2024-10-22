from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
import io
import webbrowser 
from googlesearch import search
# تنظیم خروجی به UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
class Media():
  def __init__(self,sender) :
    self.emailSender=sender
    # self.sender= smtplib.SMTP("smtp.gmail.com",587)
    # self.sender.starttls()
    # self.sender.login(self.emailSender,"yoluwpnorfeoirzh")
  
  def searchGoogle(self,searchQuery):
    for j in search(searchQuery, tld="co.in", num=10, stop=10, pause=2):
     print(j)
     webbrowser.open(j)
  
  def a(self):
   print("parsa")
   
  def sendEmail(self,emailAddress,data):
    self.sender.sendmail(self.emailSender,emailAddress,data)
    self.sender.close()
  
  def sendEmailpro(self, subject,rec,text,data):
   msg = MIMEMultipart() 
   msg['From'] = self.emailSender
   msg['To'] = rec
   msg['Subject'] = subject

# محتوای HTML ایمیل
   html_content = """
  <!DOCTYPE html>
  <html lang="fa">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: red;
            margin: 0;
            padding: 20px;
        }
        .container {
            background-color: blue;
          
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        p {
            color: #555;
        }
    </style>
  </head>
  <body>
    <div class="container">
        <h1>سلام!</h1>
        <p>این یک ایمیل HTML با CSS است.</p>
    </div>
  </body>
  </html>
  """

# اضافه کردن محتوای HTML به پیام
   msg.attach(MIMEText(html_content, 'html'))

# ارسال ایمیل
   try:  
     self.sender.send_message(msg)
     print("ایمیل با موفقیت ارسال شد.")
   except Exception as e:
    print(f"خطا در ارسال ایمیل: {e}")
  

    
 
 
# s=Media("psagharzadeh@gmail.com")
# data="<!DOCTYPE html><html><body><h2>HTML Images</h2><p>HTML images are defined with the img tag:</p><img src='w3schools.jpg' alt='W3Schools.com' width='104' height='142'></body></html>"
# text="salam khobi as hal delet bego"
# s.sendEmailpro("alaki","psagharzadeh@gmail.com",text,data)
# s.searchGoogle("find best job in mschine learning ")
# s["a"]()

