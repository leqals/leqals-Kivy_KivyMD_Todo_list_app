from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, BooleanProperty
import random
import datetime

class Todo(MDBoxLayout):
    date = datetime.datetime.today()
    title = StringProperty('test 1')
    description = StringProperty('this is the test 1 description')
    deadline = StringProperty(date.strftime('%B  %d,  %Y'))
    isDone = BooleanProperty(False)
    
    def send_notification(self):
        # if deadline is due then a push notification to the user else pass
        # note : the above may require event bubbling
        pass
    
    def toggle(self):
        
        # Send an update request to the backend to change the todo to its new isDone value
        self.isDone = not self.isDone
        
    def delete_todo(self):
        
        # Todo
        # check if isDone is True then delete else prompt the user with an alert
        # send a delete request to the backend to delete the todo
        # Bubble event to the todo parent with its ID as a param so that the parent can remove it from the UI
        self.remove_widget(self)