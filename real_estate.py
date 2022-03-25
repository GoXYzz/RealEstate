# The goal is to extract data from the website and get details about real estate for rent in the specified city in Serbia
# and store the results in JSON file
from bs4 import BeautifulSoup
import requests

class RealEstateScraper:
	""" Scraper needs input for numbers of pages for scraping, file name and name of the city """
	def __init__(self, pages, file_name, city_name):
		self.pages = pages
		self.file_name = file_name + ".json"
		self.city_name = city_name

	# Method for scraping
	def scrapy_method(self):
		""" Making file for storing objects """
		f = open(self.file_name, "a")
		# Opening json object
		f.write("{" + '"' + self.city_name + '"' + ": [")
		# ID is unique identificator for object
		ID = 0

		# *pages defines number of pages for scraping
		for self.num_page in range(1, int(self.pages)):
			# Making request
			r = requests.get(f"https://www.halooglasi.com/nekretnine/izdavanje-stanova/" + 
				self.city_name + "?page=" + str(self.num_page))
			# Soup pattern
			soup = BeautifulSoup(r.text, features='html.parser')
			# Searching for data in specified div
			results = soup.find_all('div', {'class': 'my-product-placeholder'})

			for result in results:
				# Getting the price
				cena = result.find('div', {'class': 'central-feature'}).text
				# Trimming space and removing euro sign
				euro = cena.rstrip('.\xa0€')
				# Removing decimal point     								
				price = euro.replace('.', '') 									
				print(cena)

				# Getting the title
				searching_title = result.find("h3", {"class":"product-title"}).text
				# Removing quotes from title
				title = searching_title.replace('"', '')							
				print(title)

				# Getting the place
				place = result.find("ul", {"class" : "subtitle-places"}).text
				print(place)

				# Getting details section
				details = result.find("ul", {"class" : "product-features"}).text
				print(details)
				
				# Getting about section
				searching_about = result.find("p", {"class" : "product-description"}).text
				about = searching_about.replace('"', '')
				print(about)

				# Opening file and appending results
				f = open(self.file_name, "a")
				# Makin json objects
				f.write("{\n" + '"' + "ID" + '"' + ":" +  str(ID)  + ",\n"
				+ '"' + "price" + '"' + ":" + price + ",\n" 
				+ '"' + "title" + '"' + ":" + '"' + title + '"' + ",\n" 
				+ '"' + "place" + '"' + ":" + '"' + place + '"' + ",\n"
				+ '"' + "details" + '"' + ":" + '"' + details + '"' + ",\n" 
				+ '"' + "about" + '"' + ":" + '"' + about + '"' + "\n},")
				#Incrementing identificator for the next loop
				ID += 1

		# Forming the last line of JSON object
		f = open(self.file_name, "a")
		f.write("]}")

		# Reading the file into a list of lines
		lines = open(self.file_name, 'r').readlines()
		# Editing the last line of the list of lines
		new_last_line = (lines[-1].replace(",", ''))
		# Removing comma from the last line
		lines[-1] = new_last_line
		# Writing the modified list back out to the file
		open(self.file_name, 'w').writelines(lines)


