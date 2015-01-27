# -*- coding: cp1252 -*-
from naoqi import ALProxy
import time
import socket

class EmbodimentExperiment:

    def __init__(self, ip_address, port = 9559):
        #Load Nao Proxies
        self.tts = ALProxy("ALTextToSpeech", ip_address, port)
        self.behaviorManager = ALProxy("ALBehaviorManager", ip_address, port)

    def connectToPlayASoundServer(self, ip_address, soundPort = 50007):
        self.playASoundSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.playASoundSocket.connect((ip_address, soundPort))

    def _playVirtualSound(self, soundName):
        self.playASoundSocket.sendall(soundName)
        self.playASoundSocket.recv(1024)

    #BEHAVIORS
    def initialization(self):
        self.behaviorManager.runBehavior('mike/init')

    def close(self, isPhysical):
        self.behaviorManager.runBehavior('mike/close')
        if not isPhysical:
            self._playVirtualSound('close')
            self.playASoundSocket.close()

    def offScript(self, isPhysical):
        if isPhysical:
            self.tts.say("I'm sorry I did not quite get that. Could you go back to the script so that I can improve my speech recognition even more?")
        else:
            self._playVirtualSound('offScript.wav')

    def behavior(self, trial, isPhysical, isSocial):
        if trial == 1: self.trial_1(isPhysical, isSocial)
        elif trial == 2: self.trial_2(isPhysical, isSocial)
        elif trial == 3: self.trial_3(isPhysical, isSocial)
        elif trial == 4: self.trial_4(isPhysical, isSocial)
        elif trial == 5: self.trial_5(isPhysical, isSocial)
        elif trial == 6: self.trial_6(isPhysical, isSocial)
        elif trial == 7: self.trial_7(isPhysical, isSocial)
        elif trial == 8: self.trial_8(isPhysical, isSocial)
        elif trial == 9: self.trial_9(isPhysical, isSocial)
        elif trial == 10: self.trial_10(isPhysical, isSocial)
        elif trial == 11: self.trial_11(isPhysical, isSocial)
        elif trial == 12: self.trial_12(isPhysical, isSocial)
        elif trial == 13: self.trial_13(isPhysical, isSocial)
        elif trial == 14: self.trial_14(isPhysical, isSocial)
        elif trial == 15: self.trial_15(isPhysical, isSocial)
        elif trial == 16: self.trial_16(isPhysical, isSocial)
        else: self.close()

    def trial_1(self, physical, social):
        if not social:
            self.behaviorManager.post.runBehavior('mike/neutral-1')
            time.sleep(1)
            if physical:
                self.tts.say("Hi.")
                time.sleep(1)
                self.tts.say("Let's start the converstation. What is your name?")
            else:
                self._playVirtualSound('1.wav')
                time.sleep(1)
                self._playVirtualSound('1_2a.wav')
        else:
            self.behaviorManager.post.runBehavior('mike/social-1')
            time.sleep(1)
            if physical:
                self.tts.say("Hi")
                time.sleep(1)
                self.tts.say("I'm looking forward to having a conversation with you. What is your name?")
            else:
                self._playVirtualSound('1.wav')
                time.sleep(1)
                self._playVirtualSound('1_2b.wav')
            
    def trial_2(self, physical, social):
        if not social:
            if physical:
                self.tts.say("How are you?")
            else:
                self._playVirtualSound('1_3.wav')
        else:
            self.behaviorManager.post.runBehavior('mike/neutral-4')
            time.sleep(1)
            if physical:
                self.tts.say("How are you?")
            else:
                self._playVirtualSound('1_3.wav') 

    def trial_3(self, physical, social):
        if not social:
            self.behaviorManager.post.runBehavior('mike/neutral-2')
            time.sleep(1)
            if physical:
                self.tts.say("What is the matter?")
            else:
                self._playVirtualSound('2a.wav')
        else:
            self.behaviorManager.post.runBehavior('mike/social-2')
            time.sleep(1)
            if physical:
                self.tts.say("Aah. What's the matter?")
            else:
                self._playVirtualSound('2b.wav')

    def trial_4(self, physical, social):
        if not social:
            if physical:
                self.tts.say("It can get quite cold indeed. Robots can not feel cold.")
            else:
                self._playVirtualSound('3a.wav')
        else:            
            if physical:
                self.tts.say("It can get quite cold indeed. I don't like that either.")
            else:
                self._playVirtualSound('3b.wav')
 
    def trial_5(self, physical, social):
        if not social:
            if physical:
                self.tts.say("Besides a better understanding of human language I want to learn new movements.")
                self.behaviorManager.post.runBehavior('mike/neutral-4')
                self.tts.say("Maybe even join the robot football team.")
                self.tts.say("Do you play a sport?")
            else:
                self._playVirtualSound('4_1.wav')
                self.behaviorManager.post.runBehavior('mike/neutral-4')
                self._playVirtualSound('4_2.wav')
                self._playVirtualSound('4_3.wav')
        else:
            if physical:
                self.tts.say("Besides a better understanding of human language I want to learn new movements.")
                self.behaviorManager.post.runBehavior('mike/social-4')
                self.tts.say("Maybe even join the robot football team.")
                self.tts.say("Do you play a sport?")
            else:
                self._playVirtualSound('4_1.wav')
                self.behaviorManager.post.runBehavior('mike/social-4')
                self._playVirtualSound('4_2.wav')
                self._playVirtualSound('4_3.wav')

    def trial_6(self, physical, social):
        if not social:
            self.behaviorManager.post.runBehavior('mike/neutral-5')
            if physical:
                self.tts.say("It's good to keep fit.")
                self.tts.say("Do you have a new year's resolution?")
            else:
                self._playVirtualSound('5_1a.wav')
                self._playVirtualSound('5_2.wav')
        else:
            self.behaviorManager.post.runBehavior('mike/social-5')
            if physical:
                self.tts.say("That is really good of you.")
                time.sleep(1)
                self.tts.say("Do you have a new year's resolution?")
            else:
                self._playVirtualSound('5_1b.wav') 
                self._playVirtualSound('5_2.wav')

    def trial_7(self, physical, social):
        if not social:
            if physical:
                self.tts.say("OK")
                self.tts.say("What do you want to see there?")
            else:
                self._playVirtualSound('6_1a.wav')
                self._playVirtualSound('6_2.wav') 
        else:
            if physical:
                self.tts.say("How nice of you!")
                self.tts.say("What do you want to see there?")
            else:
                self._playVirtualSound('6_1b.wav')
                self._playVirtualSound('6_2.wav')

    def trial_8(self, physical, social):
        if not social:
            self.behaviorManager.post.runBehavior('mike/neutral-7')
            time.sleep(1) 
            if physical:
                self.tts.say("That is nothing for me. Robots can not understand humor.")
                self.tts.say("If you tell a joke I might be able to learn how to understand it")
            else:
                self._playVirtualSound('7_1a.wav')
                self._playVirtualSound('7_2a.wav')
        else:
            self.behaviorManager.post.runBehavior('mike/social-7')
            time.sleep(1)
            if physical:
                self.tts.say("That sounds cool. Unfortunately robots cannot understand humor.")
                self.tts.say("Can you please tell a joke. I might be able to learn how to understand it.")
            else:
                self._playVirtualSound('7_1b.wav')
                self._playVirtualSound('7_2b.wav')

    def trial_9(self, physical, social):
        if not social:
            if physical:
                self.tts.say("Haha")
                self.tts.say("I have one to. Fool me once, shame on you. Fool me twice, shame on me. Fool me three hundred fifty thousand times, you are a weatherman.")
            else:
                self._playVirtualSound('8_1a.wav')
                self._playVirtualSound('8_2.wav')
        else:
            self.behaviorManager.post.runBehavior('mike/social-8')
            if physical:
                time.sleep(3)
                self.tts.say("I have one to. Fool me once, shame on you. Fool me twice, shame on me. Fool me three hundred fifty thousand times, you are a weatherman.")
            else:
                time.sleep(1)
                self._playVirtualSound('8_1b.wav')
                time.sleep(2)
                self._playVirtualSound('8_2.wav')

    def trial_10(self, physical, social):
        if not social:
            if physical:
                self.tts.say("Maybe I should become an actor like Benedict Cumberbatch. He plays Alan Turing in the imitation game.")
                self.tts.say("Do you know that movie?")
            else:
                self._playVirtualSound('9_2a.wav')
                self._playVirtualSound('9_3.wav')
        else:
            self.behaviorManager.post.runBehavior('mike/social-9')
            if physical:
                time.sleep(3)
                self.tts.say("Maybe I should become an actor like Benedict Cumberbatch. He plays my hero, Alan Turing, in the imitation game.")
                self.tts.say("Do you know that movie?")
            else:
                time.sleep(1)
                self._playVirtualSound('9_1b.wav')
                time.sleep(2)
                self._playVirtualSound('9_2b.wav')
                self._playVirtualSound('9_3.wav')

    def trial_11(self, physical, social):
        if not social:
            self.behaviorManager.post.runBehavior('mike/neutral-4')
            if physical:
                self.tts.say("Yeah I hope so!")
                self.tts.say("What is your favorite movie for the Oscars this year? ")
            else:
                self._playVirtualSound('10_1a.wav')
                self._playVirtualSound('10_2.wav')
        else:
            self.behaviorManager.post.runBehavior('mike/social-4')
            if physical:
                self.tts.say("Yeah let us hope so!")
                self.tts.say("What is your favorite movie for the Oscars this year?")
            else:
                self._playVirtualSound('10_1b.wav')
                self._playVirtualSound('10_2.wav')

    def trial_12(self, physical, social):
        if not social:
            if physical:
                self.tts.say("I only need electricity to function. So I can get hungry sometimes. I heard humans when hungry can go like this: ")
                self.behaviorManager.post.runBehavior('mike/neutral-11')
                time.sleep(2)
                self.tts.say("Is that true?")
            else:
                self._playVirtualSound('11_1a.wav')
                self._playVirtualSound('11_2.wav')
                self._playVirtualSound('11_3.wav')
        else:
            if physical:
                self.tts.say("Good question! I only need electricity to function. So I can get hungry sometimes. I heard humans when hungry can behave like this: ")
                self.behaviorManager.post.runBehavior('mike/social-11')
                time.sleep(4)
                self.tts.say("Is that true?")
            else:
                self._playVirtualSound('11_1b.wav')
                self.behaviorManager.post.runBehavior('mike/social-11')
                self._playVirtualSound('11_2.wav')
                self._playVirtualSound('11_3.wav')

    def trial_13(self, physical, social):
        pass
    def trial_14(self, physical, social):
        pass
    def trial_15(self, physical, social):
        pass
    def trial_16(self, physical, social):
        pass
