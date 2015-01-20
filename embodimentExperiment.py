from naoqi import ALProxy
import time
import pyaudio
import wave

class EmbodimentExperiment:

    def __init__(self, ip_address, port = 9559, soundLocation = 'sounds/', chunkSize = 1024):
        #Load Nao Proxies
        try:
            self.tts = ALProxy("ALTextToSpeech", ip_address, port)
            self.behaviorManager = ALProxy("ALBehaviorManager", ip_address, port)
        except Exception:
            raise

        #Set sound settings
        self.soundLocation = soundLocation
        self.chunkSize = chunkSize

    def _speechForVirtualNao(self, loc):
        wf = wave.open(self.soundLocation + loc, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
        data = wf.readframes(self.chunkSize)
        while data != '':
            stream.write(data)
            data = wf.readframes(self.chunkSize)

        stream.stop_stream()
        stream.close()
        p.terminate()

    #BEHAVIORS
    def initialization(self):
            self.behaviorManager.runBehavior('mike/init')

    def close(self):
            self.behaviorManager.runBehavior('mike/close')

    #1 - Hi, how are you?
    def neutral_1(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/neutral-1')
        time.sleep(1)
        if physical:
            self.tts.say("Hi, how are you?")
        else:
            self._speechForVirtualNao('1.wav')     

    def social_1(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/social-1')
        time.sleep(1)
        if physical:
            self.tts.say("Hi, how are you?")
        else:
            self._speechForVirtualNao('1.wav') 

    #2 - What is the matter?
    def neutral_2(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/neutral-2')
        time.sleep(1)
        if physical:
            self.tts.say("What is the matter?")
        else:
            self._speechForVirtualNao('2a.wav') 
            
    def social_2(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/social-2')
        time.sleep(1)
        if physical:
            self.tts.say("Oh. What's the matter?")
        else:
            self._speechForVirtualNao('2b.wav')

    #3 - Cold outside
    def neutral_3(self, physical = True):
        if physical:
            self.tts.say("It can get quite cold indeed. Robots can not feel cold.")
        else:
            self._speechForVirtualNao('3a.wav') 
            
    def social_3(self, physical = True):
        if physical:
            self.tts.say("It can get quite cold indeed. I don't like that either.")
        else:
            self._speechForVirtualNao('3b.wav')

    #4 - Robot football  
    def neutral_4(self, physical = True):
        if physical:
            self.tts.say("Besides a better understanding of human language I want to learn new movements.")
            self.behaviorManager.post.runBehavior('mike/neutral-4')
            self.tts.say("Maybe even join the robot football team.")
            self.tts.say("Do you play a sport?")
        else:
            self._speechForVirtualNao('4_1.wav')
            self.behaviorManager.post.runBehavior('mike/neutral-4')
            self._speechForVirtualNao('4_2.wav')
            self._speechForVirtualNao('4_3.wav')
            
    def social_4(self, physical = True):
        if physical:
            self.tts.say("Besides a better understanding of human language I want to learn new movements.")
            self.behaviorManager.post.runBehavior('mike/social-4')
            self.tts.say("Maybe even join the robot football team.")
            self.tts.say("Do you play a sport?")
        else:
            self._speechForVirtualNao('4_1.wav')
            self.behaviorManager.post.runBehavior('mike/social-4')
            self._speechForVirtualNao('4_2.wav')
            self._speechForVirtualNao('4_3.wav')

    #5 - Keep fit
    def neutral_5(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/neutral-5')
        if physical:
            self.tts.say("It's good to keep fit.")
            self.tts.say("Do you have a new year's resolution?")
        else:
            self._speechForVirtualNao('5_1a.wav') 
            self._speechForVirtualNao('5_2.wav') 
            
    def social_5(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/social-5')
        if physical:
            self.tts.say("That is really good of you.")
            time.sleep(1)
            self.tts.say("Do you have a new year's resolution?")
        else:
            self._speechForVirtualNao('5_1b.wav') 
            self._speechForVirtualNao('5_2.wav')

    #6 - Theater
    def neutral_6(self, physical = True):
        if physical:
            self.tts.say("OK")
            self.tts.say("What do you want to see there?")
        else:
            self._speechForVirtualNao('6_1a.wav')
            self._speechForVirtualNao('6_2.wav') 
            
    def social_6(self, physical = True):
        if physical:
            self.tts.say("How nice of you!")
            self.tts.say("What do you want to see there?")
        else:
            self._speechForVirtualNao('6_1b.wav')
            self._speechForVirtualNao('6_2.wav')

    #7 - Comedian
    def neutral_7(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/neutral-7')
        time.sleep(1) 
        if physical:
            self.tts.say("That is nothing for me. Robots can not understand humor.")
            self.tts.say("If you tell a joke I might be able to understand it")
        else:
            self._speechForVirtualNao('7_1a.wav')
            self._speechForVirtualNao('7_2a.wav') 
            
    def social_7(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/social-7')
        time.sleep(1)
        if physical:
            self.tts.say("That sounds cool. Unfortunately robots cannot understand humor.")
            self.tts.say("Can you please tell a joke. I might be able to understand it.")
        else:
            self._speechForVirtualNao('7_1b.wav')
            self._speechForVirtualNao('7_2b.wav') 
