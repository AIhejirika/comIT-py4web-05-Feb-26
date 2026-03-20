# ☕ Python OOP Exercise: Build a Café Ordering System

**Difficulty:** Beginner–Intermediate  
**Topic:** Object-Oriented Programming (OOP)  
**Estimated Time:** 2–3 hours  

---

## 🎯 What You Will Learn

By completing this exercise you will practice:

- Creating **classes** and **objects**
- Using `__init__` to set up attributes
- Using **methods** to add behavior to a class
- Storing objects in **lists**
- Using a **`while` loop** to build an interactive menu
- Formatting printed output neatly

---

## 📖 Key Concepts (Read This First!)

### What is a Class?
A **class** is like a blueprint. It describes what an object *is* and what it can *do*.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name    # attribute
        self.breed = breed  # attribute

    def bark(self):         # method
        print(f"{self.name} says: Woof!")

my_dog = Dog("Rex", "Labrador")  # creating an object
my_dog.bark()                    # calling a method
```

### What is `self`?
`self` refers to **the object itself**. Every method in a class must have `self` as its first parameter so Python knows which object is being used.

### What is `__init__`?
`__init__` is a **special method** that runs automatically when you create a new object. It sets up the starting values (attributes) for the object.

---

## 🏗️ The Exercise

You will build a **Café Ordering System** step by step. The final program will:

1. Show a menu of coffee drinks
2. Let the customer pick a drink and a size
3. Keep taking orders until the customer says they are done
4. Print a bill with subtotal, tax, and tip

---

## 📂 File Structure

Create a single file called `cafe.py`. All your code goes there.

---

## 🔨 Step-by-Step Instructions

---

### Step 1 — Create the `Coffee` Class

This class represents **one type of coffee** on the menu.

**Create a class called `Coffee` with these attributes:**

| Attribute     | Type    | Description                              |
|---------------|---------|------------------------------------------|
| `name`        | `str`   | The name of the drink (e.g. "Latte")     |
| `description` | `str`   | A short description of the drink         |
| `base_price`  | `float` | The starting price before size is added  |

**Add a method called `__str__`** that returns a nicely formatted string describing the coffee. This method is called automatically when you `print()` an object.

```python
class Coffee:
    def __init__(self, name, description, base_price):
        # YOUR CODE HERE
        pass

    def __str__(self):
        # Return a string like: "Latte - A creamy espresso with steamed milk - $3.50"
        # YOUR CODE HERE
        pass
```

> 💡 **Hint:** To format a float with 2 decimal places use `f"${self.base_price:.2f}"`

---

### Step 2 — Create the `Order` Class

This class represents **a single item** a customer has ordered (one drink, one size).

**Create a class called `Order` with these attributes:**

| Attribute | Type     | Description                                  |
|-----------|----------|----------------------------------------------|
| `coffee`  | `Coffee` | The Coffee object the customer chose         |
| `size`    | `str`    | The size: `"Small"`, `"Medium"`, or `"Large"`|
| `price`   | `float`  | Calculated final price for this order item   |

**Size pricing rules — add these to the price on top of `base_price`:**

| Size   | Extra Cost |
|--------|------------|
| Small  | $0.00      |
| Medium | $0.50      |
| Large  | $1.00      |

**Add a method called `calculate_price`** that takes the size and returns the correct total price.

```python
class Order:
    def __init__(self, coffee, size):
        self.coffee = coffee
        self.size = size
        self.price = self.calculate_price()   # automatically calculate the price

    def calculate_price(self):
        # Start with the coffee's base price
        # Add extra cost based on size
        # Return the final price
        # YOUR CODE HERE
        pass

    def __str__(self):
        # Return a string like: "Medium Latte - $4.00"
        # YOUR CODE HERE
        pass
