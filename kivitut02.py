import kivy
kivy.require('1.10.1')
 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
 


import Graph as gf
# You can create your kv code in the Python file
# Builder.load_string("bmi-kivy.kv")
 
# Create a class for all screens in which you can include
# helpful methods specific to that screen
w = 0
h = 1
g = ""
r = 0
    
class HomeScreen(Screen):
    pass

class GenderScreen(Screen):
    male = ObjectProperty(True)
    female = ObjectProperty(False)
    gender = ""
    checkbox_is_active = ObjectProperty(False)
    def gender_is(self, value):
        self.g = value 
        GenderScreen.gender = value
        global g
        g = str(value)
 
class HeightScreen(Screen):  
    def heightValue(self, height):
        global h
        h = float(height)/100
    pass

class WeightScreen(Screen):
    def weightValue(self, weight):
        global w
        w = int(weight)
    
    pass

class ResultScreen(Screen):
    gf.graphs(h,w)    # Create a image of graph with name graphpic.png, Now display as you want
    bmi = float(0)
    def calculateBMI(self, label):
        r = float(w/(h**2))
        ResultScreen.bmi = r
        label.text = str(r)
        print(label)
        # print(self)
        # calculated_bmi.text = str("Hello")
        # return (r)
    pass

class ScreenManagement(ScreenManager):
    pass
 
class KivyTut2App(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return
 
sample_app = KivyTut2App()
sample_app.run()