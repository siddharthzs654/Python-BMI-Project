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
class ScreenOne(Screen):
    male = ObjectProperty(True)
    female = ObjectProperty(False)
    
    checkbox_is_active = ObjectProperty(False)
    def gender_is(self, instance, value):
            print(value)  

 
class ScreenTwo(Screen):
    pass
 
 
# # The ScreenManager controls moving between screens
# screen_manager = ScreenManager()
 
# # Add the screens to the manager and then supply a name
# # that is used to switch screens
# screen_manager.add_widget(ScreenOne(name="screen_one"))
# screen_manager.add_widget(ScreenTwo(name="screen_two"))

class ScreenManagement(ScreenManager):
    pass
 
class KivyTut2App(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return
 
sample_app = KivyTut2App()
sample_app.run()