```

---

### Step 3 — Create the `Cafe` Class

This class manages the whole café: the menu and the customer's list of orders.

**Create a class called `Cafe` with these attributes:**

| Attribute | Type   | Description                              |
|-----------|--------|------------------------------------------|
| `name`    | `str`  | The name of the café                     |
| `menu`    | `list` | A list of `Coffee` objects               |
| `orders`  | `list` | A list of `Order` objects (starts empty) |
| `tax_rate`| `float`| Tax rate as a decimal (e.g. `0.08` = 8%)|

```python
class Cafe:
    def __init__(self, name, tax_rate=0.08):
        self.name = name
        self.menu = []       # empty list — we will fill it with coffees
        self.orders = []     # empty list — orders are added as the customer shops
        self.tax_rate = tax_rate

    def add_to_menu(self, coffee):
        """Add a Coffee object to the menu list."""
        # YOUR CODE HERE
        pass

    def display_menu(self):
        """Print the full menu with numbers so the customer can pick."""
        # Print a header with the café name
        # Loop through self.menu with enumerate() to show numbers
        # Example output:
        #   === SUNNY BEAN CAFÉ MENU ===
        #   1. Espresso       - Strong and bold shot of coffee    - $2.50
        #   2. Americano      - Espresso diluted with hot water   - $3.00
        # YOUR CODE HERE
        pass

    def display_sizes(self):
        """Print the available sizes."""
        # Show the three sizes and their extra costs
        # YOUR CODE HERE
        pass

    def add_order(self, coffee, size):
        """Create a new Order and add it to the orders list."""
        new_order = Order(coffee, size)
        self.orders.append(new_order)
        print(f"\n✅ Added: {new_order}")

    def calculate_subtotal(self):
        """Add up the price of every order and return the total."""
        # Loop through self.orders and sum all the prices
        # YOUR CODE HERE
        pass

    def print_bill(self, tip_percent):
        """Print a formatted receipt with subtotal, tax, tip, and grand total."""
        subtotal = self.calculate_subtotal()
        tax = subtotal * self.tax_rate
        tip = subtotal * (tip_percent / 100)
        total = subtotal + tax + tip

        # Print a formatted receipt
        # Example output:
        # ==========================================
        #        SUNNY BEAN CAFÉ — YOUR BILL
        # ==========================================
        #  Medium Latte                      $4.00
        #  Large Cappuccino                  $5.50
        # ------------------------------------------
        #  Subtotal:                         $9.50
        #  Tax (8%):                         $0.76
        #  Tip (15%):                        $1.43
        # ==========================================
        #  TOTAL:                           $11.69
        # ==========================================
        #
        # YOUR CODE HERE
        pass
```

> 💡 **Hint for formatting columns:** Use f-strings with alignment.  
> Example: `f"{'Subtotal:':<30} ${subtotal:>6.2f}"` — `<30` left-aligns in 30 chars, `>6.2f` right-aligns a float.

---

### Step 4 — Set Up the Menu Data

Outside of any class, create a `Cafe` object and fill its menu with coffee drinks.

```python
# --- SETUP ---
cafe = Cafe("Sunny Bean Café", tax_rate=0.08)

# Create Coffee objects and add them to the menu
cafe.add_to_menu(Coffee("Espresso",    "Strong and bold shot of coffee",           2.50))
cafe.add_to_menu(Coffee("Americano",   "Espresso diluted with hot water",          3.00))
cafe.add_to_menu(Coffee("Cappuccino",  "Equal parts espresso, foam, and milk",     3.75))
cafe.add_to_menu(Coffee("Latte",       "Creamy espresso with lots of steamed milk",3.50))
cafe.add_to_menu(Coffee("Flat White",  "Velvety milk with a double espresso shot", 4.00))
cafe.add_to_menu(Coffee("Macchiato",   "Espresso 'stained' with a touch of foam",  3.25))
cafe.add_to_menu(Coffee("Mocha",       "Espresso with chocolate and steamed milk", 4.25))
cafe.add_to_menu(Coffee("Cold Brew",   "Slow-steeped coffee served cold",          4.00))
```

---

### Step 5 — Build the Interactive Menu (The `while` Loop)

This is the main ordering loop. It keeps running until the customer chooses to check out.

```python
SIZES = ["Small", "Medium", "Large"]

print(f"\nWelcome to {cafe.name}! ☕")

