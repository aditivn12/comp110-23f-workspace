from exercises.ex08.bear import Bear
from exercises.ex08.fish import Fish

class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]
    def __init__(self, num_fish: int, num_bears: int, day: int = 0):
        self.fish: list[Fish] = []
        for i in range(0, num_fish):
            self.fish.append(Fish())
        self.bears: list[Bear] = []
        for i in range(0, num_bears):
            self.bears.append(Bear())
        self.day: int = 0
    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~ \n")
        print(f"Fish population: {len(self.fish)}")
        print (f"Bear population: {len(self.bears)}")



    