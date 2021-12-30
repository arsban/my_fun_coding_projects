import requests


def video_download(url=""):
    """Функция позволяет скачивать видеофайлы в формате mp4 и просматривать их
    во время скачивания. благодаря аргументу stream=True в методе get() библиотеки requests.
    аргумент chunk_size в методе iter_content() выделяет место в памяти, которое может иметь только числовое значение.
    этот промежуток видеоряда и можно просматривать. """
    filename = "You_download_this_file_by_arsban"
    try:
        response = requests.get(url=url, stream=True) 
        response.raise_for_status()
        with open(f'filename.{"mp4"}', "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return "VideoFile downloaded"
    except Exception as ex:
        return f"Somethin wrong...{ex}"


def main():
    print(video_download(url=input("URL >>> ")))


if __name__ == '__main__':
    main()
