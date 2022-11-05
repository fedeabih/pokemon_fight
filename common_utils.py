import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Pokemon Fight!')

    # Required Positional

    parser.add_argument('pokemon1', type=str, default='',
                        help = 'Select the Pokemon 1 to fight.')
    parser.add_argument('pokemon2', type=str, default='',
                        help = 'Select the Pokemon 2 to fight.')

    return parser.parse_args() 