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

		
class mixedTools(object):
        classmethod
        def ArrayToString(values=[1,2,3,4]):                
                try:                        
                        list1 = values
                        str1 = ','.join(str(e) for e in list1)
                        return str1
                except Exception as e:
                        print(e)
                        return False

if __name__ == "__main__":
	print (mixedTools.ArrayToString())
