import imp


import pytube

link= 'https://www.youtube.com/watch?v=wHpUQ5K68Bc'
yt= pytube.YouTube(link)
yt.streams.first().download('C:/Users/DELL/Documents/PYTHON/Python_Download/')
print('Done!')