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
        print("Loaded Nao")

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
        time.sleep(3)
        if physical:
            self.tts.say("Hi, how are you?")
        else:
            self._speechForVirtualNao('1.wav')     

    def social_1(self, physical = True):
        self.behaviorManager.post.runBehavior('mike/social-1')
        time.sleep(2)
        if physical:
            self.tts.say("Hi, how are you?")
        else:
            self._speechForVirtualNao('1.wav') 

    #2 - ...
