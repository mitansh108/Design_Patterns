from observer import Observer

class TVdisplay(Observer):
    def update(self, temp):
        print(f"Tv temperature updated to {temp}")



