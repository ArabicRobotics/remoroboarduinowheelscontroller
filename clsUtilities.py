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

		
class MixedTools(object):
        
	def ArrayToString(self,values=[1,2,3,4]):                
			try:                        
					list1 = values
					str1 = ','.join(str(e) for e in list1)
					return str1
			except Exception as e:
					print(e)
					return False

	def convertAngleMove(self,inAngle,X,Y):
		try:
			print ("I am in _move ! ")
			values = [0,0,0,0]
			X=X* self.scale
			Y=Y*self.scale
			angle = int(inAngle)
			#if angle ==0:
			#    return values
			if angle>=0 and angle<45:
				values=[(-X)+Y,X,(-X)+Y,X]
				return self.floatToInt(values)
			if angle>=45 and angle<90:
				values = [Y-X,Y,Y-X,Y]
				return self.floatToInt(values)

			if angle>=90  and angle<135: 
				values = [Y,Y+X,Y,Y+X]
				return self.floatToInt(values)

			if angle>=135  and angle<180:

				values = [X*-1,Y+X,X*-1,Y+X]
				return self.floatToInt(values)



			if angle>=180  and angle< 225:
				values=[(X-Y)*-1,X,(X-Y)*-1,X]
				return self.floatToInt(values)



			if angle>=225  and angle<270:

				values=[Y-X,Y,Y-X,Y]
				return self.floatToInt(values)

			if angle>=270  and angle< 315:
				values=[Y,Y+X,Y,Y+X]
				return self.floatToInt(values)
			if angle>=315  and angle<=360:        
				values=[-X,X-Y,-X,X-Y]

				return self.floatToInt(values)
		except Exception as e:
			print ("Error in socket move")
			print e
			logger = clsLog()
			logger.error(str(e))
			return False


if __name__ == "__main__":
	mixedTools = MixedTools()
	print (mixedTools.ArrayToString())
