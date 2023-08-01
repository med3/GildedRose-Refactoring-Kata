import pytest
from gilded_rose import GildedRose, Item, AgedBrie, BackstagePass, ConjuredItem, Sulfuras

def test_normal_item_quality_degradation():
    item = Item("Normal Item", 10, 20)
    gilded_rose = GildedRose([item])

    gilded_rose.update_quality()
    assert item.quality == 19

def test_normal_item_quality_after_sell_date():
    item = Item("Normal Item", 0, 20)
    gilded_rose = GildedRose([item])

    gilded_rose.update_quality()
    assert item.quality == 18

def test_normal_item_quality_not_below_zero():
    item = Item("Normal Item", 10, 1)
    gilded_rose = GildedRose([item])

    gilded_rose.update_quality()
    assert item.quality == 0

def test_normal_item_quality_not_above_fifty():
    item = Item("Normal Item", 10, 50)
    gilded_rose = GildedRose([item])

    gilded_rose.update_quality()
    assert item.quality == 49

# ... Add other item tests for AgedBrie, BackstagePass, ConjuredItem, and Sulfuras ...

# Mocking Example
def test_update_quality_calls_item_methods(mocker):
    item_mock = mocker.MagicMock(spec=AgedBrie)
    gilded_rose = GildedRose([item_mock])

    gilded_rose.update_quality()

    item_mock.update_quality.assert_called_once()

# Monkeypatching Example
def test_parse_item_calls_correct_subclass(monkeypatch):
    def mock_parse_item(self, item):
        return AgedBrie(item, 5, 49)

    monkeypatch.setattr(GildedRose, "parse_item", mock_parse_item)

    items = ["Aged Brie, 5, 49"]
    gilded_rose = GildedRose(items)

    assert isinstance(gilded_rose.items[0], AgedBrie)

# ... Add other tests for mocking and monkeypatching ...

# Test when the input contains an unknown item
def test_parse_item_unknown_item():
    items = ["Unknown Item, 5, 30"]
    gilded_rose = GildedRose(items)

    with pytest.raises(ValueError, match="Unknown item type"):
        gilded_rose.update_quality()

if __name__ == "__main__":
    pytest.main()
