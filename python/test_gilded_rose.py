# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_sulfurus(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 20, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)
        
    def test_sulfurus_past_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 20, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].sell_in)
        self.assertEquals(31, items[0].quality)

    def test_aged_brie_hits_50_quality(self):
        items = [Item("Aged Brie", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_aged_brie_quality_increases_by_2_after_date(self):
        items = [Item("Aged Brie", 0, 37)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(39, items[0].quality)

    def test_normal_item(self):
        items = [Item("Rat soup", 20, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(10, items[0].quality)

    def test_normal_item_degrades_twice_as_fast(self):
        items = [Item("Rat soup", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality)

    def test_normal_item_stops_at_zero(self):
        items = [Item("Rat soup", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_backstage_pass_increases_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(26, items[0].quality)

    def test_backstage_pass_stops_at_50_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_backstage_pass_less_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(27, items[0].quality)

    def test_backstage_pass_less_than_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(28, items[0].quality)

    def test_backstage_pass_less_than_0_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
