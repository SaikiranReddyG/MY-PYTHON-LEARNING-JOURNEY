import asyncio
from random import randint
#from req_http import http_get, http_get_sync
#the highest pokemon id
max_pokemon = 898


def get_random_pokemon_name_sync() -> str:
    pokemon_id = (1, max_pokemon)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon["name"])

async def get_random_pokemon_name() -> str:
    pokemon_id = (1, max_pokemon)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


async def main()  -> None :
    for i in range(20):
    pokemon_name = get_random_pokemon_name_sync()
    print(pokemon_name)

if __name__ == '__main__':
     asyncio.run(main())