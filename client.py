import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:tcp -h 127.0.0.1 -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

printer.printString("Ola Mundo!")
print(printer.maiusculas("ola do ice"))
print(printer.contaPalavras("testando para atividade de SD :)"))

if communicator:
    communicator.destroy()
