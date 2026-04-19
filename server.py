import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"

    def maiusculas(self, s, current=None):
        return s.upper()

    def contaPalavras(self, s, current=None):
        return len(s.split())

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
adapter.add(object, Ice.stringToIdentity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()
