#beautifulsoup4 module 4 is the 4th version of bs4
import bs4
import requests
res = requests.get('https://www.amazon.in/Zephyrus-GU502GU-ES003T-15-6-inch-i7-9750H-Graphics/dp/B07RSS7MRW/ref=sr_1_1?dchild=1&keywords=asus+rog&qid=1590250951&sr=8-1')
#res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
