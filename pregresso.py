import smtplib
import CommonUtility
import mysql.connector
import os
import sys
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


DB_USER = CommonUtility.getParameterFromFile( 'DATABASE_USER' )
DB_PORT = CommonUtility.getParameterFromFile( 'DATABASE_PORT' )
DB_PWD = CommonUtility.getParameterFromFile( 'DATABASE_PWD' )
DB_SCHEMA = CommonUtility.getParameterFromFile( 'DATABASE_SCHEMA' )
LEAGUES_LIST_PATH = os.path.dirname(os.getcwd())

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'raspbotbet@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'monzascommesse888'  #change this to match your gmail password
 
class Emailer:
    def sendmail(self, recipient, subject):
          
        emailData = MIMEMultipart()
        emailData['Subject'] = subject
        emailData['To'] = ", ".join(recipient)
        emailData['From'] = GMAIL_USERNAME
        
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("/home/alessio9567/metodo_results.csv", "rb").read())  
        part.add_header('Content-Disposition', 'attachment; filename="metodo_results_pregresso.csv"')

        emailData.attach(part)
      
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
  
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
  
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, emailData.as_string())
        session.quit
  
sender = Emailer()

mydb = mysql.connector.connect( user=DB_USER , password = DB_PWD , host = '127.0.0.1' , auth_plugin = 'mysql_native_password' )
mycursor = mydb.cursor()

mycursor.execute("select b.home_team, \
                         b.away_team, \
                         b.home_odd, \
                         b.draw_odd, \
                         b.away_odd, \
                         b.match_date, \
                         '' as tip,\
                         b.competition_cod,\
                         b.home_goals,\
                         b.away_goals,\
                         '' as last_lost_home,\
                         '' as last_diff_goals,\
                         '' as last_lost_odd,\
                         '' as last_competition_cod,\
                         b.match_cod \
                  from db_test.next_metodo a \
                  join db_dev.latest_results b \
                  on a.match_cod=b.match_cod")

results49 = mycursor.fetchall()
fp = open('/home/alessio9567/metodo_results_pregresso.csv', 'w')
attach_file = csv.writer(fp)
attach_file.writerows(results49)
fp.close()
#
#
sendTo = [ 'sacchinit@gmail.com', 'alessio.iannini@gmail.com']
emailSubject = "Alcuni risultati pregressi del bot"
# 
sender.sendmail(sendTo, emailSubject)  
###
##
