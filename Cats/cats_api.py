import requests


url = "https://api.thecatapi.com/v1/images/search"


class Cats(object):
    """API for search random cats photos"""

    def __init__(self, url):
        self.api_url = url
        self.search_response = None

    def search(self):
        self.search_response = requests.get(self.api_url)
        return self.search_response.json()

    def get_img_url(self):
        """ use after self.search """
        self.img_url = self.search_response.json()[0]['url']
        return self.img_url

    def get_img_width(self):
        """ use after self.search """
        self.img_width = self.search_response.json()[0]['width']
        return self.img_width

    def get_img_height(self):
        """ use after self.search """
        self.img_height = self.search_response.json()[0]['height']
        return self.img_height

    def get_id(self):
        """ use after self.search """
        self.id = self.search_response.json()[0]['id']
        return self.id

    def get_breeds(self):
        """ use after self.search """
        self.breeds = self.search_response.json()[0]['breeds']
        return self.breeds


if __name__ == '__main__':
    from PIL import Image
    from io import BytesIO

    img = Cats(url)
    img.search()
    pic = img.get_img_url()
    print(pic)
    image = Image.open(BytesIO(requests.get(pic).content))
    image.show()
