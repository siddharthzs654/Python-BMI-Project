import kivy
kivy.require('1.10.1')
 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty
 
# You can create your kv code in the Python file
# Builder.load_string("bmi-kivy.kv")
 
# Create a class for all screens in which you can include
# helpful methods specific to that screen
class HomeScreen(Screen):
    pass

class GenderScreen(Screen):
    male = ObjectProperty(True)
    female = ObjectProperty(False)
    gender = ""
    checkbox_is_active = ObjectProperty(False)
    def gender_is(self, value):
            print(value)  
            GenderScreen.gender = value
 
class HeightScreen(Screen):    
    pass

class WeightScreen(Screen):
    pass

class ResultScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass
 
class KivyTut2App(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return
 
sample_app = KivyTut2App()
sample_app.run()