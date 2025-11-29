import requests
all_html =""
for i in range(1,11):
  print("Page :", i)
  url = f'https://quotes.toscrape.com/page/{i}/'
  r = requests.get(url)
  r.encoding = "utf-8"
  all_html += r.text + "\n"

def scrap_quotes(html):
  with open('quotes.txt','w', encoding="utf-8") as f:
    for line in html.split('\n'):
      if '<span class="text" itemprop="text">' in line:
        line = line.replace('<span class="text" itemprop="text">','').replace('</span>','')
        line = line.strip()
        line = line.replace('“', '').replace('”', '')
        f.write(line + "\n")

def scrap_author(html):
  with open('author.txt','w', encoding="utf-8") as f:
    for line in html.split('\n'):
      if ' <span>by <small class="author" itemprop="author">' in line:
        line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
        line = line.strip()
        f.write(line + "\n")

scrap_author(all_html)
scrap_quotes(all_html)

def final_author_and_quotes(authors_file,quotes_file):

  with open(authors_file,'r',encoding="utf-8") as a:
    with open(quotes_file, 'r',encoding="utf-8") as q:
     with open("quotes.csv",'w',encoding="utf-8") as output:

      authors = a.readlines()
      quotes = q.readlines()

      for author, quote in zip(authors,quotes):
        output.write(f"{author.strip()},{quote.strip()}\n")


final_author_and_quotes('author.txt','quotes.txt')