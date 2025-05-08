class Counter:
    count = 0

    def __init__(self , meassage):
        self.meassage = meassage
        print(self.meassage)
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created : {cls.count}")

obj1:Counter = Counter("1st Object Created")
obj2:Counter = Counter("2nd Object Created")
obj3:Counter = Counter("3rd Object Created")
obj4:Counter = Counter("4th Object Created")
Counter.display_count()
