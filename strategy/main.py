from discount_service import DiscountService
from diwali import DiwaliStrategy
from holi import HoliStrategy

diwali = DiwaliStrategy()
holi = HoliStrategy()

disc_service = DiscountService(diwali)
disc_service.process()

disc_service = DiscountService(holi)
disc_service.process()
