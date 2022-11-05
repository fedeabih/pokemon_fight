from common_utils import get_args

def main():
    args = get_args()

    pokemon1    =   args.pokemon1
    pokemon2    =   args.pokemon2

    print(f"Starting the fight: {pokemon1} vs {pokemon2}")

if __name__ == '__main__':
    main()


