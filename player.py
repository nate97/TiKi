import vlc
import time


class TiKiPlayer:
    def __init__(self):
        print ('Started playing audio')
        # Audio file properties
        self.filename = ''
        self.audiolength = 0
        # Initialize self.player
        self.player = None
        
        
    # Set the name of the song file
    def setFileName(self, filename):
        self.filename = filename
        
    
    # Define the ending point of the song
    def setAudioLength(self, audiolength):
        self.audiolength = audiolength
        
        
    # Start the media file
    def playAudio(self):
        instance = vlc.Instance()

        #Create a MediaPlayer with the default instance
        self.player = instance.media_player_new()

        #Load the media file
        media = instance.media_new(self.filename)

        #Add the media to the player
        self.player.set_media(media)

        # Play for the length of the song then quit
        self.player.play()
        time.sleep(self.audiolength)
        
        
    # Pause audio
    def pauseAudio(self):
        pass
        
        
    # Set volume of the audio
    def setVolume(self, volume):
        pass
        
        
    # Stop playing audio
    def stopAudio(self):
        pass