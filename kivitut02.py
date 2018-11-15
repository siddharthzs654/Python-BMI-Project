import kivy
kivy.require('1.10.1')
 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import Graph as gf

w = 0
h = 1
g = ""
r = 0
name = ""
age = ""
    
class HomeScreen(Screen):
    def validateName(self, nameInput):
        global name
        name = nameInput
        print(name)
        if(name == ""):
            popup = Popup(title='Error',
                    content=Label(text='Name can\'t be empty' ),
                    size_hint=(None, None), size=(400, 100))
            popup.open()

    def validateAge(self, ageInput):
        global age
        
        if(ageInput == ""):
            popup = Popup(title='Error',
                    content=Label(text='Age can\'t be empty' ),
                    size_hint=(None, None), size=(400, 100))
            popup.open()
        else:
            try:
                age = int(ageInput)
            except:
                popup = Popup(title='Error',
                        content=Label(text='Age can only contain numbers' ),
                        size_hint=(None, None), size=(400, 100))
                popup.open()

    def shouldGo(self):
        print("hello")
        global age, name
        if(age == "" or name == ""):
            HomeScreen.errorMsg()
            return False
        else:
            return True

    def errorMsg():
        print("hey")
        popup = Popup(title='Error',
                content=Label(text='Fill All the values' ),
                size_hint=(None, None), size=(400, 100))
        popup.open()
        
    pass

class GenderScreen(Screen):
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
        print(h)
    pass

class WeightScreen(Screen):
    def weightValue(self, weight):
        global w
        w = int(weight)
        print(w)
    
    pass

class ResultScreen(Screen):
    #gf.graphs(h,w)    # Create a image of graph with name graphpic.png, Now display as you want
    bmi = float(0)
    category = " "
    def calculateBMI(self, label):
        r = float(w/(h**2))
        r = round(r,2)
        ResultScreen.bmi = r
        if (ResultScreen.bmi <=18.5):
            ResultScreen.category = "Under Weight"
        elif (ResultScreen.bmi <=24.9):
            ResultScreen.category = "Normal Weight"
        elif (ResultScreen.bmi <=29.9):
            ResultScreen.category = "Over Weight"
        else:
            ResultScreen.category = "Obese"
        label.text = str(ResultScreen.category) + " with " + str(r)
        print(label)
        gf.graphs(h,w)

    pass

class OptionalScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass
 
class KivyTut2App(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return
 
sample_app = KivyTut2App()
sample_app.run()