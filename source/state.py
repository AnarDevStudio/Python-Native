class State():
    def __init__(this, value):
        this.value = value

    def getState(this):
        print(this.value)

    def setState(this, new_value):
        this.value = new_value
        print(this.value)