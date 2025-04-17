class InvalidInputError(Exception):
    def __init__(self,value,message="Input must be between 1 and 100"):
        self.value=value
        self.message=f"Error:{message} and you have entered {value}"
        super().__init__(self.message)
import random
guess=random.randint(1,100)#guess stores a random number given by user
count=0#counts the number of attempts u made

print("Welcome to the guessing game")
while(True):
    try:
        user_input=int(input("Enter your number:"))
        if user_input<1 or user_input>100:
            raise InvalidInputError(user_input)
        if(user_input>guess):
            print("Please try with a smaller value")
            count+=1
            continue
        elif(user_input<guess):
            print("Please try with a larger value")
            count+=1
            continue
        else:
            print("You found it congratulations!!")
            print(f"You guessed the correct answer in {count} attempts.")
            break
    except  ValueError:
        print("Please enter a valid value")
    except InvalidInputError as e:
        print(f"Dear user{e}")
    
print("thanks for playing")