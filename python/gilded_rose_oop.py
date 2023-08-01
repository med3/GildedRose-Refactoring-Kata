# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

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
        self.sell_in -= 1
        self.quality += 1

        if self.sell_in < 0:
            self.quality += 1

        self.quality = min(self.quality, 50)

class BackstagePass(Item):
    def update_quality(self):
        self.sell_in -= 1

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
        self.quality -= 2
        self.sell_in -= 1

        if self.sell_in < 0:
            self.quality -= 2

        self.quality = max(self.quality, 0)
        self.quality = min(self.quality, 50)

class Sulfuras(Item):
    def update_quality(self):
        # Sulfuras does not change its quality or sell_in value
        pass
