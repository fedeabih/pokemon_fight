from common_utils import get_args
import pypokedex
import sys

def main():
    args = get_args()

    pokemons    =   {
        args.pokemon1.capitalize(): 0,
        args.pokemon2.capitalize(): 0
    }

    for key in pokemons.keys():
        try:
            poke            =   pypokedex.get(name=key)
            pokemons[key]   =   poke.base_stats.attack
        except Exception as e:
            print(f'{e}: {key}')
            sys.exit(1)

    print(f'\nStarting the fight:')

    if len(pokemons) < 2:
        print(f'{key} ({pokemons[key]}) vs {key} ({pokemons[key]})')

        poke_winner     =   key

    else:
        for key in pokemons.keys():
            print(f'{key} ({pokemons[key]})',end=' ')
            if key != list(pokemons.keys())[-1]:
                print('vs',end=' ')
            else:
                print('\n')
        
        poke_winner     =   [key for key, value in pokemons.items() if value == max(pokemons.values())]

    if len(poke_winner) >= 2:
        print('\nThe battle ends in a draw.')
    else:
        print(f'The winner is {poke_winner[0]}!!')

if __name__ == '__main__':
    main()


