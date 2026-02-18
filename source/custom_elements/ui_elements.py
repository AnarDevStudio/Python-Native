from source.component import *

class Button(Component):
    def __init__(self, value, **props): 
        self.value = value
        self.onClick = props.get("onClick")  
        self.onChange = props.get("onChange")  

        if callable(self.onClick):
            self.onClick()
