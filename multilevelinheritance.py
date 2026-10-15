
# #multilevel inheritance grandparent ->parent-> child

class device:
    def power_on(self):
        print("device switched on")
class computer(device):
    def run_program(self):
        print("running a python program")
class laptop(computer):
    def charge(self):
        print("laptop battery charging")
asus=laptop()
asus.power_on()
asus.run_program()
asus.charge()
print()