# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 2, 1),Item("foo", 3, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
        self.assertEquals(0, items[1].quality)
        

    def test_Aged_Brie(self):
        items = [Item("Aged Brie",20,40),Item("Aged Brie",4,50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(41, items[0].quality)
        self.assertEquals(50, items[1].quality)


    def test_Backstage(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",20,40),
        Item("Backstage passes to a TAFKAL80ETC concert",9,40),
        Item("Backstage passes to a TAFKAL80ETC concert",4,40),
        Item("Backstage passes to a TAFKAL80ETC concert",4,50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(41, items[0].quality)
        self.assertEquals(42, items[1].quality)
        self.assertEquals(43, items[2].quality)
        self.assertEquals(50, items[3].quality) 

    def test_Sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 7, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    

if __name__ == '__main__':
    unittest.main()
