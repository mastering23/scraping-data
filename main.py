import requests
for i in range(1,11):
  print("Page :", i)
  url = f'https://quotes.toscrape.com/page/{i}/'
  r = requests.get(url)
  r.encoding = "utf-8"
  html = r.text

  with open('quotes.txt','a', encoding="utf-8") as f:
    for line in html.split('\n'):
      if '<span class="text" itemprop="text">' in line:
        line = line.replace('<span class="text" itemprop="text">','').replace('</span>','')
        line = line.strip()
        line = line.replace('“', '').replace('”', '')
        f.write(line + "\n")

  with open('author.txt','a', encoding="utf-8") as f:
    for line in html.split('\n'):
      if ' <span>by <small class="author" itemprop="author">' in line:
        line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
        line = line.strip()
        f.write(line + "\n")

