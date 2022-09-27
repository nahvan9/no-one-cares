from mvc.model import AppModel
from mvc.view import AppView

class AppController():
    def __init__(self):
        self.model = AppModel()
        self.view = AppView()
        
        self.set_commands()
        self.view.mainloop()

    def set_commands(self):
        pass
    