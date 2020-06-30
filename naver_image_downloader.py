from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import os

if __name__ == "__main__":
    print("this is main")

class NaverImageDownloader:

    baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
    img_path = './img/'

    def __init__(self, keyWord, limit, img_path=None):
        self.keyWord = keyWord
        self.limit = limit
        if(img_path != None):
            self.img_path = img_path


    def download_images(self):
        if not os.path.exists(self.img_path):
            os.makedirs(self.img_path)

        url = self.baseUrl + quote_plus(self.keyWord)

        html = urlopen(url)
        soup = bs(html, "html.parser")
        img = soup.find_all(class_='_img')

        n = 1
        for i in img:
            imgUrl = i['data-source']
            with urlopen(imgUrl) as f:
                with open(self.img_path + self.keyWord + str(n)+'.jpg', 'wb') as h:
                    img = f.read()
                    h.write(img)
            if self.limit <= n:
                break
            n += 1


