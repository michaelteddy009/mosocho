with open('attachments/file1.txt') as f:
	#print(f.mode) #this gives the mode that the file is in and for this case it's in read mode presented by r.
	#fContents = f.read() #this reads all of the contents of the file but if we specify something like f.read(100) then the first 100 characters will be reead from the file
	#print(fContents) #if incase we passed  a size to read then printing f.tell() will tell us the current position
	#if we read particular size but want the next read command to start from the beginning we use f.seek(0n)

	#fReadlines = f.readline() #this will read the first line in the text but note readlines will oontain all the lines in a list
	#print(fReadlines)

	for line in f:
			print(line, end='')	 # this will print the entire file too