
import requests
import hashlib
from bs4 import BeautifulSoup
import datetime
import CommonUtility,Utility
import Results
import pandas as pd
import mysql.connector
import os
import sys

DB_USER = CommonUtility.getParameterFromFile( 'DATABASE_USER' )
DB_PORT = CommonUtility.getParameterFromFile( 'DATABASE_PORT' )
DB_PWD = CommonUtility.getParameterFromFile( 'DATABASE_PWD' )
DB_SCHEMA = CommonUtility.getParameterFromFile( 'DATABASE_SCHEMA' )
ENV = CommonUtility.getParameterFromFile('ENV')
LEAGUES_LIST_PATH = os.path.dirname(os.getcwd())
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


mydb = mysql.connector.connect( user=DB_USER , password = DB_PWD , host = '127.0.0.1' , auth_plugin = 'mysql_native_password' )
mycursor = mydb.cursor()

Utility.telegram_bot_sendlog("START main_results.py")

now = datetime.datetime.now()
df_leagues = pd.read_csv(r'{}/Leagues.csv'.format(LEAGUES_LIST_PATH),sep=';',header=None)

for i in df_leagues.index:
    
    cl = df_leagues.values[i][0] + '/' + df_leagues.values[i][1]
    print(cl)
    
    page = requests.get("https://www.betexplorer.com/soccer/{}/results".format(cl), headers=HEADERS)
    page_content = BeautifulSoup(page.content, "html.parser")
    partite = str(page_content.findAll('td',attrs={"class":"h-text-left"})).encode("utf-8")
    md5_hash = hashlib.md5()
    md5_hash.update(partite)
    actual_hash = md5_hash.hexdigest()
    
    mycursor.execute("select hash \
                      from {}.hash_table \
                      where competition_cod = '{}'".format(DB_SCHEMA, df_leagues.values[i][2]))
    
    try:
        if( actual_hash != mycursor.fetchall()[0][0]):
        
            Results.execute(df_leagues.values[i][0],
                            df_leagues.values[i][1],
                            df_leagues.values[i][2],
                            df_leagues.values[i][3])
        
            mycursor.execute("REPLACE INTO {}.hash_table \
                              VALUES ('{}','{}')".format(DB_SCHEMA, df_leagues.values[i][2], actual_hash))
            mydb.commit()
    except:
        Results.execute(df_leagues.values[i][0],
                        df_leagues.values[i][1],
                        df_leagues.values[i][2],
                        df_leagues.values[i][3])
        
        mycursor.execute("REPLACE INTO {}.hash_table \
                          VALUES ('{}','{}')".format(DB_SCHEMA, df_leagues.values[i][2], actual_hash))
        mydb.commit()
        
    
    Utility.telegram_bot_sendlog("END Update Results {}".format(cl))
