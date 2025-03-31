import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        """
        testing normal items
        """
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
        items = [Item("foo", 8, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(29, items[0].quality)
        items = [Item("foo", 8, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(29, items[0].quality)
        items = [Item("foo", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(28, items[0].quality)
        

    def test_aged_brie(self):
        """
        testing for aged brie
        """
        items = [Item("Aged Brie", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)
        self.assertEqual(1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        self.assertEqual(0, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras(self):
        """
        testing for sulfuras
        """
        items = [Item("Sulfuras", 1 , 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes(self):
        """
        testing for backstage passes
        """
        items = [Item("Backstage passes", 7, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].sell_in)
        self.assertEqual(22, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(25, items[0].quality)
        items = [Item("Backstage passes", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
        items = [Item("Backstage passes", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_conjured(self):
        """
        testing for conjured itesms
        """
        items = [Item("Conjured", 5 , 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(8, items[0].quality)
        items = [Item("Conjured", -1 , 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

if __name__ == '__main__':
    unittest.main()