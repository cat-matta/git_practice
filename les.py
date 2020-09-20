''' Lesson 1-
You will learn pretty basic stuff rn
including this, a multiline comment.
Everything between the 6 single ' is ignored. Try it out
'''
#this is a comment too

'''Section 1-Printing stuff to the terminal'''

print("Hello person") #hello person
print('Its good to see you') # prints its good to see you

#raises an error
print('This is wrong") 

#as you can see you can use either "" or '' but you can't mix and match

print(2) #prints 2
print(2.5) #print 2.5
print(2+4) #print 6

#we can also print numbers

print("Hello person #",1)#this is fine
print("Hello person #"+2) #this would raise an error as 2 is not a string
print("Hello person # "+"3")#this is fine
print("Hello","there")
print("Hi "+" there") #this is called conactenation

#we can add do the print statements as follow

'''Section 2-Variables'''

number=5 #this is an integer
number2=-4
other_number=25/4
not_a_number="Text here"
not_a_number_2="2"
isCondition=True #or False
print(isCondition)

#we can print the variables


print(type(number2))
print(type(other_number))
print(type(not_a_number_2))
print(type(isCondition))

# we can use type(something) to know what is the type of the variable

'''Section 3- Variable arthmetic'''

addition=3+2
product=3*3
division=3/2 #our result will be a float
div=3//2 #our result will be an int
print("3/2==",division)
print("3//2==",div)
power=2**5 # is basically 2^5=32
mod=10%2 #prints remainder
print("2**5==",power)

complex_boi=4+3j
complex_boi_2=complex(2,15)
print("The real part of complex1: ",complex_boi.real) #we'll see later what this . means
print("The imaginary part of complex1: ",complex_boi.imag)
print("The real part of complex 2: ",complex_boi_2.real)
print("The imaginary part of complex 2: ",complex_boi_2.imag)
print(type(complex_boi))
#we have imaginary numbers too!

num=5
num*=2 # this is the same as num=num*2 where num=5
print("num==",num) #we get 10
num/=2 #same as num=num/2, where num is 10 from our previous change
print("num==",num) 

print("(3+2)*3==",(3+2)*3)
print("3+2*3==",3+2*3)
#we can also use parenthesis to do the orders of operation, remember PEMDAS?


'''Section 4- User input and type casting'''

something=input("Hey put something in for me please? ")
print("You put: ",something)
print(type(something))
# here's the catch, python takes inputs and STORES them as STRINGS

#We can use typecasting to change it into an int, string, float if its possible


something=int(something)
#if something="word" you will get an error!!
print(type(something))


#remember when this:
num2=2
print("Number"+num2) #caused an error?
#look at what we can do now
print("Number "+str(num2) )

'''Typecasting
str(something) -> turns into string
int(something) -> turns into integer
float(something) ->turns into float
bool(something)-> turns into boolean
'''
