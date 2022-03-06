i=1
while i<=10:
    print(i)
    i += 1

num3=50
num4=100
if(num3==num4):
    print(num4)
elif (num3>num4):
    print(num3)
else:
    print (num3+num4)

Dic={'name': 'Ahmed',
     'country': 'Egypt',
     'age': 38,
     'frindes': ['Mohamed','Mostafa','Sameh']
    }
print(Dic['name'])

def SumNumbers():
    num1=10
    num2=30
    res=num1+num2
    print(res)
    return res-20


#tt=(1,2,3,True,'Home')

#print(tt)

#print(SumNumbers())

def Welcome(*names):
    print('Welcome '+names[1])

#Welcome('Ahmed','Mohamed','Ali')
try:
    x=50/5
except:
    print('error divide by zero')
else:
    print('True')
finally:
    print('Good')

ColorsFile=open("G:\\Python\\Colors.txt")

for Color in ColorsFile.readlines():
    print(Color)
ColorsFile.close()

TimesFile=open("G:\\Python\\Times.txt","a")
TimesFile.write("ELMAGREB")
TimesFile.close()
#4:14

