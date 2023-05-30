def zad1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} cuisine.")

        def open_restaurant(self):
            print(f"The restaurant {self.restaurant_name} is now open!")

    newRestaurant = Restaurant("MyRestaurant", "Italian")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def display_flavors(self):
            print("Our ice cream flavors:")
            for flavor in self.flavors:
                print(f"- {flavor}")

    ice_cream_stand = IceCreamStand("MyIceCreamStand", "Ice cream", ["vanilla", "chocolate", "strawberry"])
    ice_cream_stand.describe_restaurant()
    ice_cream_stand.display_flavors()

def zad2():
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def display_flavors(self):
            print("The following ice cream flavors are available:")
            for flavor in self.flavors:
                print("- " + flavor)

    ice_cream_stand = IceCreamStand("Scoops", "Ice Cream", ["vanilla", "chocolate", "strawberry"])
    ice_cream_stand.display_flavors()

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, hours):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.location = location
            self.hours = hours

        def display_flavors(self):
            print("The following ice cream flavors are available:")
            for flavor in self.flavors:
                print("- " + flavor)

        def add_flavor(self, flavor):
            self.flavors.append(flavor)

        def remove_flavor(self, flavor):
            self.flavors.remove(flavor)

        def has_flavor(self, flavor):
            return flavor in self.flavors

    class PopsicleStand(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, hours):
            super().__init__(restaurant_name, cuisine_type, flavors, location, hours)

        def sell_popsicle(self, flavor):
            if self.has_flavor(flavor):
                print(f"Selling {flavor} popsicle!")
                self.remove_flavor(flavor)
            else:
                print(f"Sorry, we don't have {flavor} popsicles.")

    class SoftServeStand(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, hours):
            super().__init__(restaurant_name, cuisine_type, flavors, location, hours)

        def serve_cone(self):
            print("Here's your soft serve cone!")

        def serve_twist(self):
            print("Here's your soft serve twist!")


def zad3():
    import tkinter as tk

    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors

        def display_flavors(self):
            print("Available flavors:")
            for flavor in self.flavors:
                print(flavor)

    class IceCreamApp:
        def __init__(self, ice_cream_stand):
            self.ice_cream_stand = ice_cream_stand

            self.root = tk.Tk()
            self.root.title(self.ice_cream_stand.name)

            self.flavors_label = tk.Label(self.root, text="Available flavors:")
            self.flavors_label.pack()

            for flavor in self.ice_cream_stand.flavors:
                flavor_label = tk.Label(self.root, text=flavor)
                flavor_label.pack()

            self.root.mainloop()

    if __name__ == "__main__":
        ice_cream_stand = IceCreamStand("Cool Treats", ["Vanilla", "Chocolate", "Strawberry", "Mint"])
        ice_cream_stand.display_flavors()

        app = IceCreamApp(ice_cream_stand)
zad3()