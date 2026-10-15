
# polymorphism many forms
# method overridding

class phone:
    def camera(self):
        print("taking a normal photo")
class smartphone:
    def camera(self):
        print("taking a potrait photo")
mi=smartphone()
mi.camera()
nokia=phone()
nokia.camera()
print()
