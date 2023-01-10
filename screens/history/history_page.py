from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty


class History(MDBoxLayout):
    hTitle = StringProperty('Test1')
    hDes = StringProperty('Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur, veritatis! Ut, numquam? Temporibus, mollitia.')
    hTime = StringProperty('1 min ago')

class HistoryPage(MDScreen):
    # Todos
    # - create a function to get the data 
    # - Import the history component
    # - Loop over the data and the a history component for every Item
    pass 

        