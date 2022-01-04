import requests
from bs4 import BeautifulSoup
import sys

# requirements are requests, beautifulsoup4, sys and html5lib
# lxml didn't work for some reason so i used html5lib


if __name__ == "__main__":
	search = ""
	if(len(sys.argv) > 1): # if there are other args than the current working directory
		for i, arg in enumerate(sys.argv): # some fancy loop
			if(i > 0): # exclude the cwd
				search = search + arg + " " # add up the arguments
	else:
		search = input("https://www.urbandictionary.com/define.php?term=") # ask for user input
	print(search) # debug
	url = "https://www.urbandictionary.com/define.php?term=" + search # url gets merged
	print(url) # debug
	print('\n'*2) # seperation
	r = requests.get(url).text # get the html
	soup = BeautifulSoup(r, 'html5lib') # make some soup
	for match in soup.find_all('div', class_='meaning my-4'): # find all meaning
		print("="*120) # seperation
		print(match.text) # print meaning
		print("="*120) # seperation
		print('\n') # seperation