import requests 
from bs4 import BeautifulSoup
urls = ['https://www.joiasgold.com.br/aneis', 'https://www.joiasgold.com.br/aliancas'] 
headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

dicURL = {'URL':[],'Title':[]}
for url in urls: 
	req = requests.get(url)
	print(req.text)
	soup = BeautifulSoup(req.text, 'html.parser')
	titulo = soup.find_all('title')
	dicURL['URL'].append(url)
	dicURL['Title'].append(titulo)
	
print(dicURL)