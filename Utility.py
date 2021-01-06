
import requests
import mysql.connector
import CommonUtility

DB_USER = CommonUtility.getParameterFromFile( 'DATABASE_USER' )
DB_PORT = CommonUtility.getParameterFromFile('DATABASE_PORT')
DB_PWD = CommonUtility.getParameterFromFile('DATABASE_PWD')
DB_SCHEMA = CommonUtility.getParameterFromFile('DATABASE_SCHEMA')
ENV = CommonUtility.getParameterFromFile('ENV')

mydb = mysql.connector.connect(user=DB_USER, password=DB_PWD, host='127.0.0.1', auth_plugin='mysql_native_password' )
mycursor = mydb.cursor()


def build_bot_message( method_match, tip , prod ):

    bot_message_next_match= "\n \
\U0001F4C5 {} \U0000231A {} \n \
\n \
{} \n \
\n \
\U000026BD {}-{} \n \
\n \
\U0001F3B2 @{} @{} @{} \n  \
\n \
\U0001F449 PRONO: {} ".format(str(method_match[5]).split(' ')[0][8:10]+'/'+str(method_match[5]).split(' ')[0][5:7]+'/'+str(method_match[5]).split(' ')[0][:4],
                              str(method_match[5]).split(' ')[1][:5],
                              decode_emoji(method_match[6]),
                              method_match[0],method_match[1],method_match[2],method_match[3],method_match[4],tip)
    
    if(prod == 1):
        telegram_bot_sendtext( bot_message_next_match )
    else:
        telegram_bot_sendlog( bot_message_next_match )

def telegram_bot_sendtext( bot_message ):

    BOT_TOKEN = CommonUtility.getParameterFromFile('BOT_TOKEN')
    BOT_CHATID = str(CommonUtility.getParameterFromFile('BOT_CHATID'))

    send_text = 'https://api.telegram.org/bot' + \
                                     BOT_TOKEN + \
                       '/sendMessage?chat_id=' + \
                                    BOT_CHATID + \
                  '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)


def telegram_bot_sendlog( bot_message ):

    BOT_TOKEN = '1310003274:AAE6FmLQVlYWrerylGfrxN1CRhhQYekjLX4'
    BOT_CHATID = '-1001215704490'

    send_text = 'https://api.telegram.org/bot' + \
                                     BOT_TOKEN + \
                       '/sendMessage?chat_id=' + \
                                    BOT_CHATID + \
                  '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)


