# Assignment 1: Design Your Own Class (Smartphone)

class Smartphone:
    """
    A class representing a generic smartphone.
    
    This class demonstrates attributes, methods, a constructor, and encapsulation
    by managing a private battery level.
    """

    def __init__(self, brand: str, model: str, battery_level: int = 100):
        """Initializes a new Smartphone object."""
        self.brand = brand
        self.model = model
        self._battery_level = max(0, min(100, battery_level))  # Encapsulated attribute
        self.installed_apps: list[str] = []

    def charge(self, amount: int) -> str:
        """Charges the phone and returns the new battery level."""
        self._battery_level = min(100, self._battery_level + amount)
        return f"Charging... Battery is now {self._battery_level}%"

    def use_app(self, app_name: str, minutes: int) -> str:
        """Simulates using an app, which drains the battery."""
        if app_name not in self.installed_apps:
            return f"Error: '{app_name}' is not installed."
        
        drain = max(1, minutes // 5)
        self._battery_level = max(0, self._battery_level - drain)
        return f"Used {app_name} for {minutes} min. Battery is now {self._battery_level}%"

    def install_app(self, app_name: str) -> str:
        """Installs a new app if it's not already installed."""
        if app_name not in self.installed_apps:
            self.installed_apps.append(app_name)
            return f"{app_name} installed successfully."
        return f"'{app_name}' is already installed."

    def __str__(self) -> str:
        """Provides a user-friendly string representation of the object."""
        return f"{self.brand} {self.model} (Battery: {self._battery_level}%)"

class GamingPhone(Smartphone):
    """
    A subclass of Smartphone specializing in gaming.
    
    This class demonstrates inheritance and polymorphism by overriding the
    use_app method to simulate higher battery drain for gaming.
    """
    
    def __init__(self, brand: str, model: str, battery_level: int = 100):
        """Initializes a new GamingPhone object."""
        super().__init__(brand, model, battery_level)
        
    def use_app(self, app_name: str, minutes: int) -> str:
        """Simulates a heavier battery drain when a gaming app is used."""
        if app_name not in self.installed_apps:
            return f"Error: '{app_name}' is not installed."

        gaming_drain = max(1, minutes // 2)  # Higher drain for gaming
        self._battery_level = max(0, self._battery_level - gaming_drain)
        return f"Gaming on {app_name} for {minutes} min. Battery is now {self._battery_level}%"

# Activity 2: Polymorphism Challenge (Vehicles)


class Mover:
    """An abstract base class for any object that can move."""
    
    def move(self) -> str:
        """Defines the abstract 'move' method that subclasses must implement."""
        pass

class Car(Mover):
    """A Car class that defines a unique way to move."""
    def move(self) -> str:
        return "Driving"

class Plane(Mover):
    """A Plane class that defines a unique way to move."""
    def move(self) -> str:
        return "Flying"

class Boat(Mover):
    """A Boat class that defines a unique way to move."""
    def move(self) -> str:
        return "Sailing"

def demonstrate_polymorphism(movers: list[Mover]) -> None:
    """
    Takes a list of Mover objects and calls the 'move' method on each.
    
    This function demonstrates polymorphism as the same method call
    produces a different result for each object type.
    """
    for mover in movers:
        print(f"{mover.__class__.__name__}: {mover.move()}")
