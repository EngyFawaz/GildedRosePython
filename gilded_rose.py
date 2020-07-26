# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.sell_in < 0 or item.quality <= 0:
                break

            if item.name == "Aged Brie": 
                if item.quality < 50:
                    item.quality = item.quality + 1

            elif item.name == "Backstage passes to a TAFKAL80ETC concert": 
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.sell_in < 11:
                        item.quality = item.quality + 1
                    if item.sell_in < 6:
                        item.quality = item.quality + 1

            elif item.name == "Conjured":
                item.quality = item.quality - 2
                
            elif item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality - 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
