import csv,re,time, keyboard, webbrowser, glob, datetime
tomorrow = datetime.datetime.now() + datetime.timedelta(1) #tommorow DAY-MNTH-YEAR
csvopen=glob.glob("*.csv") #any CSV file in a current folder
with open(csvopen[0]) as csvfile:
    numreader=csv.reader(csvfile, delimiter=';')
    str_list = []
    for row in numreader:
        phonenumber=re.sub(r'\D', '',row[3]).split() #elaborate phone numbers from row 11, replace all non-numeric symbols with '', using regular expressions 
        message=("TEXT1"+row[1]+"SPACE"+row[2]+"TEXT2"+tomorrow.strftime('%d-%m-%Y')+"TEXT3"+row[0]+".")
        for i in phonenumber:
            webbrowser.open("https://web.whatsapp.com/send?phone=39"+i+"&text="+message) #open WhatsAPP WEB, and send messages
            time.sleep(9)
            keyboard.press_and_release("enter")
            time.sleep(7)
            keyboard.press_and_release("ctrl+w")
            keyboard.press_and_release("enter")
