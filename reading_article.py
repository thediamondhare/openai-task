import requests 
import pandas as pd

def saveArticleContent():
    url = f'https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt'
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        textData = response.text
        rows = textData.strip().split('\n')
        data = [row.split('::') for row in rows]
        df = pd.DataFrame(data[1:], columns=data[0])
        df.to_csv('text.csv', index=False)
    else:
        raise Exception("Failed to fetch the file.")
  
def readArticleContent():
    saveArticleContent()
    articleText = pd.read_csv('text.csv', sep="::", encoding="utf-8")
    return articleText

