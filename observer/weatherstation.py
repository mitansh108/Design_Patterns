class WeatherStation():

    def __init__(self):
        self.__observers = []
        self.__temperature = 0

    def addObserver(self, new_observer):
        self.__observers.append(new_observer)

    def removeObserver(self, ob):
        self.__observers.remove(ob)

    def updateTemperature(self, new_temp):
        self.__temperature = new_temp

        self.notifyObservers()
    
    def notifyObservers(self):
        for obs in self.__observers:
            obs.update(self.__temperature)
    