from histori import Histori
from text_editor import TextEditor
from text_memento import TextMemento

text_editor = TextEditor()
history = Histori()

text_editor.write("Hello")
text_editor.write(" World")

history.save_state(text_editor.save_text())

text_editor.write("Goodbye")
text_editor.write(" World")
history.save_state(text_editor.save_text())
history.get_history()
print("-------------------")
text_editor.restore(history.undo())
print(text_editor.get_text())

text_editor.restore(history.redo())
print("--------------")
print("After Redo")
print("--------------")
print(text_editor.get_text())







