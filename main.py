import pytube

url = input("Enter video URl: ")

path = ""
pytube.YouTube(url).streams.get_highest_resolution().download(path)
