import pyttsx3

var=pyttsx3.init()
name=input("What is your name? :")
var.say(f"hello, {name}")
var.runAndWait()