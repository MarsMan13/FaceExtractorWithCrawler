from getFace import GetFace
from naver_image_downloader import NaverImageDownloader

if __name__ == "__main__":
    keyWords = []
    print("======Naver image crawler + Face image extractor ======")
    while True:
        keyWord = input("인물의 이름은 입력하세요(공백입력시 입력 종료) : ")
        if keyWord.strip() == "":
            break
        limit = int(input("크롤링할 이미지의 갯수를 입력하세요(ex) 20): "))
        keyWords.append((keyWord, limit))

    for ele in keyWords:
        keyWord = ele[0]
        limit = ele[1]
        imageDownloader = NaverImageDownloader(keyWord, limit)
        imageDownloader.download_images()
        print("---", keyWord, "---")
        print("--- All images crawled ---")
        print("--- Extrating face image Starts ---")
        faceGetter = GetFace(keyWord)
        faceGetter.run()
        print("--- Extrating face image finishes ---")

    print("\n\n\n===                End of program              ====")
    print("===           created by choiGoChoiGun          ===")
    print("===      This is an open source(public domain)  ===")
