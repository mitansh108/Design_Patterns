from weatherstation import WeatherStation
from tv import TVdisplay
from mobile import Mobiledisplay

ws = WeatherStation()
tv = TVdisplay()
m = Mobiledisplay()

ws.addObserver(tv)
ws.addObserver(m)
ws.updateTemperature(500)
