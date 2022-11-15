from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from user_helper import username_helper
from kivymd.uix.dialog import MDDialog


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        # self.theme_cls.primary_palette = "Yellow"
        # self.theme_cls.primary_hue = 'A700'
        # self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        # label = MDLabel(text="Hello World", halign='center', theme_text_color='Custom', text_color=(135/225,206/225,235/222),
        #                 font_style='Button')
        # icon_label = MDIcon(icon='language-python',halign='center')
        # icon_btn = MDFlatButton(text="Hello world",pos_hint={"center_x": .5, "center_y": .5})
        #icon_btn = MDRectangleFlatButton(text="Hello world",pos_hint={"center_x": .5, "center_y": .5})
        # icon_btn = MDIconButton(icon="play",pos_hint={"center_x": .5, "center_y": .5})
        # icon_btn = MDFloatingActionButton(icon="play",pos_hint={"center_x": .5, "center_y": .5})
        # username  = MDTextField(text="Enter username", pos_hint={"center_x": .5, 'center_y': .5},
        #                         size_hint_x=None, width=300)
        self.username = Builder.load_string(username_helper)
        btn = MDRectangleFlatButton(text="Show", pos_hint={'center_x': .5, 'center_y': .4},
                                    on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(btn)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_string = "Please Enter username"
        else:
            check_string = self.username.text + ' does not Exist'
        close_dialog = MDFlatButton(text="Close", on_release= self.close_dialog)
        self.dialog = MDDialog(title='Username', text=check_string, buttons=[close_dialog])
        self.dialog.open()
        print(self.username.text)

    def close_dialog(self, obj):
        self.dialog.dismiss()

DemoApp().run()