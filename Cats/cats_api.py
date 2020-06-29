import requests
from PIL import Image
from io import BytesIO


url = "https://api.thecatapi.com/v1/images/search"


class Cats(object):
    """API for search random cats photos"""

    def __init__(self, url):
        self.api_url = url

    def search(self):
        response = requests.get(self.api_url)
        return response.json()

    def get_img_url(self):
        self.img_url = self.search()[0]['url']
        return self.img_url

    def get_img_width(self):
        self.img_width = self.search()[0]['width']
        return self.img_width

    def get_img_height(self):
        self.img_height = self.search()[0]['height']
        return self.img_height

    def get_id(self):
        self.id = self.search()[0]['id']
        return self.id

    def get_breeds(self):
        self.breeds = self.search()[0]['breeds']
        return self.breeds


if __name__ == '__main__':
    img = Cats(url)
    pic = img.get_img_url()
    print(pic)
    image = Image.open(BytesIO(requests.get(pic).content))
    image.show()
