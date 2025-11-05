import tkinter as tk

class Animal:
    def speak(self):
        return ""

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

class Duck(Animal):
    def speak(self):
        return "꽥꽥!"

def make_sound(animal):
    label.config(text=animal.speak())

root = tk.Tk()
root.title("동물소리듣기")

label = tk.Label(root, text="동물소리를 들어보세요.", font=("Arial", 14))
label.pack(pady=15)

frame = tk.Frame(root)
frame.pack()

btn1 = tk.Button(frame, text="강아지", width=10, command=lambda: make_sound(Dog()))
btn1.pack(side="left", padx=5)

btn2 = tk.Button(frame, text="고양이", width=10, command=lambda: make_sound(Cat()))
btn2.pack(side="left", padx=5)

btn3 = tk.Button(frame, text="오리", width=10, command=lambda: make_sound(Duck()))
btn3.pack(side="left", padx=5)

root.mainloop()
