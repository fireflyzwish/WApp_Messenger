import csv,re,time, keyboard, webbrowser, datetime #modules to import
with open("*NAME*.csv") as csvfile: #*.CSV file should be named as *NAME*
    numreader=csv.reader(csvfile, delimiter=';') #delimiter CSV
    str_list = [] #make the list
    for row in numreader: #open the file
        phonenumber=re.sub(r'\D', '',row[11]).split() #elaborate phone numbers from row 11, replace all non-numeric symbols with '', using regular expressions 
        message=("Dear "+row[9]+", you have an appointment at "+row[12]+" "+row[13]+". This message is a reminder, don't hesitate to contact us via mail or something else blah blah blah")
        for i in phonenumber:
            webbrowser.open("https://web.whatsapp.com/send?phone=39"+i+"&text="+message) #open WhatsAPP API, and send messages
            time.sleep(7)
            keyboard.press_and_release("enter")
            time.sleep(5)
            keyboard.press_and_release("ctrl+w")
            keyboard.press_and_release("enter")
