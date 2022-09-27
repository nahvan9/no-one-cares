

class AppModel():
    def __init__(self, input, output='', option=0):
        self.input = input
        self.output = output
        self.option = option

    def convertInput(self):
        stringArray = self.input.lower().split(' ')
        return stringArray

    def option1(self, array):
        for word in array:
            x = len(word)


    def checkLower(self, letter):
        if letter == letter.lower():
            return True
        else:
            return False
        
app = AppModel('Hello World How are You?')
print(app.convertInput())
print(app.checkLower('?'))
print(app.checkLower('A'))