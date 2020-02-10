from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {}
os.chdir('F:/Downloads')

makeDirectory = input("\nCreate new directory for your downloads [y/n] :")
if makeDirectory == 'n':
	print("\nNo directory made for download so defaults to 'F/downloads\n'")
elif makeDirectory == 'y':
	down = input('\nName folder for downloads : ')
	path = os.path.join(os.getcwd(), down)
	if os.path.isdir(path):
		print("Path already exits so will be used for download.")
		print('Downloading to {}\n'.format(path))
	else:
		os.mkdir(path)
		print('Downloading to {}\n'.format(path))
else:
	print("\nInvalid Response, use either 'y' for 'yes' or 'n' for no\n\n")
	exit()

inputedLink = input("Input the link you want to download: ")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([inputedLink])