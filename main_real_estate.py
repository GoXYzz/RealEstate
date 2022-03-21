from real_estate import RealEstateScraper

# Taking inputs from the user
page_num = input("How many pages you want to scrape: ")
new_file_name = input("Enter the name of the file to store json object: ")
city = input("Enter the name of the city: ")

# Passing inputs and making new instance of RealEstateScraper class
new_scrape_object = RealEstateScraper(page_num, new_file_name, city)
# Scraping method call
new_scrape_object.scrapy_method()