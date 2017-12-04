from time import sleep

def sleep_decorator(function):
	print('sleep decorator')
	def wraper(*args, **kwargs):
		sleep(2)
		return function(*args, **kwargs)
		sleep(1)
	return wraper

@sleep_decorator
def print_number(*args,**kwargs):
	for num in args:
		sleep(1)
		print(num)
	if kwargs is not None:
		for k,v in kwargs.iteritems():
			sleep(1)
			print(k,v)
	


print(print_number('5',1,4,7,8,5,2,3,5,6,8,6,2,5,1,2,1, firstnaem='rana', lastname='sharmin'))

