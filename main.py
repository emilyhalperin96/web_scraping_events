import requests 
import selectorlib

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

def send_email():
    pass

def store(extracted):
    with open('data.txt', 'a') as file:
        file.write(extracted + '\n') 

def read(extracted):
    with open('data.txt', 'r') as file:
        return file.read()

if __name__ == '__main__':
    scraped = scrape(URL)
    extracted = extract(scraped)
    
    content = read(extracted)
    print(extracted)
    if extracted != 'No upcoming tours':
        if extracted not in content:
            #only store an event when the event is new 
            store(extracted)
            send_email()


