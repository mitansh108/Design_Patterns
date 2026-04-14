from text_memento import TextMemento
from typing import List
class Histori:
    def __init__(self):
        self.__history : list[TextMemento] = []
        self.__redo_stack: list[TextMemento] = []
    
    def save_state (self, tm:TextMemento):
        self.__history.append(tm)
        self.__redo_stack.clear()
    
    def get_history(self):
        for i in range(len(self.__history)):
            print(f"{i} = {self.__history[i].get_saved_text()}")

    def undo(self) -> TextMemento:
        if len(self.__history) > 0:
            self.__redo_stack.append(self.__history.pop())
            if len(self.__history) == 0:
                return TextMemento("")
            return self.__history[-1]
        return TextMemento("")
    
    def redo(self):
        if len(self.__redo_stack) > 0:
            tm = self.__redo_stack.pop()
            self.__history.append(tm)
            return tm
        return self.__history[-1] if self.__history else TextMemento("")

