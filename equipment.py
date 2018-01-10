class Test1():
    def __init__(self, name):
        self.name = name

    def process(self):
        print('{} heals you'.format(self.name))

class Test2():
    def __init__(self, name):
        self.name = name

    def process(self):
        print('{} smashes you'.format(self.name))
