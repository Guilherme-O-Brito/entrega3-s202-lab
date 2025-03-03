from database import Database
from writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.db = database

    def search_by_name(self, name: str):
        query = self.db.collection.find({"name": name})
        writeAJson(query, name)
        return query
    
    def search_by_types(self, types: list):
        query = self.db.collection.find({"type": {"$in": types}})
        writeAJson(query, str(types))
        return query
    
    def search_by_2_evolutions(self):
        query = self.db.collection.find({
                "next_evolution": { "$exists": True, "$type": "array" },
                "$expr": { "$gt": [{ "$size": "$next_evolution" }, 1] }
            })
        writeAJson(query, 'pokemons-with-more-than-2-evolutions')
        return query
    
    def search_by_number_of_weaknesses(self, weaknesses: int):
        query = self.db.collection.find({"weaknesses": {"$size": weaknesses}})
        writeAJson(query, f'pokemons-with-{weaknesses}-weaknesses')    
        return query
    
    def search_by_type_of_weakness(self, types: list):
        query = self.db.collection.find({"weaknesses": {"$all": types}})
        writeAJson(query, f'pokemons-with-{str(types)}-weaknesses')
        return query
    
