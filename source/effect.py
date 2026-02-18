NO_DEPS = object()

class useEffect:
    def __init__(self, function, deps=NO_DEPS): 
        self.function = function
        self.deps = deps
        self.first_run = True
        self.prev = None
        self.execute()

    def execute(self):
        if self.deps is NO_DEPS:
            self.function()
            return
        if self.deps is None:
            if self.first_run:
                self.function()
                self.first_run = False
            return
        if self.prev != self.deps:
            self.prev = self.deps
            self.function()




