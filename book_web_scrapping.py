import requests
import bs4
import re


# GOAL: Get the title of every book with 2-star rating

# products = soup.select(".product_pod")

my_dict = {
	'1' : 'One',
	'2' : 'Two',
	'3' : 'Three',
	'4' : 'Four',
	'5' : 'Five'
}
list_stars = [1, 2, 3, 4, 5]
fav_star = 0
two_star_titles_1 = []
two_star_titles_2 = []

# Solution 1. Check desired class in item or not
def two_star_1(num, products):
	for item in products:
		if f'star-rating {num}' in str(item):
			book_img = item.select("img")
			title = book_img[0]['alt']
			two_star_titles_1.append(title)
			print(title)

# --------------------------------------------

# Solution 2. Automatically choose the item has desired class
def two_star_2(num, products):
	for item in products:
		if len(item.select(f".star-rating.{num}")) != 0:
			a_book = item.select("h3 > a")
			# print(img_book)
			title = a_book[0]['title']
			two_star_titles_2.append(title)
			print(title)


base_url = "http://books.toscrape.com/catalogue/page-{}.html"
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
text = soup.select("ul > li.current")[0].getText()

pattern = r'\d{2}'
last_page_num = int(re.findall(pattern, text)[-1])

while True:
	fav_star = input("What's the number of stars you want? (1-5) ")

	if int(fav_star) not in list_stars:
		print("Please input a number from 1 to 5!")
		continue
	else:
		break

for x in range(1, last_page_num + 1):
	scrape_url = base_url.format(x)
	res = requests.get(scrape_url)

	print(f"\n==================== Page {x} / {last_page_num} ====================\n")
	print(f"This is page {x}, url: {scrape_url}")

	soup = bs4.BeautifulSoup(res.text, 'lxml')
	products = soup.select(".product_pod")
	two_star_1(my_dict[fav_star], products)
	print("---------------------------------")
	two_star_2(my_dict[fav_star], products)

print(two_star_titles_1)
print(two_star_titles_2)