# this programm will use pytube to read all the URL´s in a youtube playlist, associate them to the video´s title and save them into a file.
#  The purpose of this programm is to prevent loosing videos from a playlist due to their removal from the platform.

from pytube import *


#create a .txt file 
lines = ['Here all the results will be logged',]
with open('log.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line)
        f.write('\n')


#get the playlist´s URL
plist = input("instert the playlist´s URL: ")

#print the number of videos in the playlist
selected_playlist = Playlist(plist)

print("the number of videos in the playlist: " + str(selected_playlist.length))

#log every URL of the playlist
p = Playlist(plist)

#this function will print all the titles associated to the video´s URLs and write them on the .txt file
def title_logger(x_url):
    yt = YouTube(x_url)
    print(yt.title)
    with open('log.txt', 'a',  encoding='utf-8') as f:
        f.write(''.join(yt.title))
        f.write(' : ')
#get the number of videos we want to sort out
number = input("insert the number of videos in the playlist ")


#this loop will print the playlist´s URLs and use the title_logger function, then it writes them on the .txt file
for url in p.video_urls[:int(number)]:
    print(url),title_logger(url)
    with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(''.join(url))
            f.write('\n')
    



