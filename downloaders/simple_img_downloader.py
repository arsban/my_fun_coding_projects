import requests


def img_download(url=""):
    filename = "You_download_this_file_by_arsban"
    try:
        response = requests.get(url=url)

        with open(f'filename.{"jpeg"}', "wb") as file:
            file.write(response.content)
        return "Img downloaded"
    except Exception as ex:
        return f"Somethin wrong...{ex}"


def main():
    print(img_download(url=input("URL >>> ")))


if __name__ == '__main__':
    main()
