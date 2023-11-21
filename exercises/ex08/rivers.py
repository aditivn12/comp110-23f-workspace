"""File to define River class"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:
    """This creates a river oject."""
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and creates a new list."""
        age_fish: list[Fish] = []
        age_bear: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                age_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                age_bear.append(bear)
        return None

    def bears_eating(self):
        "Function to stimulate bears eating."
        for bear in self. bears:
            if len(self.fish) > 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def remove_fish(self, amount:int):
        """Removes specific fish amounts."""
        remove_fish: list[Fish] = []
        for fish in self.fish:
            if amount > 0:
                remove_fish.append(fish)
        
        for i in range(0, len(remove_fish)):
            self.fish.remove(remove_fish[i])

    def check_hunger(self):
        """Checks the hunger score of the bears."""
        checking_hunger: list[Bear] = []
        for i in self.bears:
            if i.hunger_score < 0:
                checking_hunger.append(i)
        for i in range(0, len(checking_hunger)):
            self.bears.append(Bear())
        return None

    def repopulate_fish(self):
        """Repopulates the fish in the river."""
        fish_count: int = len(self.bears) // 2 * 4
        for i in range(0, fish_count):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Repopulates the bears in the river."""
        bear_count: int = len(self.bears) // 2
        for i in range(0, bear_count):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """River information function."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()

        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """One week in the river."""
        for i in range(0,7):
            self.one_river_day()