from __future__ import print_function, division
from functools import wraps

class decorator_class(object):
	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print("call method executed this before {}".format(self.original_function.__name__))
		return self.original_function(*args, **kwargs)

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print("wrapper executed this before {}".format(original_function.__name__))

	return wrapper_function

def my_logger(orig_func):
	import logging
	logging.basicConfig(filename="{}.log".format(orig_func.__name__), level=logging.INFO)

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))

		return orig_func(*args, **kwargs)

	return wrapper

def my_timer(orig_func):
	import time

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orig_func(*args, **kwargs)

		t2 = time.time() - t1
		print("{} ran in: {} sec".format(orig_func.__name__, t2))

		return result

	return wrapper


# @decorator_class
@decorator_function
def display():
	print("display function ran.")

import time

@my_logger
@my_timer
def display_info(name, age):
	time.sleep(1)
	print("display_info ran with arguments ({}, {})".format(name, age))


if __name__ == '__main__':
	# display()
	# display_info("John", 25)
	display_info("Picard", 68)

	# display_info = my_timer(display_info)
	# print(display_info.__name__)