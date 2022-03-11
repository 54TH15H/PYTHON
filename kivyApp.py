from kivy.app import App
from kivy.uix.label import Label
class DemoApp(App):

    def build(self):
        return Label(
            text = 'Hello World...!',
            color = (1,0,0,1)
        )  

myFirstApp = DemoApp()
myFirstApp.run()