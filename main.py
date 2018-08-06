''' This main algorithm will be used 
	to convert the text to speech
	then save the audio result as 
	.mp3 file'''

import time 
from gtts import gTTS
from commune import get_read_list_txt_file


def run_main_convert_text2speech(input_folder,output_folder,extention):
	''' read the text from the file'''
	file_txt_name_list, readed_text_list = get_read_list_txt_file(input_folder,extention)

	''' write the audio file'''

	for i in range(0,len(file_txt_name_list)):
		tts = gTTS(str(readed_text_list[i]), lang='en')
		tts.save(str(file_txt_name_list[i])+".mp3")


	
if __name__ == '__main__':

	tic = time.clock()

	print("---> please wait!")
	
	input_folder= "./text_files"
	output_folder = "output_results/"
	
	extention = ".text"
	
	run_main_convert_text2speech(input_folder,output_folder,extention)
	
	toc = time.clock()
	print('Processing finished in :',str(toc-tic),'s')