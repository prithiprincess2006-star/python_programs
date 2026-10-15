class student:
    name="unknown"
    mark=0
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def setdetails (self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print("name: ",self.name)
        print("mark: ",self.mark)
