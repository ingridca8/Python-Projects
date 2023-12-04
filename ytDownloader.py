from pytube import YouTube

link = input('Intro link: ')
yt = YouTube(link)

print('Title: ', yt.title)
print('Views: ', yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/home/Ingrid/Videos/Youtube')