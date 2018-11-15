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
rbc = ""
wbc = ""
hb = ""
platelets = ""
report = ""
    
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

class OptionalScreen(Screen):
    def getWbc(self, wbcInput):
        global wbc, age
        try:
            wbc = int(wbcInput)
        except:
            popup = Popup(title='Error',
                    content=Label(text='WBC can only contain numbers' ),
                    size_hint=(None, None), size=(400, 100))
            popup.open()

        if(age == 0):
            if(wbc<9000):
                wbc="Low"
            elif(wbc<30000):
                wbc="Normal"
            else:
                wbc="High"
        elif(age < 2):
            if(wbc<6200):
                wbc="Low"
            elif(wbc<17000):
                wbc="Normal"
            else:
                wbc="High"
        if(age >=2):
            if(wbc<5000):
                wbc="Low"
            elif(wbc<10000):
                wbc="Normal"
            else:
                wbc="High"

    def getPlatelets(self, plInput):
        global platelets
        try:
            platelets = int(plInput)
        except:
            popup = Popup(title='Error',
                    content=Label(text='WBC can only contain numbers' ),
                    size_hint=(None, None), size=(400, 100))
            popup.open()

        if(platelets<150000):
            platelets = "Low"
        elif(platelets<450000):
            platelets = "Normal"
        else:
            platelets = "High"
            
    def result(self, rbcIN, hbIN):
        global rbc, wbc, hb, platelets, g
        rbc = float(rbcIN)
        hb = float(hbIN)
        # RBC CALCULATIONS
        if(g == "male"):
            if(rbc<4.7):
                rbc="Low"
            elif(rbc<6.1):
                rbc="Normal"
            else:
                rbc="High"
        elif(g == "female"):
            if(rbc<4.2):
                rbc="Low"
            elif(rbc<5.4):
                rbc="Normal"
            else:
                rbc="High"

        # HB CALCULATIONS
        if(g == "male"):
            if(hb<13.5):
                hb="Low"
            elif(hb<17.5):
                hb="Normal"
            else:
                hb="High"
        elif(g == "female"):
            if(hb<12.0):
                hb="Low"
            elif(hb<15.5):
                hb="Normal"
            else:
                hb="High"
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
        print(label)
        gf.graphs(h,w)

        # Making the report

        global report
        report = "Dear "+name+"\nYou are "+str(ResultScreen.category) + " with " + str(r)+"."
        if(rbc != ""):
            report+= "\nYour RBC count is " + rbc
        if(wbc != ""):
            report+= "\nYour WBC count is " + wbc
        if(hb != ""):
            report+= "\nYour Hemoglobin is " + hb
        if(platelets != ""):
            report+= "\nYour platelets count is " + platelets
        label.text = report

    pass

class ScreenManagement(ScreenManager):
    pass
 
class KivyFITNESSApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return
 
sample_app = KivyTut2App()
sample_app.run()