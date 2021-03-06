from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4, MP4Tags, error, delete
from mutagen.mp3 import MP3
from mutagen import File
import mutagen

from audiofile import TiKiFile
from player import TiKiPlayer


import vlc
import time
import glob, os

cwd = os.getcwd()

class TiKiMediaPlayer:

    def __init__(self):
        print ('Tiki Music Player')

        self.searchDirectory()
        self.sortAudio()

        print (self.allMusic['02.mp3'])


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
            audioFile = TiKiFile()
            audioFile.setFilename(filename)
            audioFile.setMetaData()

            artist = audioFile.getArtist()

            title = audioFile.getTitle()

            album = audioFile.getAlbum()

            tracknumber = audioFile.getTracknumber()

            genre = audioFile.getGenre()

            date = audioFile.getDate()
            
            audiolength = audioFile.audioLength

            temp = {
                'artist':artist,
                'title':title,
                'album':album,
                'tracknumber':tracknumber,
                'genre':genre,
                'date':date,
                'audiolength':audiolength,
                }

            # Update music dictionary
            self.allMusic.update({filename:temp})

            # temp
            #player = TiKiPlayer()
            #player.playAudio(filename, audiolength)


TiKiMediaPlayer()