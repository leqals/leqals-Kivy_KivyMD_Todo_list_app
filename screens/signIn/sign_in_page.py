from kivymd.uix.screen import MDScreen 
from kivy.properties import StringProperty


class SignInPage(MDScreen):
    # TODOS
    
    # - Collect the login data
    
    email = StringProperty('')
    password = StringProperty('')
    
    
    
    def get_data(self):
        self.email = self.ids.email.text
        self.password = self.ids.password.text 
        
    # - Check data validity
        isEmail = True if '@' in self.email and '.' in self.email else False
        isPassword = True if self.password != '' and len(self.password) > 3 else False 
        
        return isEmail, isPassword
        
    
        
        
        
        
        
        
        
        
    
    