from random import randint, choice
from characters import CHARACTERS ,ENEMIES
from game_objects import GAME_OBJECTS
from game_map import GameMap


def get_trapped(character):
    print('You got trapped')
    damage = randint(5 ,25)
    character.get_damaged(damage)


def get_healed(character):
    print('You got healed')
    hp = randint(5 ,25)
    character.get_healed(hp)


def fight_with_enemy(character ,enemy):
    is_won = True

    while True:

        character.fight(enemy)

        if character.is_dead():
            is_won = False
            break
        elif enemy.is_dead():
            break

    return is_won

MOVE_DIRACTION = {'l', 'r', 'u', 'd', 'stop'}

print('Welcome to my game!')
name = input('Enter your name: ')
race = input('Choose race [Human, Orc, Elf]: ')
level = input('Difficulty [Hard, Medium, Easy]: ')

if level == 'Hard':
    objects = [ choice(GAME_OBJECTS)() for i in range(4) ]
    enemies = [ choice(ENEMIES)() for i in range(3) ]
    objects += enemies
elif level == 'Medium':
    objects = [choice(GAME_OBJECTS)() for i in range(3)]
    enemies = [choice(ENEMIES)() for i in range(2)]
    objects += enemies
elif level == 'Easy':
    objects = [choice(GAME_OBJECTS)() for i in range(3)]
    enemies = [choice(ENEMIES)() for i in range(1)]
    objects += enemies

x, y = randint(0, 4), randint(0, 4)
char = CHARACTERS[race](name, x, y)
char.show_stats()

game_map = GameMap(5, 5, objects)
game_map.put_char(char, *char.give_coords())


while True:

    print(game_map)

    while True:
        end_game = False
        move_diraction = input("Choose the way you go (L,R,D,U or stop): ")
        while move_diraction not in MOVE_DIRACTION:
            move_diraction = input("Choose the way you go (L,R,D,U or stop): ")
        if move_diraction == "l":
            move = (-1, 0)
        elif move_diraction == "r":
            move = (1, 0)
        elif move_diraction == "u":
            move = (0, -1)
        elif move_diraction == "d":
            move = (0, 1)
        elif move_diraction == "stop":
            break
        elif move_diraction is not "l" or move_diraction is not "r" or \
            move_diraction is not "d" or move_diraction is not "u" or move_diraction is not "stop":
            print("Please enter a proper direction")
        cur_pos = char.give_coords()
        next_pos = tuple(map(lambda a, b: a + b, cur_pos, move))

    for element in objects:
        if element.respond()[0] == next_pos:
            step = element.respond()[1]
        else: step = ''

        if step == 'Exit_door':
            print("\nYou won! Let's play one more time?" )
            end_game = 'Won'
            break
        elif step == 'Heal':
            get_healed(char)
        elif step == 'Trap':
            get_trapped(char)
            if char.is_dead():
                end_game = 'Lost'
                print('Sorry, you lost.')
                print('Game Over')
                break
        elif step == 'Undead' or step == 'Murloc':
            print ('\nYou have met an ENEMY ! ! !')
            is_won = fight_with_enemy(char, element)
            if not is_won:
                end_game = 'Lost'
                print('Sorry, you lost.')
                print('Game Over')
                break
        else: pass
    if not end_game:
        char.is_moving(move)
        new_pos = char.give_coords()

        game_map.is_moving(char, *cur_pos, *new_pos)
    else:
        break


