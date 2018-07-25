''' This main algorithm will be used 
	to convert the text to speech
	then save the audio result as 
	.mp3 file'''

import time 
from gtts import gTTS
from commune import get_read_list_txt_file

tic = time.clock()

''' read the text from the file'''

input_folder= "./text_files"
file_txt_name_list, readed_text_list = get_read_list_txt_file(input_folder)

''' write the audio file'''
output_folder = "output_results/"

for i in range(0,len(file_txt_name_list)):
	tts = gTTS(str(readed_text_list[i]), lang='en')
	tts.save(str(file_txt_name_list[i])+".mp3")

toc = time.clock()
print('Processing finished in :',str(toc-tic),'s')

# TODO 
'''
make the script as a function 
if __name__ == '__main__':

	'''