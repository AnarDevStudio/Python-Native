from source.component import *

class BaseComponent(Component):
    def __init__(self, value=None, **props):
        self.value = value
        self.props = props
        self.onClick = props.get("onClick")
        self.onChange = props.get("onChange")
        self.setup() 

        if callable(self.onClick):
            self.onClick()

    def setup(self):
        pass


class Button(BaseComponent):
    def setup(self):
        print(f"Button hazır: {self.value}")


class Text(BaseComponent):
    def setup(self):
        self.color = self.props.get("Color")
        if callable(self.color):
            self.color()
        print(f"Text hazır: {self.value}, Color: {self.color}")


class View(BaseComponent):
    def setup(self):
        print("View hazır")
