import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?source=hp&ei=p3LcXPrvF9Hw9AOTipnADw&q=finastra+website&oq=finastra+website&gs_l=psy-ab.12..0.721.12863..13010...8.0..0.217.4258.0j26j2......0....1..gws-wiz.....0..0i131j0i10j0i22i30j33i160j0i22i10i30.slGFQRwOrWs'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text.encode('utf-8'))
