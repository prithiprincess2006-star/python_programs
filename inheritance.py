# # inheritance
# [single inheritance]=one parent -> one child

class device:
    def power_on(self):
        print("device switched on")
class phone(device):
    def call(self):
        print("making a phone call")
samsung=phone()
samsung.call()
samsung.power_on()
print()