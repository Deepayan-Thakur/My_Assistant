import pyttsx3

me = pyttsx3.init()
rate = me.getProperty('rate')
me.setProperty('rate', rate-50)

intro = "Hello my name is Jarvis \
    Please write your name below !!!"
me.say(intro)
me.runAndWait()

name = input("Write your name please : ")

me.say("Nice to meet you!"+ name +" "+ "\
    please write someting below, so that i can speak it , and also please tell me.")
me.runAndWait()

me.say("How many times you want to say me the lines: ")
me.runAndWait()
num = int(input("Write the number of times : "))

for i in range(num):
    me.say("please write someting below")
    me.runAndWait()
    user_input = input("PLease Write >... ")
    me.say(user_input)
    me.runAndWait()