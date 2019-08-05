# greeting = input('What is your greeting? ')
# print(greeting)
# age = input('What is your age? ')
# if age is type(int):
# new_age = 0	
try:
	new_age = int(age) + 50
	print(age)
	print(new_age)
except Exception as e:
	print("You need to enter a number for your age!")

exp = 20 - 10 / 5 * 3 ** 2
print(exp)

hw = 'hi there'
hw_replace = hw.replace('e', 'i')
print(hw_replace)
print(hw.upper())

hw[1] # i
hw[:2] # hi
hw[-1] # e

l = ["hello", 20, "my friend!"]
l.count(20) # 1

emails = ['darren@gmail.com', 'darren@hotmail.com', 'darren@yahoo.com']
for email in emails:
	if 'gmail' in email:
		print(email)

names = ['Darren Jensen', 'Nerrad Nesnej', 'Professor Hydrocarb']
for name, email in zip(names, emails):
	print("{} has email address {}.".format(name, email))

file=open('example.txt', 'r')
print(file.read()) # File contents output
print(file.read()) # ''
file.seek(0)
content = file.readlines()
print(content) # File contents output one line per array element
content = [i.rstrip('\n') for i in content]
print(content) # Same as above with the new line character removed
file.close()

filew=open('newexample.txt', 'w') # 'w' is write mode, use 'a' to append
filew.write('Line 1\n')
filew.write('Line 2')
filew.close()

# other modes are
# r+ open for reading and writing to the START of the file without replacing the file
# w+ open for reading and writing and will replace file
# a+ open for reading and writing to the END of the file without replacing the file

with open('example.txt', 'a+') as file:
	content=file.read()
	file.write('\nhello!')

print(content)


