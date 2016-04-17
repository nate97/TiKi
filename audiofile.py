from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4, MP4Tags, error, delete
from mutagen.mp3 import MP3
import mutagen

# We're treating every audio file as an individual object
class TiKiFile:

    def __init__(self):
        print ('Opened music file')
        ### Object globals ###
        self.fileName = ''
        # Audio METADATA
        self.artist = ''
        self.title = ''
        self.album = ''
        self.tracknumber = ''
        self.genre = ''
        self.date = ''
        # Audio file properties
        self.audioLength = 0


    # Define current file we're using
    def setFilename(self, filename):
        self.fileName = filename


    # Define all the avalible metadata for the current object
    def setMetaData(self):
        # Extract basic metadata out of any file by using easy
        metadata = mutagen.File(self.fileName, easy=True)
        
        ######### METADATA #########
        try:
            self.artist = metadata['artist']
        except:pass
        
        try:
            self.title = metadata['title']
        except:passr
        
        try:
            self.album = metadata['album']
        except:pass
        
        try:
            self.tracknumber = metadata['tracknumber']
        except:pass
        
        try:
            self.genre = metadata['genre']
        except:pass
        
        try:
            self.dat = metadata['date']
        except:pass
        ######### METADATA #########
        
        # Audio properties
        self.audioLength = metadata.info.length


    def getArtist(self):
        return self.artist


    def getTitle(self):
        return self.title


    def getAlbum(self):
        return self.album


    def getTracknumber(self):
        return self.tracknumber


    def getGenre(self):
        return self.genre


    def getDate(self):
        return self.date


    def getAudioLength(self):
        return self.audioLength
