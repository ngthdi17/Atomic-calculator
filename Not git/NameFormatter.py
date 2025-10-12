firstname = str(input("Enter your first name: "))
lastname = str(input("Enter your last name: "))
fullname = firstname + " " + lastname
print('Hi' , fullname.upper() , ' ,your name has' , len(fullname) , 'letters, and it start with' , firstname[0])
print(f'The last letter of your first name is {firstname[-1]}')
print(f'The first 3 letters of the full name is {fullname[0:3]}')
print(f'The reverse version of your full name is {fullname[::-1]}')
if firstname[0] == 'a,A,e,E,i,I,o,O,u,U':
    print('Your first name starts with a vowel,' , firstname[0])
else:
    print('Your first name starts with a consonant,' , firstname[0])
print(f'{lastname.lower()} {firstname.upper()}')
print(f'The amount of "a"s in your name is {fullname.count("a,A")}')