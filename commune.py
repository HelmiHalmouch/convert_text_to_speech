import os, glob 
from os.path import basename

# now you can call it directly with basename
#print(basename("/a/b/c.txt"))

def get_list_txt_file(input_folder):

	list_text_file_name = []

	os.chdir(input_folder)
	for file in glob.glob("*.text"):
		#print(file)
		#print(basename(file))
		file_text_name = os.path.splitext(file)[0]

		list_text_file_name.append(file_text_name)
		#print(file_text_name)

	return list_text_file_name



if __name__ == '__main__':
	input_folder= "./text_files"
	print(get_list_txt_file(input_folder))
	
'''
	#print(list_text_file_name)

for i in range(0,len(list_text_file_name)):
	print(i) '''
