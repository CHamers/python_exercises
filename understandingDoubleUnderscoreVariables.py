class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23 #seen by convention as a hint that a name is to be treated as private
        self.__baz = 42 #changes the name of the variable 

t = Test()

print(dir(t))
