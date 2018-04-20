import requests
import bs4
from itertools import cycle

LEVEL_0_WEBSITE = "http://www.r-u-ready.xyz/"
LEVEL_0_PARSER = "html.parser"
LEVEL_0_PICTURE = "level0.png"
LEVEL_0_ENCODING = "base64"
WRITE_MODE = "wb"

# DATA is the the memory of the script in level0_right
DATA = "7A  46  5C  53  55  59  03  5A  41  03  06  01".replace(" ", "").decode('hex')
# KEY is the string in the center of the downloaded picture
KEY = "Israel-is-70"


def main():
    # Download the image
    website_data = requests.get(LEVEL_0_WEBSITE).text
    encoded_image = bs4.BeautifulSoup(website_data, LEVEL_0_PARSER).find_all('img')[0]['src']
    encoded_image = encoded_image.replace("data:image/png;base64, ", "")
    decoded_image = encoded_image.decode(LEVEL_0_ENCODING)
    with open(LEVEL_0_PICTURE, WRITE_MODE) as file_object:
        file_object.write(decoded_image)

    # Calculate the solution
    key = cycle(KEY)
    print ''.join(map(lambda x: chr(ord(x) ^ ord(key.next())), DATA))


if __name__ == "__main__":
    main()
