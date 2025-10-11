import json
from datetime import datetime

MENU_FILE = 'menu.json'
SALES_FILE = 'sales.json'


class Cafe:
    def __init__(self):
        self.menu = self.load_data(MENU_FILE)
        self.sales = self.load_data(SALES_FILE)

    def load_data(self, filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self, filename, data):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    # ------------------ MENU MANAGEMENT ------------------

    def add_item(self, name, price):
        self.menu[name] = price
        self.save_data(MENU_FILE, self.menu)
        print(f"Added '{name}' to menu for ${price:.2f}")

    def update_price(self, name, price):
        if name in self.menu:
            self.menu[name] = price
            self.save_data(MENU_FILE, self.menu)
            print(f"Updated price of '{name}' to ${price:.2f}")
        else:
            print("Item not found in menu.")

    def remove_item(self, name):
        if name in self.menu:
            del self.menu[name]
            self.save_data(MENU_FILE, self.menu)
            print(f"Removed '{name}' from menu.")
        else:
            print("Item not found.")

    def show_menu(self):
        print("\n--- Cafe Menu ---")
        for name, price in self.menu.items():
            print(f"{name}: ${price:.2f}")
        print("------------------\n")

    # ------------------ ORDER MANAGEMENT ------------------

    def place_order(self):
        self.show_menu()
        order = {}
        while True:
            item = input("Enter item name (or 'done' to finish): ").strip()
            if item.lower() == 'done':
                break
            if item not in self.menu:
                print("Item not found.")
                continue
            quantity = int(input(f"Enter quantity of '{item}': "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity

        if not order:
            print("No items ordered.")
            return

        total = self.generate_bill(order)
        date = datetime.now().strftime("%Y-%m-%d")
        if date not in self.sales:
            self.sales[date] = 0
        self.sales[date] += total
        self.save_data(SALES_FILE, self.sales)

    def generate_bill(self, order):
        print("\n--- Bill Receipt ---")
        total = 0
        for item, qty in order.items():
            price = self.menu[item]
            item_total = price * qty
            total += item_total
            print(f"{item} x {qty} = ${item_total:.2f}")
        print(f"Total: ${total:.2f}")
        print("--------------------\n")
        return total

    # ------------------ SALES REPORT ------------------

    def view_sales(self):
        print("\n--- Daily Sales ---")
        for date, amount in self.sales.items():
            print(f"{date}: ${amount:.2f}")
        print("-------------------\n")


def main():
    cafe = Cafe
