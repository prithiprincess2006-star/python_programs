# # multiple inheritance - father - mother - child

class camera:
    def take_photo(self):
        print("taking a photo")
class musicplayer:
    def playmusic(self):
        print("playing music")
class smartphone:
    def call(self):
        print("making a phone call")
mi=smartphone()
mi.playmusic()
mi.take_photo()
mi.call()
print()