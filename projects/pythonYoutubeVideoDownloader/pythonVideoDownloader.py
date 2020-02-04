from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {}
os.chdir('F:/Downloads')
inputedLink = input("Input the link you want to download: ")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([inputedLink])