'''
Here we start the implimantation 
of multithreding using python 
firstly using a easy example 
then for the preblem of text to speech 

'''
# import package for threading
import threading 


# def task before applay threding

x = 0 
def task(lock_arg):
	global x 
	for i in range(1000000):

		lock_arg.acquire(True)
		x +=1
		lock_arg.release()

# applay treading on the main task
def main_task():

	# add local arg to addjust the threading.Thread command 
	lock_arg = threading.Lock()
	#apply therading command 
	t1 = threading.Thread(target = task, args = (lock_arg,))
	t2 = threading.Thread(target = task, args = (lock_arg,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()



# try
if __name__ == '__main__':
	
	main_task()

	print("{0}".format(x))
