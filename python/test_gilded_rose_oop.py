import pytest
from gilded_rose import GildedRose, Item, AgedBrie, BackstagePass, ConjuredItem, Sulfuras

def test_normal_item_quality_degradation():
    items = [Item("Normal Item", 10, 20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 19

def test_normal_item_quality_after_sell_date():
    items = [Item("Normal Item", 0, 20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 18

def test_normal_item_quality_not_below_zero():
    items = [Item("Normal Item", 10, 1)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 0

def test_normal_item_quality_not_above_fifty():
    items = [Item("Normal Item", 10, 50)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 49

def test_aged_brie_quality_increase():
    items = [AgedBrie("Aged Brie", 10, 20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 21

def test_aged_brie_quality_after_sell_date():
    items = [AgedBrie("Aged Brie", 0, 20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 22

def test_aged_brie_quality_not_above_fifty():
    items = [AgedBrie("Aged Brie", 10, 50)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 50

def test_backstage_pass_quality_increase():
    items = [BackstagePass("Backstage Pass", 15, 20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 21

def test_backstage_pass_quality_increase_double_near_concert():
    items = [BackstagePass("Backstage Pass", 10, 20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 22

def test_backstage_pass_quality_increase_triple_very_near_concert():
    items = [BackstagePass("Backstage Pass", 5, 20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 23

def test_backstage_pass_quality_zero_after_sell_date():
    items = [BackstagePass("Backstage Pass", 0, 20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 0

def test_backstage_pass_quality_not_above_fifty():
    items = [BackstagePass("Backstage Pass", 5, 50)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 50

def test_conjured_item_quality_degradation():
    items = [ConjuredItem("Conjured Item", 10, 20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 18

def test_conjured_item_quality_after_sell_date():
    items = [ConjuredItem("Conjured Item", 0, 20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 16

def test_conjured_item_quality_not_below_zero():
    items = [ConjuredItem("Conjured Item", 10, 1)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 0

def test_sulfuras_quality_stable():
    items = [Sulfuras("Sulfuras", 10, 80)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 80

def test_sulfuras_sell_in_stable():
    items = [Sulfuras("Sulfuras", 10, 80)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].sell_in == 10
