from web3 import Web3
from playsound import playsound
from termcolor import colored
import schedule
from datetime import datetime
from pytz import timezone
from adr import addresses
import smtplib


#===============Mail Settings(Optional)=====================
sender_mail = "" # Mail from which you will send alert
sender_password = "" # Check your sender mail password at Google/apppasswords
receiver_mail = "" # Mail on which you will receive alert (it can be same as sender mail)

#================Alert Sound(Optional)=======================
alert_sound = "./alert.mp3" # Put your alert sound, leave blank if none

#===============Log File settings(Optional)==================
log_file = "./whale_address_log.txt" # Path to your log file, leave blank if none

#===============Threshold settings====================
#Send alert if balance is more than:
eth_balance = 200
bnb_balance = 100000
matic_balance = 10000000
fantom_balance = 10000000
avax_balance = 100000


separator = 60*"="

ankr_eth = "https://rpc.ankr.com/eth"
eth3 = Web3(Web3.HTTPProvider(ankr_eth))

ankr_bnb = "https://rpc.ankr.com/bsc"
bnb3 = Web3(Web3.HTTPProvider(ankr_bnb))

ankr_polygon = "https://rpc.ankr.com/polygon"
matic3 = Web3(Web3.HTTPProvider(ankr_polygon))

ankr_avalanche = "https://rpc.ankr.com/avalanche"
avax3 = Web3(Web3.HTTPProvider(ankr_avalanche))

ankr_fantom = "https://rpc.ankr.com/fantom"
fantom3 = Web3(Web3.HTTPProvider(ankr_fantom))


def ether():
    print("")
    print("Checking Time: " + datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S | %d-%m-%Y'))
    print("=========================Checking ETH==========================")
    print("  Time                     Address                         Balance")
    for n in addresses:
        balance = eth3.eth.getBalance(n)
        convert_in_eth = eth3.fromWei(balance, "ether")
        # Checking ETH balance
        if convert_in_eth > eth_balance:
            print(colored(datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S') + " || " + n + " || " + str("%.8f" %
                convert_in_eth) + " ETH!!!", "red"))
            
            #textfile log
            try:
                with open(log_file, "a") as file:
                    file.writelines(f'{str("%.1f" %convert_in_eth)} ETH \n{n}\n{separator}\n')
            except:
                continue
            
            # alert sound
            try:
                playsound(alert_sound)
            except:
                continue
    
            
            # alert on mail
            try:
                sender = sender_mail
                password = sender_password
                receiver = receiver_mail
                subject = "Whale Alert!"
                body = "Address: \n" + n + "\n\n" + "Balance: " + str("%.2f" %convert_in_eth) + " ETH !!!"
                message = 'Subject: {}\n\n{}'.format(subject, body)

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, receiver, message)
            except:
                continue
                
        print(datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S') + " || " + n + " || " + str("%.8f" %
                    convert_in_eth) + " ETH")




def bnb():
    print("")
    print("Checking Time: " + datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S | %d-%m-%Y'))
    print("==========================Checking BNB==========================")
    print( "  Vreme                     Address                         Balance")
    for n in addresses:
        balance = bnb3.eth.getBalance(n)
        convert_in_bnb = bnb3.fromWei(balance, "ether")
        if convert_in_bnb > bnb_balance:
            print(colored(datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S') + " || " + n + " || " + str("%.8f" %
                convert_in_bnb) + " BNB!!!", "red"))
            #textfile log
            try:
                with open(log_file, "a") as file:
                    file.writelines(f'{str("%.1f" %convert_in_bnb)} BNB \n{n}\n{separator}\n')
            except:
                continue

            # alert sound
            try:
                playsound(alert_sound)
            except:
                continue

            # alert on mail
            try:
                sender = sender_mail
                password = sender_password
                receiver = receiver_mail
                subject = "Whale Alert!"
                body = "Address: \n" + n + "\n\n" + "Balance: " + str("%.2f" %convert_in_bnb) + " BNB !!!"
                message = 'Subject: {}\n\n{}'.format(subject, body)

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, receiver, message)
            except:
                continue
                
        print(datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S') + " || " + n + " || " + str("%.8f" %
                    convert_in_bnb) + " BNB")



