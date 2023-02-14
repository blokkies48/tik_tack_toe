from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from logic import AppLogic


class MainApp(App):
    def build(self):
        Builder.load_file("design.kv")
        screen_manager = ScreenManager()

        screen_manager.add_widget(AppLogic(name = "AppLogic"))
        return screen_manager

if __name__ == "__main__":

    MainApp().run()
