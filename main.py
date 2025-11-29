import requests
r = requests.get("https://quotes.toscrape.com/")
r.encoding = "utf-8"
# print(r.status_code)

html = r.text
with open('quotes.txt','w', encoding="utf-8") as f:
  for line in html.split('\n'):
    if '<span class="text" itemprop="text">' in line:
      line = line.replace('<span class="text" itemprop="text">','').replace('</span>','')
      line = line.strip()
      line = line.replace('“', '').replace('”', '')
      f.write(line + "\n")

html2 = r.text
with open('author.txt','w', encoding="utf-8") as f:
  for line in html.split('\n'):
    if ' <span>by <small class="author" itemprop="author">' in line:
      line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
      line = line.strip()
      f.write(line + "\n")

