import time

class GeyserClassic:
    MAX_DATE_FILTER = 100
    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and type(filter) == Mechanical and not self.slot_1:
            self.slot_1 = filter
        if slot_num == 2 and type(filter) == Aragon and not self.slot_2:
            self.slot_2 = filter
        if slot_num == 3 and type(filter) == Calcium and not self.slot_3:
            self.slot_3 = filter

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot_1 = None
        if slot_num == 2:
            self.slot_2 = None
        if slot_num == 3:
            self.slot_3 = None

    def get_filters(self):
        return (self.slot_1,self.slot_2,self.slot_3)

    def water_on(self):
        for i in (self.slot_1, self.slot_2, self.slot_3):
            if not i:
                return False

            if time.time() - i.date > self.MAX_DATE_FILTER:
                return False
        return True



class Mechanical:
    DATE = True
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)


class Aragon:
    DATE = True
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)

class Calcium:
    DATE = True
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)



my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
# w = my_water.water_on() # False

my_water.add_filter(3, Calcium(time.time()))
print(my_water.water_on())
time.sleep(15)
print(time.time() - my_water.get_filters()[0].date)
print(my_water.water_on())
print(my_water.water_on())