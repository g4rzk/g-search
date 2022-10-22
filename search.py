# author by g4rzk (Angga Kurniawan)
# 22/Okt/2022 09:39 PM

import argparse
from g4rzk.module import *

class search:
	def __init__(self):
		self.count = []
		self.google_url = "https://www.google.com"

	def get_form(self, url_main):
		soup = parser(ses.get(f"{url_main}", headers={"user-agent": "chrome"}).text, "html.parser")
		for form in soup.find_all("div", class_="egMi0 kCrYT"):
			regex_title = re.search(r'<h3 class=".*?"><div class=".*?">(.*?)<\/div>', str(form))
			regex_url = re.search(r'<div class=".*?"><a href\=\"\/(.*?)\">', str(form))
			print(f"  - {regex_title.group(1)}\n  - {regex_url.group(1)}\n")
			self.count.append(regex_title.group(1))

			if len(self.count) == arg.count:
				print(f"\n  - Search {len(self.count)} url, finished...")
				sys.exit()

		for n in soup.find_all("div", class_="nMymef MUxGbd lyLwlc"):
			for i in n.find_all("a", href=True):
				if "Berikutnya >" in i.text:
					run.get_form(f"{self.google_url}/"+i.get("href"))

if __name__ == "__main__":
	parse = argparse.ArgumentParser()
	parse.add_argument("-c", metavar="<COUNT>", type=int, dest="count", help="the number of urls you want to scrape")
	parse.add_argument("-q", metavar="<QUERY>", dest="query", help="google query that you want to scrape")
	arg = parse.parse_args()
	
	run = search()
	if arg.query and arg.count:
		try:
			os.system("clear")
			run.get_form(f"https://www.google.com/search?q={arg.query}")
		except:
			pass
	else:
		parse.print_help()
