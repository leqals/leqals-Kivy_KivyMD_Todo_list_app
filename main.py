import os 
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from screens.signIn.sign_in_page import SignInPage
from screens.home.home_page import HomePage
from screens.history.history_page import HistoryPage
from kivy.lang.builder import Builder
from kivymd.uix.textfield import MDTextFieldRound


Window.size = [330, 640]

class TrackioApp(MDApp):
    sm = MDScreenManager(id='screen_manager')
    def build(self):
        self.ld_kv_files()
        self.add_screen()
        
        return self.sm
    
    def add_screen(self):
        self.sm.add_widget(SignInPage(name='signIn'))
        self.sm.add_widget(HomePage(name='home'))
        self.sm.add_widget(HistoryPage(name='history'))
    
    def ld_kv_files(self):
        Builder.load_file('components/utilities.kv')
        Builder.load_file('components/todo.kv')
        Builder.load_file('screens/home/home_page.kv')
        Builder.load_file('screens/signIn/sign_in_page.kv')
        Builder.load_file('screens/history/history_page.kv')

    def switchScreen(self):
        pass
        
    
if __name__ == '__main__': TrackioApp().run()