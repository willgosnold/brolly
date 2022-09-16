from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.uix.widget import Widget

class MainScreen(Screen):
    pass

class SecondaryScreen(Screen):
    pass

class MainScreenManager(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return presentation



if __name__ == '__main__':
    print("something")
    MainApp().run()