class HotBeverage:
    price=0.30
    name="hot beverage"

    def __init__(self):
        self.name = n
        self.price = p
        self.descrip = description()

    def description(self):
        return "Just some hot water in a cup..."

    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def __repr__(self):
            return "Type what do you want to see here."
        
