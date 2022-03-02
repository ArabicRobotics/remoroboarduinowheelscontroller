import json
import time
class switch(object):
	value = ""
	def __new__(class_, value):
		class_.value = value
		return True

class enumItem(object):
	def __init__(self,name,value,shortDescription):
		self.name = name
		self.value = value
		self.description = shortDescription