while True:
    print("\n" + "="*40)
    print("What would you like to do?")
    print("1. View menu and order a drink")
    print("2. View current order")
    print("3. Checkout and pay")
    print("="*40)

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        # Show menu
        cafe.display_menu()

        # Ask the customer to pick a drink (validate input!)
        drink_input = input("\nEnter the number of the drink you want (or 0 to cancel): ").strip()

        if drink_input == "0":
            continue   # go back to the top of the while loop

        # Check that the input is a valid number
        if not drink_input.isdigit():
            print("❌ Please enter a number.")
            continue

        drink_index = int(drink_input) - 1   # subtract 1 because lists start at 0

        if drink_index < 0 or drink_index >= len(cafe.menu):
            print("❌ That number is not on the menu. Try again.")
            continue

        selected_coffee = cafe.menu[drink_index]

        # Show sizes
        cafe.display_sizes()
        size_input = input("Enter the number of the size you want: ").strip()

        if not size_input.isdigit():
            print("❌ Please enter a number.")
            continue

        size_index = int(size_input) - 1

        if size_index < 0 or size_index >= len(SIZES):
            print("❌ Invalid size. Try again.")
            continue

        selected_size = SIZES[size_index]

        # Add the order
        cafe.add_order(selected_coffee, selected_size)

    elif choice == "2":
        if not cafe.orders:
            print("\n🛒 Your order is empty.")
        else:
            print("\n--- Your Current Order ---")
            for i, order in enumerate(cafe.orders, start=1):
                print(f"  {i}. {order}")
            print(f"  Subtotal so far: ${cafe.calculate_subtotal():.2f}")

    elif choice == "3":
        if not cafe.orders:
            print("\n❌ You have not ordered anything yet!")
            continue

        # Ask for tip percentage
        print("\nHow much would you like to tip?")
        print("1. 10%    2. 15%    3. 20%    4. No tip")
        tip_choice = input("Enter your choice (1/2/3/4): ").strip()

        tip_map = {"1": 10, "2": 15, "3": 20, "4": 0}
        tip_percent = tip_map.get(tip_choice, 0)

        cafe.print_bill(tip_percent)
        print("\nThank you for visiting! Have a great day! ☕\n")
        break   # Exit the while loop — we are done!

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
```

---

## ✅ Sample Output

```
Welcome to Sunny Bean Café! ☕

========================================
What would you like to do?
1. View menu and order a drink
2. View current order
3. Checkout and pay
========================================
Enter your choice (1/2/3): 1

=== SUNNY BEAN CAFÉ MENU ===
1. Espresso       - Strong and bold shot of coffee          - $2.50
2. Americano      - Espresso diluted with hot water         - $3.00
3. Cappuccino     - Equal parts espresso, foam, and milk    - $3.75
...

Enter the number of the drink you want (or 0 to cancel): 3

Sizes available:
1. Small  (+$0.00)
2. Medium (+$0.50)
3. Large  (+$1.00)
Enter the number of the size you want: 3

✅ Added: Large Cappuccino - $4.75

...

==========================================
       SUNNY BEAN CAFÉ — YOUR BILL
==========================================
 Large Cappuccino                   $4.75
 Medium Latte                       $4.00
------------------------------------------
 Subtotal:                          $8.75
 Tax (8%):                          $0.70
 Tip (15%):                         $1.31
==========================================
 TOTAL:                            $10.76
==========================================

Thank you for visiting! Have a great day! ☕
```

---

## 🚀 Bonus Challenges

Once you finish the main exercise, try these extensions:

1. **Remove an item:** Add a menu option that lets the customer remove a drink from their order.
2. **Quantity:** Let the customer order more than one of the same drink (add a `quantity` attribute to `Order`).
3. **Loyalty discount:** If the customer orders 3 or more items, apply a 5% discount.
4. **Specials:** Add a `daily_special` attribute to `Cafe` and display it at the top of the menu.
5. **Save the receipt:** Write the bill to a `.txt` file instead of just printing it.

---

## 🗺️ Class Diagram (Quick Reference)

```
+---------------------------+
|         Coffee            |
+---------------------------+
| name: str                 |
| description: str          |
| base_price: float         |
+---------------------------+
| __str__() -> str          |
+---------------------------+

+---------------------------+
|          Order            |
+---------------------------+
| coffee: Coffee            |
| size: str                 |
| price: float              |
+---------------------------+
| calculate_price() -> float|
| __str__() -> str          |
+---------------------------+

+---------------------------+
|           Cafe            |
+---------------------------+
| name: str                 |
| menu: list[Coffee]        |
| orders: list[Order]       |
| tax_rate: float           |
+---------------------------+
| add_to_menu(coffee)       |
| display_menu()            |
| display_sizes()           |
| add_order(coffee, size)   |
| calculate_subtotal()      |
| print_bill(tip_percent)   |
+---------------------------+
```

---

## 💡 Common Mistakes to Avoid

| Mistake | Fix |
|---|---|
| Forgetting `self` in method parameters | Every method needs `self` as the first parameter |
| Using `=` instead of `==` in conditions | `=` assigns a value, `==` compares two values |
| List index off by one | Menu shows `1, 2, 3...` but lists use `0, 1, 2...` — always subtract 1 |
| Not validating user input | Use `.isdigit()` before converting with `int()` to avoid crashes |
| Infinite loop with no exit | Make sure your `while True` loop has a `break` somewhere |

---

*Good luck and enjoy your coffee! ☕*
