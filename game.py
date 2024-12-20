# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms
class Room:
    def __init__(self, name, description, quest, number):
        self.name = name
        self.description = description
        self.quest = quest
        self.number = number
        self.exits = {}

corridor_infini = Room(
    "Corridor Infini",
    "Un couloir interminable avec des néons grésillants et un sol carrelé beige.",
    "Résolvez un puzzle de répétition pour obtenir le chiffre 1.",
    1
)
self.rooms.append(corridor_infini)

bureau_abandonne = Room(
    "Bureau Abandonné",
    "Un espace de bureaux désordonné où des téléphones sonnent sporadiquement.",
    "Trouvez des indices dans le chaos pour révéler le chiffre 2.",
    2
)
self.rooms.append(bureau_abandonne)

souterrain_inonde = Room(
    "Souterrain Inondé",
    "Une pièce immergée avec des conduites rouillées et des reflets inquiétants.",
    "Naviguez prudemment pour découvrir le chiffre 3.",
    3
)
self.rooms.append(souterrain_inonde)

chambre_rouge = Room(
    "Chambre Rouge",
    "Une pièce rouge oppressante avec des symboles cryptiques sur les murs.",
    "Déchiffrez les symboles pour obtenir le chiffre 4.",
    4
)
self.rooms.append(chambre_rouge)

labyrinthe_de_portes = Room(
    "Labyrinthe de Portes",
    "Un labyrinthe avec des portes qui mènent à différents endroits.",
    "Trouvez la bonne séquence pour récupérer le chiffre 5.",
    5
)
self.rooms.append(labyrinthe_de_portes)

chambre_du_gardien = Room(
    "Chambre du Gardien",
    "Une grande salle avec un trône au centre, occupée par un boss imposant.",
    "Affrontez le boss pour obtenir le chiffre 6.",
    6
)
self.rooms.append(chambre_du_gardien)
        

        # Create exits for rooms
corridor_infini.exits = {"E": bureau_abandonne}
bureau_abandonne.exits = {"E": souterrain_inonde, "O": corridor_infini}
souterrain_inonde.exits = {"S": chambre_rouge, "O": bureau_abandonne}
chambre_rouge.exits = {"N": souterrain_inonde, "S": labyrinthe_de_portes}
labyrinthe_de_portes.exits = {"N": chambre_rouge, "E": chambre_du_gardien}
chambre_du_gardien.exits = {"O": labyrinthe_de_portes}
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
