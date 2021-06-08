import pyttsx3                  #This is necessary to install first

#-------------------------------------------------------------------------------------------------

me = pyttsx3.init()                       #
rate = me.getProperty('rate')             # This is to make the speech little bit slow 
me.setProperty('rate', rate-50)           # 

#-------------------------------------------------------------------------------------------------

intro = "Hello my name is Jarvis \
    Please write your name below !!!"                       #This is only for saying
me.say(intro)
me.runAndWait()

#-------------------------------------------------------------------------------------------------

name = input("Write your name please : ")                           # This is for the user to input name

#-------------------------------------------------------------------------------------------------

me.say("Nice to meet you!"+ name +" "+ "\
    please write someting below, so that i can speak it , and also please tell me.")                    #This is only for saying
me.runAndWait()

#-------------------------------------------------------------------------------------------------

me.say("How many times you want to say me the lines: ")
me.runAndWait()                                                                     #This is only for saying

#-------------------------------------------------------------------------------------------------

num = int(input("Write the number of times : "))                # This is how many times you write sentences

#-------------------------------------------------------------------------------------------------

for i in range(num):
    me.say("please write someting below")                               #This is only for saying
    me.runAndWait()
    user_input = input("PLease Write >... ")
    me.say(user_input)
    me.runAndWait()
#-------------------------------------- Thank you -----------------------------------------------------------
