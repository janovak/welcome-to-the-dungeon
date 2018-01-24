import json
import equipment
from dungeon_events import DungeonEvents
from deck import Deck

monsters = json.load(open('monster_deck.json'))["monsters"]
deck = Deck()
for k, v in monsters.items():
    deck.build(k, v['quantity'])
deck.shuffle()

events = list(monsters.keys()) + ['enter_dungeon', 'finish_dungeon']
dungeon_events = DungeonEvents(events)

start = equipment.Test1('heal')
sword = equipment.Test2('sword')
shield = equipment.Test1('shield')

dungeon_events.register('enter_dungeon', start)
dungeon_events.register('orc', sword)
dungeon_events.register('orc', shield)
dungeon_events.register('lich', shield)

dungeon_events.attack("enter_dungeon")
dungeon_events.attack("lich")
