import requests 
import selectorlib
import os 
import smtplib, ssl
import time 

URL = 'https://programmer100.pythonanywhere.com/tours/'

#get the page source 

def scrape(url):
    #scrape the page source from the URL
    response = requests.get(url)
    #get the text 
    source = response.text
    return source 

def extract(source):

    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value 

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'emilyphalperin@gmail.com'
    password = 'enter pw'

    receiver = 'emilyphalperin@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    

def store(extracted):
    with open('data.txt', 'a') as file:
        file.write(extracted + '\n') 

def read(extracted):
    with open('data.txt', 'r') as file:
        return file.read()

if __name__ == '__main__':
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        
        content = read(extracted)
        print(extracted)
        if extracted != 'No upcoming tours':
            if extracted not in content:
                #only store an event when the event is new 
                store(extracted)
                send_email(message='Hey, new event was found.')
        time.sleep(2)


