import os, glob 
import shutil
from os.path import basename
from gtts import gTTS

# now you can call it directly with basename
#print(basename("/a/b/c.txt"))

def get_read_list_txt_file(input_folder):

	readed_text_list = []
	file_txt_name_list = []

	os.chdir(input_folder)
	for file in glob.glob("*.text"):
		#print(file)
		#print(basename(file))
		file_text_name = os.path.splitext(file)[0]
		#print(file_text_name)
		file = open(file_text_name+".text", "r") 
		text = file.read() 
		file_txt_name_list.append(file_text_name)
		readed_text_list.append(text)

	return file_txt_name_list, readed_text_list

'''
if __name__ == '__main__':
	input_folder= "./text_files"
	file_txt_name_list, readed_text_list= get_read_list_txt_file(input_folder)
	print(file_txt_name_list)
	print(readed_text_list)'''


