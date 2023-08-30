
class Superhero:
    def __init__(self, super_name, alias, power_level, superpower, weakness):
        self.super_name = super_name
        self.alias = alias
        self.power_level = power_level
        self.superpower = superpower
        self.weakness = weakness


batman = Superhero("Batman", "Bruce Wayne", 100, "Rich", "No parents")
superman = Superhero("Superman", "Clark Kent", 1000, "Everything", "Kryptonite")
wonder_woman = Superhero("Wonder Woman", "Diana Prince", 750, "Lasso of Truth", "Firearms")
flash = Superhero("Flash", "Barry Allen", 50, "Speed", "Cold")
green_lantern = Superhero("Green Lantern", "Hal Jordan", 500, "Willpower", "Yellow")
ironman = Superhero("Ironman", "Tony Stark", 100, "Smart", "Arrogance")
captain_america = Superhero("Captain America", "Steve Rogers", 500, "Morality and strength", "Naivety")
spiderman = Superhero("Spiderman", "Peter Parker", 500, "Spider stuff", "Mary Jane")
hulk = Superhero("Hulk", "Bruce Banner", 1000, "Strength", "Anger")
black_widow = Superhero("Black Widow", "Natasha Romanoff", 250, "Espionage", "Brainwashing")
thor = Superhero("Thor", "Thor Odinson", 1000, "Lightning", "Unworthy")

superheroes = [
    batman,
    superman,
    wonder_woman,
    flash,
    green_lantern,
    ironman,
    captain_america,
    spiderman,
    hulk,
    black_widow,
    thor
]



for superhero in superheroes:
    print(f"{superhero.super_name} || {superhero.power_level}")