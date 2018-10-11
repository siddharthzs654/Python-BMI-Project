import kivy
kivy.require('1.10.1')
 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty
 
# You can create your kv code in the Python file
Builder.load_string("""
#: import CheckBox kivy.uix.checkbox
<CustLabel@Label>:
    color: 0, 0, 0, 1

<CustCheckBox@CheckBox>:
    _radio_state_image:
        self.background_radio_normal
    canvas:
        Rectangle:
            source: self._radio_state_image
            size: sp(200), sp(300)
            pos: int(self.center_x - sp(100)), int(self.center_y - sp(150))

<ScreenOne>:
    BoxLayout:
        orientation: "vertical"

        BoxLayout:
            orientation: "vertical"
            size_hint_y: 0.8
            spacing:10
            
            CustLabel:
                text: str("BODY MASS INDEX")
                color: 0,0,0,1
                size_hint_y: 0.1
                font_size : 50
 
            CustLabel:
                text: str("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
                color: 0,0,0,1
                size_hint_y: 0.1
            
            CustLabel:
                text: "Gender"
                color: 0, 0, 0, 1
                size_hint_y: 0.1

            BoxLayout:
                orientation: "horizontal"
                size_hint_y: 0.7
                spacing:10
                CustCheckBox:
                    on_active: root.gender_is(self, self.value)
                    background_radio_normal : "5b3744081107e16378fe66a7c97b11a1.jpg"
                    background_radio_down : "male_button_down.png"
                    group: "gender"
                    value: "male"
                    size_hint_x: .5
            
                CustCheckBox:
                    on_active: root.gender_is(self, self.value)
                    background_radio_normal : "59073b75808581554caa8e4c1d374fe9.jpg"
                    background_radio_down : "female_button_down.png"
                    group: "gender"
                    value: "female"
                    size_hint_x: .5
                
        Button:
            text: "Next"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'
            size_hint_x: 1
            size_hint_y: 0.1
 
<ScreenTwo>:
    BoxLayout:
        orientation : "vertical"

        BoxLayout:
            orientation: "vertical"
            size_hint_y: 0.2
            spacing:10
            
            CustLabel:
                text: str("BODY MASS INDEX")
                color: 0,0,0,1
                size_hint_y: 0.1
                font_size : 50
 
            CustLabel:
                text: str("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
                color: 0,0,0,1
                size_hint_y: 0.1


        BoxLayout:
            orientation : "horizontal"
            size_hint_y: 0.6

            # Box Containing HEIGHT Slider
            # Orientation is vertical
            BoxLayout:
                orientation: "horizontal"
                spacing:10
                size_hint_x : 0.25
    
                Slider:
                    id: height_id
                    orientation: "vertical"
                    background_vertical : "Symbol 1 – 1.png"
                    min: 0
                    max: 100
                    value: 0
                    step: 0.5
                    value_tracker:"true"
                    value_tracker_color : (1, 0, 0, 1)
                    cursor_image: "arrow-clipart-cute-6.png"
                    cursor_size: (150, 150)

        
            # Box Containing Height's value
            # Orientation is vertical
            BoxLayout:
                orientation: "vertical"
                spacing:10
                size_hint_x : 0.25
                
                CustLabel:
                    font_size : sp(40)
                    size_hint_y: 0.4

                CustLabel:
                    text: "HEIGHT"
                    font_size: sp(40)
                    color: 0, 0, 0, 1
                    size_hint_y: 0.3

                CustLabel:
                    text: str(height_id.value)
                    font_size : sp(40)
                    size_hint_y: 0.3

                CustLabel:
                    font_size : sp(40)
                    size_hint_y: 0.4

            # Box Containing Weight Slider
            # Orientation is vertical
            BoxLayout:
                orientation: "vertical"
                spacing:10
                size_hint_x : 0.50

                CustLabel:
                    text: "WEIGHT"
                    font_size: sp(40)
                    color: 0, 0, 0, 1
                    size_hint_y: 0.15

                CustLabel:
                    text: str(weight_id.value)
                    font_size : sp(40)
                    size_hint_y: 0.1

                Slider:
                    id: weight_id
                    size_hint_y: 0.1
                    orientation: "horizontal"
                    background_horizontal : "Symbol 1 – 2.png"
                    min: 0
                    max: 100
                    value: 0
                    step: 0.5
                    value_tracker:"true"
                    value_tracker_color : (1, 0, 0, 1)
                    # cursor_image: "arrow-clipart-cute-6.png"
                    # cursor_size: (150, 150)

                CustLabel:
                    font_size : sp(40)
                    size_hint_y: 0.1

        Button:
            text: "Next"
            size_hint_x: 1
            size_hint_y: 0.1
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_one'
""")
 
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
 
 
# The ScreenManager controls moving between screens
screen_manager = ScreenManager()
 
# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
 
class KivyTut2App(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return screen_manager
 
sample_app = KivyTut2App()
sample_app.run()