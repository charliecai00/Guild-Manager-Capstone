# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

TEST_HERO = 'test_hero'
ID = 'id'
STATS = 'stats'
ITEMS = 'items'
NAME = 'name'
HERO_ID = 'HERO_ID'
HEALTH = 'health'
ALIVE = 'alive'
COST = 'cost'
REQUIRED_FLDS = [ID, STATS, ITEMS, NAME, HERO_ID, HEALTH, ALIVE, COST]

dummy_hero = {TEST_HERO: {ID: 1,
                          STATS: {"STR": 20, "CON": 20, "DEX": 20, "WIS": 20, "INT": 20, "CHA": 20},
                          ITEMS: [],
                          NAME : "1",
                          HERO_ID: 1,
                          HEALTH: 2,
                          ALIVE: True,
                          COST: 5
                          }}


def hero_exists(name):
    """
    Returns whether or not a hero exists.
    """
    return name in dummy_hero


def get_heros():
    return list(dummy_hero.keys())


def get_heros_dict():
    return dummy_hero


def get_hero_details(hero):
    return dummy_hero.get(hero, None)


def del_hero(name):
    del dummy_hero[name]


def add_hero(name, details):
    dummy_hero[name] = details


def main():
    print(hero_exists(TEST_HERO))
    print(get_heros())
    print(get_heros_dict())
    print(get_hero_details(TEST_HERO))
    del_hero(TEST_HERO)
    add_hero(TEST_HERO, "Testing add_hero()")


if __name__ == '__main__':
    main()
