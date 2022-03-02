import json
class JsonFormatter (object):
	"""This class for """ 
	def __init__(self,RequestId=None,MoreParams={}):
		"""This initilization for json formatter
		""" 
		try: 
			self.RequestId = RequestId
			self._moreParams = MoreParams
			self._dataArray = []
			self._json = None    
			return
		except Exception as e:
			print (e)
			return

	def  Add(self,name,value):
		""" Add Dict name and value to the json root directly like : gender, male"""
		try:
			self._moreParams[name]=value
			return True
		except Exception  as e:
			print ( "Error on add- json - clsutilities"+str(e))
			return False
	def Insert(self,name=None,value=None):
		""" This Method to insert a new data to the [Data Array ][Name , value ] to send with json
		@type  paramName: Bool
		@param paramName : Description
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 
			self._dataArray.append({'name':name,'value':value})
			return True
		except Exception as e:
			print (e)
			return False
	@staticmethod
	def getJsonfromString(jsonString):
		""" This Method for  
		return data as json string .

		@type  jsonString: String
		@param jsonString : string of json
		@rtype:  Boolean
		@return:  json : data as json 
		False : Something went wrong
		""" 
		try:         
			return json.loads(jsonString)

		except Exception as e:
			print(e)
			return False
	@property
	def Json(self):
		""" Add json data as json ."""
		if self.RequestId is not None:
			self._json = {
			"RequestId" : self.RequestId
			}
		if self._moreParams  is not None:
			self._json.update(self._moreParams)


		if self.DataArray is not None:
			self._json["Data"] = self._dataArray            
		return self._json
	







	
	@staticmethod
	def getData(nativeJson,name):
		""" Get value in the data array in json string"""
		if len(nativeJson) != 0:
			jsonData = json.loads(nativeJson)["Data"]
			if name == None:
				return jsonData    
			for cItem in jsonData:
				if name == cItem["name"]:
					return cItem["value"]


	@property
	def MoreParams(self):
		return self._moreParams

	@MoreParams.setter
	def MoreParams(self,value):
		self._moreParams = value

	@property
	def DataArray(self):
		"""Data inside the ."""
		return self._dataArray

	@DataArray.setter
	def DataArray(self, value):
		self._dataArray = value

def main():
	jsonObj = JsonFormatter("dfgdsfg",{'Status':'sgdsfgdsfgsdfgsdfgd'})
	jsonObj.Add('Status2','ghdfghfg')
	print (jsonObj.Json)
if __name__ == '__main__':
	main()