from __future__ import print_function, division

class Employee(object):

	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('Delete name!')
		self.first = None
		self.last = None

emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim'
emp_1.fullname = 'Calvin Ku'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

