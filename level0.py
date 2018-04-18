import requests
import bs4


LEVEL_0_WEBSITE = "http://www.r-u-ready.xyz/"
LEVEL_0_PARSER = "html.parser"
LEVEL_0_PICTURE = "level0.png"
LEVEL_0_ENCODING = "base64"
WRITE_MODE = "wb"


def main():
	website_data = requests.get(LEVEL_0_WEBSITE).text
	encoded_image = bs4.BeautifulSoup(website_data, LEVEL_0_PARSER).find_all('img')[0]['src'].replace("data:image/png;base64, ", "")
	decoded_image = encoded_image.decode(LEVEL_0_ENCODING)
	with open(LEVEL_0_PICTURE, WRITE_MODE) as file_object:
		file_object.write(decoded_image)


if __name__ == "__main__":
	main()
