from naoqi import ALProxy
import time
import socket

class EmbodimentExperiment:

    def __init__(self, ip_address, port = 9559, soundPort = 50007):
        #Load Nao Proxies
        self.tts = ALProxy("ALTextToSpeech", ip_address, port)
        self.behaviorManager = ALProxy("ALBehaviorManager", ip_address, port)

        #Connect to PlayASoundServer
        self.playASoundSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.playASoundSocket.connect((ip_address, soundPort))

    def _playVirtualSound(self, soundName):
        self.playASoundSocket.sendall(soundName)
        self.playASoundSocket.recv(1024)

    #BEHAVIORS
    def initialization(self):
            self.behaviorManager.runBehavior('mike/init')

    def close(self):
            self.behaviorManager.runBehavior('mike/close')
            self._playVirtualSound('close')
            self.playASoundSocket.close()

    def behavior(self, trial, isPhysical, isSocial):
        if trial == 1: self.trial_1(isPhysical, isSocial)
        elif trial == 2: self.trial_2(isPhysical, isSocial)
        elif trial == 3: self.trial_3(isPhysical, isSocial)
        elif trial == 4: self.trial_4(isPhysical, isSocial)
        elif trial == 5: self.trial_5(isPhysical, isSocial)
        elif trial == 6: self.trial_6(isPhysical, isSocial)
        elif trial == 7: self.trial_7(isPhysical, isSocial)
        else: self.close()
            
    #1 - Hi, how are you?
    def trial_1(self, physical, social):
        if not social:
            self.behaviorManager.post.runBehavior('mike/neutral-1')
            time.sleep(1)
            if physical:
                self.tts.say("Hi, how are you?")
            else:
                self._playVirtualSound('1.wav')
        else:
            self.behaviorManager.post.runBehavior('mike/social-1')
            time.sleep(1)
            if physical:
                self.tts.say("Hi, how are you?")
            else:
                self._playVirtualSound('1.wav') 

    #2 - What is the matter?
    def trial_2(self, physical, social):
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
                self.tts.say("Oh. What's the matter?")
            else:
                self._playVirtualSound('2b.wav')

    #3 - Cold outside
    def trial_3(self, physical, social):
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

    #4 - Robot football  
    def trial_4(self, physical, social):
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

    #5 - Keep fit
    def trial_5(self, physical, social):
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

    #6 - Theater
    def trial_6(self, physical, social):
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

    #7 - Comedian
    def trial_7(self, physical, social):
        if not social:
            self.behaviorManager.post.runBehavior('mike/neutral-7')
            time.sleep(1) 
            if physical:
                self.tts.say("That is nothing for me. Robots can not understand humor.")
                self.tts.say("If you tell a joke I might be able to understand it")
            else:
                self._playVirtualSound('7_1a.wav')
                self._playVirtualSound('7_2a.wav')
        else:
            self.behaviorManager.post.runBehavior('mike/social-7')
            time.sleep(1)
            if physical:
                self.tts.say("That sounds cool. Unfortunately robots cannot understand humor.")
                self.tts.say("Can you please tell a joke. I might be able to understand it.")
            else:
                self._playVirtualSound('7_1b.wav')
                self._playVirtualSound('7_2b.wav') 
