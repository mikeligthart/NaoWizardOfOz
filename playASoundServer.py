import socket
import pyaudio
import wave

class PlayASoundServer(object):

    def __init__(self, port = 50007, listners = 1, soundLocation = 'sounds/'):
        print 'Starting server'
        self.soundLocation = soundLocation
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(('', port))
        serverSocket.listen(listners)
        try:
            self.conn, self.addr = serverSocket.accept()
            print 'Connected by ', self.addr
            self.active = True
            self.playIncommingSounds()
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except Exception as e:
            print 'An error occured:\n' + e
        finally:
            self.close(True)

    def _speechForVirtualNao(self, loc):
        wf = wave.open(self.soundLocation + loc, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
        data = wf.readframes(1024)
        while data != '':
            stream.write(data)
            data = wf.readframes(1024)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def playIncommingSounds(self):
        while self.active:
            soundFileName = self.conn.recv(1024)
            if soundFileName == 'close':
                self.active = False
            elif soundFileName != '':
                print 'play ' + soundFileName
                self._speechForVirtualNao(soundFileName)
            self.conn.send(soundFileName)
        self.close(True)

    def close(self, force = False):
        self.active = False
        if force:
            self.conn.close()
        print 'Server closed'
        

if __name__ == "__main__":
    server = PlayASoundServer()

    
