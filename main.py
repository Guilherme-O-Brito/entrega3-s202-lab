from database import Database
from pokedex import Pokedex

if __name__ == '__main__':
    db = Database(database='pokedex', collection='pokemons')
    pokedex = Pokedex(db)

    pokemons = pokedex.search_by_name('Charmander')

    types = ['Fire', 'Water', 'Grass']

    pokemons = pokedex.search_by_types(types)

    pokemons = pokedex.search_by_2_evolutions()

    pokemons = pokedex.search_by_number_of_weaknesses(2)

    types = ['Electric']

    pokemons = pokedex.search_by_type_of_weakness(types)
