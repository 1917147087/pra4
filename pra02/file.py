name=str(input('Enter your name: '))
out_file = open('name.txt', 'w')
out_file.write(name)
print('Your name is',name)
out_file.close()

out_file = open('name.txt', 'r')
name=out_file.read()
print('Your name is',name)
out_file.close()

open_file=open('numbers.txt', 'r')
num1=int(open_file.readline())
num2=int(open_file.readline())
sum=num1+num2
print(sum)
open_file.close()

open_file=open('numbers.txt', 'r')
sum=0
for line in open_file:
    num=int(line)
    sum=sum+num
print(sum)
open_file.close()

