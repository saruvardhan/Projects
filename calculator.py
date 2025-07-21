def add(n1,n2):
      return n1+n2
def subract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
res=''

operators = {
      "+": add,
      "-": subract,
      "*": multiply,
      "/": divide,
}
start= True
n1 =float(input('ENTER THE FIRST NUMBER THAT YOU WANT TO CALCULATE WITH: '))
while start:
    
    for symbol in operators:
          print(symbol)
    sym=input('enter the operator: ')
    n2=float(input('ENTER THE LAST NUBER YOU WANT TO CALCULATE: '))
    res = operators[sym](n1,n2)
    print(f"{n1} {sym} {n2}={res}")
    op= input(f'Type (y) to calculate with {res} and (n) to start new one: ').lower()
    if op == 'y':
          n1=res      
    else:
          n1 =float(input('ENTER THE FIRST NUMBER THAT YOU WANT TO CALCULATE WITH: '))
