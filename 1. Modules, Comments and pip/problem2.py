#install an external module and use it to perform an operation of your interest
import pyttsx3  #intalled by: pip install pyttsx3
engine = pyttsx3.init()
engine.say("bring a friend, join the crowd, whoever wanna come along")
engine.runAndWait()