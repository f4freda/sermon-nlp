"""
AI sermon generator 
Start date: 6 Nov 2017

I downloaded audio files of sermons from Union website and used IBM Watson to transcribe. 
The resulting file from IBM Watson contains timestamps, confidence levels and 
alternative transcriptions. This script extracts only the transcript for our project. 

"""

import re

# open and read the file
# If you don't know the size of a file, better to 
# read it a chunk at a time and close it automatically.
# The with causes the file to automatically close 
# once the action inside of it finishes. 
# And the action inside, the .read(), 
# will finish when there are no more bytes to read from the file.
with open("file_name.txt") as open_file:
    data = open_file.read()

# search for sentence after "transcript"
pattern = re.compile(r'"transcript": "[-\w ]+"')
textblob = pattern.findall(data) #apply pattern to data
blob = str(textblob) #turn regex object into string

#general cleanup
blob = blob.replace("transcript", " ") # remove the word transcript
blob = re.sub('[^.,a-zA-Z0-9 \n\.]', '', blob) # remove punctuation
# blob = blob.translate(None, string.punctuation) 
# this is used to remove all punctuation 
# what i want is to remove all punctuation except comma and dot

# remove bible reading
end_read = "this is the word of the lord" # defines where bible reading ends
blob = blob.split(end_read, 1)[1] # split the text and keep the part after bible reading
blob = ' '.join(blob.split()) # join to remove excessive whitespace

# save to new file
with open('file_name_clean.txt', 'w') as f:  
    f.write(blob)