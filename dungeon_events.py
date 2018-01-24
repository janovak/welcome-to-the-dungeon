class DungeonEvents():
    def __init__(self, events):
        self.events = { event : dict() for event in events }

    def get_subscribers(self, event):
        return self.events[event]

    def register(self, event, who, callback=None):
        if callback == None:
            callback = getattr(who, 'process')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def attack(self, event):
        for subscriber, callback in self.get_subscribers(event).items():
            callback()
