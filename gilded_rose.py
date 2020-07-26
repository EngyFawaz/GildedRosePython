# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            
            if item.name != "Sulfuras, Hand of Ragnaros" and item.quality <= 0 and item.sell_in > 0:
                item.sell_in = item.sell_in - 1
                break
                
            if item.sell_in <= 0 and item.quality <= 0:
                break

            if item.name == "Aged Brie": 
                if item.sell_in <= 0:
                    item.quality = 0
                    
                elif item.quality < 50:
                    item.quality = item.quality + 1

            elif item.name == "Backstage passes to a TAFKAL80ETC concert": 
                 if item.sell_in <= 0:
                    item.quality = 0
                
                 elif item.quality < 50:
                    item.quality = item.quality + 1
                    if item.sell_in < 11 and item.quality < 50 :
                        item.quality = item.quality + 1
                    if item.sell_in < 6 and item.quality < 50:
                        item.quality = item.quality + 1
                

            elif item.name == "Conjured":
                if item.sell_in > 0 and item.quality >= 2:
                    item.quality = item.quality - 2
                elif item.quality >= 4:
                    item.quality = item.quality - 4
                else:
                    item.quality = 0
                    
                
            elif item.name != "Sulfuras, Hand of Ragnaros":
                if item.sell_in > 0 :
                    item.quality = item.quality - 1
                elif item.quality >= 2:
                    item.quality = item.quality - 2
                else:
                     item.quality = 0
            else:
                item.quality = 80

            if item.name != "Sulfuras, Hand of Ragnaros" and item.sell_in > 0:
                item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
