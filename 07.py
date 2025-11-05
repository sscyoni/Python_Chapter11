import tkinter as tk
from tkinter import END, BOTH

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self, qty):
        return self.price * qty

    def __str__(self):
        return f"메뉴: {self.name}, 단가: {self.price}원"

class DeliveryFood(Food):
    def __init__(self, name, price, delivery_fee):
        super().__init__(name, price)
        self.delivery_fee = delivery_fee

    def total_price(self, qty):
        return (self.price * qty) + self.delivery_fee

    def __str__(self):
        return f"메뉴: {self.name}, 단가: {self.price}원, 배달비: {self.delivery_fee}원"

class Order:
    def __init__(self):
        self.items = []

    def add(self, food, qty):
        self.items.append((food, qty))

    def clear(self):
        self.items.clear()

    def total(self):
        return sum(food.total_price(qty) for food, qty in self.items)

    def summary_lines(self):
        lines = []
        for food, qty in self.items:
            lines.append(f"{food.name} x {qty} = {food.total_price(qty)}원")
        lines.append(f"총 합계: {self.total()}원")
        return lines

root = tk.Tk()
root.title("주문·배달시스템")
root.geometry("680x440")

order = Order()

menu_list = [
    Food("김밥", 3000),
    Food("떡볶이", 5000),
    DeliveryFood("치킨", 18000, 3000),
    DeliveryFood("짜장면", 6000, 2000),
    Food("라면", 4000),
]

left_frame = tk.Frame(root)
left_frame.pack(side="left", fill=BOTH, padx=10, pady=10)

tk.Label(left_frame, text="메뉴 목록").pack()

menu_box = tk.Listbox(left_frame)
menu_box.pack()

for item in menu_list:
    menu_box.insert(END, str(item))

qty_spin = tk.Spinbox(left_frame, from_=1, to=10)
qty_spin.pack(pady=5)

def add_to_cart():
    idx = menu_box.curselection()
    if not idx:
        return
    food = menu_list[idx[0]]
    qty = int(qty_spin.get())
    order.add(food, qty)
    cart_list.insert(END, f"{food.name} x {qty}")

tk.Button(left_frame, text="장바구니 담기", command=add_to_cart).pack(pady=5)

right_frame = tk.Frame(root)
right_frame.pack(side="right", fill=BOTH, padx=10, pady=10)

tk.Label(right_frame, text="장바구니 목록").pack()

cart_list = tk.Listbox(right_frame)
cart_list.pack()

total_label = tk.Label(right_frame, text="총합계: 0원")
total_label.pack()

receipt = tk.Text(right_frame, height=10)
receipt.pack(pady=5)

def clear_cart():
    order.clear()
    cart_list.delete(0, END)
    total_label.config(text="총합계: 0원")
    receipt.delete("1.0", END)

def make_order():
    receipt.delete("1.0", END)
    for line in order.summary_lines():
        receipt.insert(END, line + "\n")
    total_label.config(text=f"총합계: {order.total()}원")

tk.Button(right_frame, text="전체 비우기", command=clear_cart).pack(pady=5)
tk.Button(right_frame, text="주문하기", command=make_order).pack(pady=5)

root.mainloop()
