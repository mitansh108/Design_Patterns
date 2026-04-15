from discount_strategy import DiscountStrategy

class DiscountService:
    def __init__(self, disc_strategy):
        self.__strategy = disc_strategy

    def set_strategy(self, new_disc_strategy):
        self.__strategy = new_disc_strategy

    def process(self):
        self.__strategy.calculate_discount()
