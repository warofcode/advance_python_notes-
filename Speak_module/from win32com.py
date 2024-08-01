# from win32com.client import Dispatch

# def my_speak_function(string):
#     my_speak_function=Dispatch("SAPI.spVoice")
#     my_speak_function.Speak(string)

# def add (num1,num2):
#     total=num1+num2
#     return total
    
# my_speak_function("Hello ROhit I am your pc. I am ready to add two numbers")    
    
# while(True):                          # if you want to give only some chances only then use for loop with range 
#     try:
#         my_speak_function("Please enter your first number")
#         num1=int(input("Please enter your first number: "))
    
        
#         my_speak_function("Please enter your second number")
#         num2=int(input("Please enter your second number: "))
#         break
    
#     except:
#         my_speak_function("are you duffer  i told you to add number ")


# my_speak_function(f"Your total is {add(num1,num2)} ")
# print("your total is : " ,add(num1,num2))













from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")
speak.Voice = speak.GetVoices().Item(0)
speak.Speak("hi Kavya how may i help you today")


def taking_input():
    speak.Speak("Please enter your first number : ")
    input_number = int(input("Your number : "))
    
    speak.Speak("Please enter your second number : ")
    
    input_second = int(input("your second number : "))
    
    print(f"total is {input_number+input_second}")
    
    return speak.Speak(f"your total is {input_number+input_second}")

print(taking_input())