def matic():
    print("")
    print("Checking Time: " + datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S | %d-%m-%Y'))
    print("==========================Checking MATIC==========================")
    print("  Vreme                     Address                         Balance")
    for n in addresses:
        balance = matic3.eth.getBalance(n)
        convert_in_matic = matic3.fromWei(balance, "ether")
        if convert_in_matic > matic_balance:
            print(colored(datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S') + " || " + n + " || " + str("%.8f" %
                convert_in_matic) + " MATIC!!!", "red"))
            #textfile log
            try:
                with open(log_file, "a") as file:
                    file.writelines(f'{str("%.1f" %convert_in_matic)} MATIC \n{n}\n{separator}\n')
            except:
                continue

            # alert sound
            try:
                playsound(alert_sound)
            except:
                continue

            # alert on mail
            try:
                sender = sender_mail
                password = sender_password
                receiver = receiver_mail
                subject = "Whale Alert!"
                body = "Address: \n" + n + "\n\n" + "Balance: " + str("%.2f" %convert_in_matic) + " MATIC !!!"
                message = 'Subject: {}\n\n{}'.format(subject, body)

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, receiver, message)
            except:
                continue
                
        print(datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S') + " || " + n + " || " + str("%.8f" %
                    convert_in_matic) + " MATIC")

def avax():
    print("")
    print("Checking Time: " + datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S | %d-%m-%Y'))
    print("==========================Checking AVAX==========================")
    print("  Vreme                     Address                         Balance")
    for n in addresses:
        balance = avax3.eth.getBalance(n)
        convert_in_avax = avax3.fromWei(balance, "ether")
        if convert_in_avax > avax_balance:
            print(colored(datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S') + " || " + n + " || " + str("%.8f" %
                convert_in_avax) + " AVAX!!!", "red"))
            #textfile log
            try:
                with open(log_file, "a") as file:
                    file.writelines(f'{str("%.1f" %convert_in_avax)} AVAX \n{n}\n{separator}\n')
            except:
                continue

            # alert sound
            try:
                playsound(alert_sound)
            except:
                continue

            # alert on mail
            try:
                sender = sender_mail
                password = sender_password
                receiver = receiver_mail
                subject = "Whale Alert!"
                body = "Address: \n" + n + "\n\n" + "Balance: " + str("%.2f" %convert_in_avax) + " AVAX !!!"
                message = 'Subject: {}\n\n{}'.format(subject, body)

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, receiver, message)
            except:
                continue
                
        print(datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S') + " || " + n + " || " + str("%.8f" %
                    convert_in_avax) + " AVAX")


def fantom():
    print("")
    print("Checking Time: " + datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S | %d-%m-%Y'))
    print("==========================Checking FANTOM==========================")
    print("  Vreme                     Address                         Balance")
    for n in addresses:
        balance = fantom3.eth.getBalance(n)
        convert_in_fantom = fantom3.fromWei(balance, "ether")
        if convert_in_fantom > fantom_balance:
            print(colored(datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S') + " || " + n + " || " + str("%.8f" %
                convert_in_fantom) + " FANTOM!!!", "red"))
            #textfile log
            try:
                with open(log_file, "a") as file:
                    file.writelines(f'{str("%.1f" %convert_in_fantom)} FANTOM \n{n}\n{separator}\n')
            except:
                continue

            # alert sound
            try:
                playsound(alert_sound)
            except:
                continue

            # alert on mail
            try:
                sender = sender_mail
                password = sender_password
                receiver = receiver_mail
                subject = "Whale Alert!"
                body = "Address: \n" + n + "\n\n" + "Balance: " + str("%.2" %convert_in_fantom) + " FANTOM !!!"
                message = 'Subject: {}\n\n{}'.format(subject, body)

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, receiver, message)
            except:
                continue
                
        print(datetime.now(timezone('Europe/Rome')).strftime('%H:%M:%S') + " || " + n + " || " + str("%.8f" %
            convert_in_fantom) + " FANTOM")


# Main function which call other 5 function
def balance():
    return ether(), bnb(), matic(), avax(), fantom()

schedule.every(1).minutes.do(balance)

balance()
while True:
    schedule.run_pending()
    