def decode_emoji( competition_cod ):

    if(competition_cod=='AUS1'):
        return '\U0001F1E6\U0001F1F9 Austria Tipico Bundesliga'
    if(competition_cod=='AUS2'):
        return '\U0001F1E6\U0001F1F9 Austria Eerste Liga'
    if(competition_cod=='BEL1'):
        return '\U0001F1E7\U0001F1EA Belgium First Division'
    if(competition_cod=='BRA1'):
        return '\U0001F1E7\U0001F1F7 Brazil Serie A'
    if(competition_cod=='SWI1'):
        return '\U0001F1E8\U0001F1ED Switizerland Super League'
    if(competition_cod=='CZE1'):
        return '\U0001F1E8\U0001F1FF Czech-Republic 1-Liga'
    if(competition_cod=='CYP1'):
        return '\U0001F1E8\U0001F1FE Cyprus First Division'
    if(competition_cod=='DAN1'):
        return '\U0001F1E9\U0001F1F0 Denmark Superliga'
    if(competition_cod=='GRE1'):
        return '\U0001F1EC\U0001F1F7 Greece Super League'
    if(competition_cod=='HUN1'):
        return '\U0001F1ED\U0001F1FA Hungary Otp-Bank-Liga'
    if(competition_cod=='IRE1'):
        return '\U0001F1EE\U0001F1EA Ireland Premier Division '
    if(competition_cod=='ISR1'):
        return '\U0001F1EE\U0001F1F1 Israel Ligat-Ha-Al'
    if(competition_cod=='JAP1'):
        return '\U0001F1EF\U0001F1F5 Japan'
    if(competition_cod=='MAL1'):
        return '\U0001F1F2\U0001F1F9 Malta Premier-League'
    if(competition_cod=='OLA1'):
        return '\U0001F1F3\U0001F1F1 Holland Eredivisie'
    if(competition_cod=='OLA2'):
        return '\U0001F1F3\U0001F1F1 Holland Eerste Divisie'
    if(competition_cod=='POL1'):
        return '\U0001F1F5\U0001F1F1 Poland Ekstraklasa'
    if(competition_cod=='POR1'):
        return '\U0001F1F5\U0001F1F9 Portugal Primeira-Liga'
    if(competition_cod=='ROM1'):
        return '\U0001F1F7\U0001F1F4 Romania Liga-1'
    if(competition_cod=='SER1'):
        return '\U0001F1F7\U0001F1F8 Serbia Super Liga'
    if(competition_cod=='QAT1'):
        return '\U0001F1F6\U0001F1E6 Qatar QSL'
    if(competition_cod=='RUS1'):
        return '\U0001F1F7\U0001F1FA Russia Premier League'
    if(competition_cod=='SWE1'):
        return '\U0001F1F8\U0001F1EA Sweden Allsvenskan'
    if(competition_cod=='SLO1'):
        return '\U0001F1F8\U0001F1EE Slovenia Prva-Liga'
    if(competition_cod=='SLK1'):
        return '\U0001F1F8\U0001F1F0 Slovakia Fortuna Liga'
    if(competition_cod=='NOR1'):
        return '\U0001F1F3\U0001F1F4 Norway Eliteserien'
    if(competition_cod=='SCO1'):
        return '\U0001F1EC\U0001F1E7 Scotland Premiership'
    if(competition_cod=='TUR1'):
        return '\U0001F1F9\U0001F1F7 Turkey Super Lig'
    if(competition_cod=='UKR1'):
        return '\U0001F1FA\U0001F1E6 Ukraine Premier League'
    if(competition_cod=='ITA1'):
        return '\U0001F1EE\U0001F1F9 Italy Serie A'
    if(competition_cod=='ITA2'):
        return '\U0001F1EE\U0001F1F9 Italy Serie B'
    if(competition_cod=='ITAC'):
        return '\U0001F1EE\U0001F1F9 Italy Cup'
    if(competition_cod=='ITA3A'):
        return '\U0001F1EE\U0001F1F9 Italy Serie C Group A'
    if(competition_cod=='ITA3B'):
        return '\U0001F1EE\U0001F1F9 Italy Serie C Group B'
    if(competition_cod=='ITA3C'):
        return '\U0001F1EE\U0001F1F9 Italy Serie C Group C'
    if(competition_cod=='FRA1'):
        return '\U0001F1EB\U0001F1F7 France Ligue 1'
    if(competition_cod=='FRA2'):
        return '\U0001F1EB\U0001F1F7 France Ligue 2'
    if(competition_cod=='FRA3'):
        return '\U0001F1EB\U0001F1F7 France National'
    if(competition_cod=='FRAC'):
        return '\U0001F1EB\U0001F1F7 Coupe de France'
    if(competition_cod=='ENG1'):
        return '\U0001F1EC\U0001F1E7 England Premier League'
    if(competition_cod=='ENG3'):
        return '\U0001F1EC\U0001F1E7 England League One'
    if(competition_cod=='ENG4'):
        return '\U0001F1EC\U0001F1E7 England League Two'
    if(competition_cod=='ENGC1'):
        return '\U0001F1EC\U0001F1E7 England EFL-Cup'
    if(competition_cod=='ENGC1'):
        return '\U0001F1EC\U0001F1E7 England FA-Cup'
    if(competition_cod=='SPA1'):
        return '\U0001F1EA\U0001F1F8 Spain LaLiga'
    if(competition_cod=='SPA2'):
        return '\U0001F1EA\U0001F1F8 Spain LaLiga2'
    if(competition_cod=='ENG2'):
        return '\U0001F1EC\U0001F1E7 England Championship'
    if(competition_cod=='EUR1'):
        return '\U0001F1EA\U0001F1FA Champions League'
    if(competition_cod=='EUR2'):
        return '\U0001F1EA\U0001F1FA Europa League'
    if(competition_cod=='GER1'):
        return '\U0001F1E9\U0001F1EA Germany Bundesliga'
    if(competition_cod=='GER2'):
        return '\U0001F1E9\U0001F1EA Germany Bundesliga 2'
    if(competition_cod=='GERC'):
        return '\U0001F1E9\U0001F1EA Germany Cup'
    if(competition_cod=='BUL1'):
        return '\U0001F1E7\U0001F1EC Bulgaria Parva-Liga'
    if(competition_cod=='CRO1'):
        return '\U0001F1ED\U0001F1F7 Croatia 1-HNL'
    if(competition_cod=='AZE1'):
        return '\U0001F1E6\U0001F1FF Azerbaijan Premier League'
    else:
        return competition_cod

