class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if "Sulfuras" in item.name:
                continue 
            if "Aged Brie" in item.name:
                item.sell_in -= 1 
                if item.quality < 50:
                    item.quality += 1
            elif "Backstage passes" in item.name:
                item.sell_in -= 1 
                if item.sell_in <= 0:
                    item.quality = 0
                elif item.quality < 50:
                    if item.sell_in > 10:
                        item.quality += 1
                    elif item.sell_in > 5:
                        item.quality += 2
                    else:
                        item.quality += 3
            elif "Conjured" in item.name:
                item.sell_in -= 1 
                if item.quality == 0:
                    continue
                else:
                    if item.sell_in > 0:
                        item.quality -= 2
                    elif item.sell_in < 0:
                        item.quality -= 4
            else:
                item.sell_in -= 1 
                if item.quality == 0:
                    continue
                if item.sell_in > 0:
                    item.quality -= 1
                else:
                    item.quality -= 2
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

gil = GildedRose([Item("Backstage passes", 1, 50)])
gil.update_quality()
print(gil.items[0].sell_in)
print(gil.items[0].quality)