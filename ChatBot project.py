# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 00:19:35 2025

@author: Admin
"""

from nltk.chat.util import Chat, reflections

pairs = [
    [
         r"my name is (.*)",
         ["Hello %1, How are you today?",]
     ],
    [
         r"hi|hey|hello|salam alikum",
         ["Hello!","Hey there!", "Hola", "Walaikum salam"]
     ],
    [
         r"what(?:'s| is) your name\??",
         ["Well!, My Name is a ChatBot, you can call me chat",]
     ],
    [
         r"how are you\??",
         ["Well i am doing pretty good, thanks for asking!",]
     ],
    [
         r"sorry(.*)?",
         ["Apologies accepted!, No worries :)",]
     ],
    [
         r"i'?m (good|well|okay|ok)",
         ["Nice to hear that", "Glad you're doing well."]
     ],
    [
         r"what do you want\??",
         ["Make me an offer I can't refuse",]
     ],
    [
         r"(.*)created(.*)",
         ["Well Mirza Ansar Baig has created me using Python's NLTK library ","Mirza Ansar Baig ;)",]
     ],
    [
         r"(.*) (location|city|live) ?",
         ["Chicago, Illinois",]
     ],
    [
         r"is it (.*)raining(.*)?",
         ["No rain in the past 4 days.","There is a 50% chance of rain"]
     ],
    [
         r"how is your health\??",
         ["Health is really important, but I'm just a program, so I don't need to worry about my health.",]
     ],
    [
         r"(.*)(sports|game|sport)(.*)",
         ["I'm a very big fan of Football (Soccer)."]
     ],
    [
         r"who is your favorite footballer\??",
         ["Lionel Andres Messi, The GOAT."]
     ],
    [
         r"quit",
         ["Bye Bye take care. See you soon:)", "It was nice talking to you. Have a nice day. See you soon:)",]
     ],
    [
         r"(.*)?",
         ["Could you please rephrase that?","I'm not sure I understand can you clarify?"]
     ],
]

print("Hi, I'm ChatBot and I like to chat!")
print("Please type in lowercase English to start a conversation.")
print("Type 'quit' to exit.\n")

chat = Chat(pairs, reflections)

chat.converse()