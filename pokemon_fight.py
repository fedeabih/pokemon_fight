from common_utils import get_args
import pypokedex

def main():
    args = get_args()

    pokemons    =   {
        0: [args.pokemon1, 0],
        1: [args.pokemon2, 0]
    }

    print(f"Starting the fight: {pokemons[0][0]} vs {pokemons[1][0]}")

    for _, value in pokemons.items():
        print(value[1])
        try:
            poke        =   pypokedex.get(name=value[0])
            value[1]    =   poke.base_stats.attack
        except Exception as e:
            print(e)
    
    print(pokemons)





if __name__ == '__main__':
    main()


