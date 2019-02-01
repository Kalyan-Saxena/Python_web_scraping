import requests
from bs4 import BeautifulSoup
from csv import writer

response=requests.get('http://motherkinda.000webhostapp.com/index.html')

soup = BeautifulSoup(response.text,'html.parser')
links = soup.find_all('a')

with open('scrap.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    header = ['Link_Title','Link-Navigation']
    csv_writer.writerow(header)
    for link in links:
        if len(link.get_text())>0:
            csv_writer.writerow([link.get_text(), link['href']])
        else:
            if link.find('i')==None:
                pass
            else:
                csv_writer.writerow([link.find('i')['class'][1], link['href']])






