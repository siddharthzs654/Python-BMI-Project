from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition




class Home(Screen):
    pass

class Gender_Screen(Screen):
    pass

class Height_Screen(Screen):
    pass

class Weight_Screen(Screen):
    pass

class Result_Screen(Screen):
    pass



class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("support.kv")

class MainApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return presentation

MainApp().run()