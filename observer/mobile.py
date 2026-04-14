from observer import Observer

class Mobiledisplay(Observer):
    def update(self, temp):
        print(f"Mobile temperature updated to {temp}")



