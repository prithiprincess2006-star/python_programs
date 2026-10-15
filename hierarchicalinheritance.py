# # hierarchical inheritance one parent -> multiple child

class device:
    def power_on(self):
        print("device switched on")
class phone(device):
    def call(self):
        print("making a phone call")
class computer:
    def run_program(self):
        print("running a python program")
iphone=phone()
iphone.power_on()
iphone.call()
hp=computer()
hp.power_on()
hp.run_program()
print()
