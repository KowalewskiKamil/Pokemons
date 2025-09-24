import pandas as pd
import random as rd

class Pokemon:
    df = pd.read_csv("pokemon.csv").set_index("Name")
    def __init__(self, name: str):
        if name not in Pokemon.df.index:
            raise ValueError(f"Pokemon '{name}' nie istnieje w bazie!")
        self.name = name
        stats = Pokemon.df.loc[name]
        self.hp = stats["HP"]
        self.attack = stats["Attack"]
        self.defense = stats["Defense"]
        self.sp_attack = stats["Sp. Atk"]
        self.sp_defense = stats["Sp. Def"]
        self.speed = stats["Speed"]
def fight(pokemon_name1, pokemon_name2):
    pokemon1, pokemon2 = Pokemon(pokemon_name1), Pokemon(pokemon_name2)
    speed_bar1, speed_bar2 = pokemon1.speed, pokemon2.speed
    while pokemon1.hp > 0 and pokemon2.hp > 0:
        if speed_bar1 > speed_bar2:
            if pokemon1.sp_attack >= pokemon2.sp_defense:
                speed_bar1 -= 30
                if pokemon2.defense >= pokemon1.attack:
                    pokemon2.defense -= 20
                    pokemon2.sp_defense -= 20
                else:
                    pokemon2.hp -= (pokemon1.sp_attack - pokemon2.sp_defense)
                    if pokemon2.hp <= 0:
                        return pokemon1.name
                    pokemon2.sp_defense += 10
                    pokemon2.attack += 10
                    pokemon2.sp_attack += 20
            else:
                pokemon2.sp_defense -= 20
        else:
            if pokemon2.sp_attack >= pokemon1.sp_defense:
                speed_bar2 -= 30
                if pokemon1.defense >= pokemon2.attack:
                    pokemon1.defense -= 20
                    pokemon1.sp_defense -= 20
                else:
                    pokemon1.hp -= (pokemon2.sp_attack - pokemon1.sp_defense)
                    if pokemon1.hp <= 0:
                        return pokemon2.name
                    pokemon1.sp_defense += 10
                    pokemon1.attack += 10
                    pokemon1.sp_attack += 20
            else:
                pokemon1.sp_defense -= 20

df = pd.read_csv("pokemon.csv").set_index("Name")
scores = {name: 0 for name in df.index}

for _ in range(10000):
    p1, p2 = rd.choice(Pokemon.df.index.tolist()), rd.choice(Pokemon.df.index.tolist())
    if fight(p1, p2) in scores:
        scores[fight(p1,p2)] += 1

Scores = pd.DataFrame.from_dict(scores, orient="index", columns=["Score"])
Scores = Scores.sort_values(by="Score", ascending=False)

print(Scores.to_string())