# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = [self.parse_item(item) for item in items]

    def parse_item(self, item):
        name, sell_in, quality = item.split(', ')
        if "Sulfuras" in name:
            return Sulfuras(name, int(sell_in), int(quality))
        elif "Aged Brie" in name:
            return AgedBrie(name, int(sell_in), int(quality))
        elif "Backstage passes" in name:
            return BackstagePass(name, int(sell_in), int(quality))
        elif "Conjured" in name:
            return ConjuredItem(name, int(sell_in), int(quality))
        else:
            return NormalItem(name, int(sell_in), int(quality))

    def update_quality(self):
        for item in self.items:
            item.update_quality()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality -= 1

        self.quality = max(self.quality, 0)
        self.quality = min(self.quality, 50)

class AgedBrie(Item):
    def update_quality(self):
        super().update_quality()
        self.quality += 1

        self.quality = min(self.quality, 50)

class BackstagePass(Item):
    def update_quality(self):
        super().update_quality()

        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 6:
            self.quality += 3
        elif self.sell_in < 11:
            self.quality += 2
        else:
            self.quality += 1

        self.quality = min(self.quality, 50)

class ConjuredItem(Item):
    def update_quality(self):
        super().update_quality()
        self.quality -= 2

        self.quality = max(self.quality, 0)
        self.quality = min(self.quality, 50)

class Sulfuras(Item):
    def update_quality(self):
        # Sulfuras does not change its quality or sell_in value
        pass

if __name__ == "__main__":
    items = [
        "Normal Item, 10, 20",
        "Aged Brie, 5, 49",
        "Backstage passes to a TAFKAL80ETC concert, 15, 25",
        "Sulfuras, Hand of Ragnaros, 0, 80",
        "Conjured Mana Cake, 3, 6"
    ]
    
    gilded_rose = GildedRose(items)
    
    print("-------- Original Items --------")
    for item in gilded_rose.items:
        print(item)

    gilded_rose.update_quality()
    
    print("\n-------- Updated Items --------")
    for item in gilded_rose.items:
        print(item)
