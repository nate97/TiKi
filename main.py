from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4, MP4Tags, error, delete
from mutagen.mp3 import MP3
from mutagen import File
import mutagen

from audio import AudioFileObject

import vlc
import time
import glob, os


cwd = os.getcwd()



class TiKiMediaPlayer:

    def __init__(self):
        print ('Tiki Media')

        self.searchDirectory()
        self.sortAudio()


        #self.playAudio()



    # Search directory for all supported file types
    def searchDirectory(self):
        types = ('*.mp3', '*.mp4', '*.m4a', '*.flac')
        
        os.chdir(cwd)
    
        self.directory = []
        for files in types:
            self.directory.extend(glob.glob(files))
        
        # Sort this basic folder playlist by name
        self.directory.sort()
        


    def sortAudio(self):
        
        self.allMusic = {}
        
        for filename in self.directory:      
            print (filename)
            audioFile = AudioFileObject()
            audioFile.setFilename(filename)
            audioFile.setMetaData()

            artist = audioFile.getArtist()

            title = audioFile.getTitle()

            album = audioFile.getAlbum()

            tracknumber = audioFile.getTracknumber()

            genre = audioFile.getGenre()

            date = audioFile.getDate()
            
            audiolength = audioFile.audioLength


    def playAudio(self):
        instance = vlc.Instance()

        #Create a MediaPlayer with the default instance
        player = instance.media_player_new()

        #Load the media file
        media = instance.media_new(self.File)

        #Add the media to the player
        player.set_media(media)

        #Play for the length of the song then exit
        player.play()
        time.sleep(self.audioLength)



TiKiMediaPlayer()