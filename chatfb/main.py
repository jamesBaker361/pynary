# -*- coding: utf-8 -*-

import unirest
from appJar import gui
import csv
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterboi=ChatBot("Lil Pump")

chatterboi.set_trainer(ChatterBotCorpusTrainer)

chatterboi.train(
    "chatterbot.corpus.english"
)

def newHumanMessage(text):
	app.setLabel("humanTalk",app.getEntry("input"))
	response = chatterboi.get_response(app.getEntry("input"))
	print(response)
	app.setLabel("machineTalk",response)
	app.setEntry("input","")


app=gui()
app.setTitle("JamesBot")
app.setGeometry(400,400)
app.setFg("blue")
app.setBg("white")
app.addLabel("secret","",15,15)

app.addLabel("machineTalk","Hello!",3,0)
app.addLabel("humanTalk","", 6,10,5,1)
app.addEntry("input",20,0,15)
app.setEntryFunc("input",newHumanMessage)

app.go()