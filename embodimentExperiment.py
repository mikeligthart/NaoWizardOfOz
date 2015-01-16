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
        except Exception,e:
            print "Could not create proxies"
            print "Error was: ",e
            sys.exit(1)

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
        data = wf.readframes(chunk)
        while data != '':
            stream.write(data)
            data = wf.readframes(chunk)

        stream.stop_stream()
        stream.close()
        p.terminate()

    #BEHAVIORS
    def initialization(self, physical = True):
        if physical:
            self.behaviorManager.runBehavior('mike/init')

    def close(self, physical = True):
        if physical:
            self.behaviorManager.runBehavior('mike/close')

    #1 - Hi, how are you?
    def neutral_1(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/1-neutral')
        time.sleep(3)
        if physical:
            self.tts.say("Hi, how are you?")
        else:
            self._speechForVirtualNao('1.wav')     

    def social_1(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/1-social')
        time.sleep(2)
        if physical:
            self.tts.say("Hi, how are you?")
        else:
            self._speechForVirtualNao('1.wav') 

    #2 - ...
