import vlc
import time

class TiKiPlayer:
    def __init__(self):
        print 'Started playing audio'
        # Audio file properties
        self.filename = ''
        self.audiolength = 0
        

    def playAudio(self, filename, audiolength):
        instance = vlc.Instance()

        #Create a MediaPlayer with the default instance
        player = instance.media_player_new()

        #Load the media file
        media = instance.media_new(self.File)

        #Add the media to the player
        player.set_media(media)

        # Play for the length of the song then exit
        player.play()
        time.sleep(audiolength)