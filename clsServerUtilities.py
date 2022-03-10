from enums import *
from clsJsonFormatter import JsonFormatter
import sys
import json
class ServerUtilities(object):

    @staticmethod
    def setResult(name,value,type=enumEventType.Information,requestId=""):
        """ This Method for  
        @type  paramName: Bool
        @param paramName : Description
        @rtype:  Boolean
        @return: True : everything went fine
        False : Something went wrong
        """ 
        try: 
            #requestId = 
            formatter = JsonFormatter(requestId,)           
            formatter.Insert(name,value)
            formatter.Insert("type",type.name)
            #formatter.Insert("type","info")
            '{"op":"set","device":"robot","details":{"name": "Leds", "data": {"op": "c", "n": 1,"s":5}}}'
            result =   json.dumps (formatter.Json)
            return result
        except Exception as e:
            print (e)
            return False

def main():
    print (ServerUtilities.setResult("result",True))

if __name__ == "__main__":
    sys.exit(int(main() or 0))