from zeep import Client

wsdl = 'http://www.dneonline.com/calculator.asmx?wsdl'


def add(x, y):
    client = Client(wsdl=wsdl)
    print(client.service.Add(x, y))



fnumber = input("Enter first Number")
lnumber = input("Enter Second Number")

add(fnumber, lnumber)


def subtract(x, y):
    client = Client(wsdl=wsdl)
    print(client.service.Subtract(y, x))


fnumber = input("Enter bigger number:  ")
lnumber = input("Enter smaller number :  ")

subtract(lnumber,fnumber)

