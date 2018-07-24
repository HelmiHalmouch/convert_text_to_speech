''' This main algorithm will be used 
	to convert the text to speech
	then save the audio result as 
	.mp3 file'''

 

import time 
from gtts import gTTS

tic = time.clock()

''' read the text from the file'''
file_txt_name = "Texte_1"

file = open("text_files/"+file_txt_name+".text", "r") 
text = file.read() 
#print(text)

''' write the audio file'''

tts = gTTS(text, lang='en')
tts.save("output_results/"+file_txt_name+".mp3")

toc = time.clock()
print('Processing finished in :',str(toc-tic),'s')

# TODO 
'''
make the script as a function 
if __name__ == '__main__':

	'''