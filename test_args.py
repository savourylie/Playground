import argparse


def get_arguments():
    """Parse all the arguments provided from the CLI.

    Returns:
      A list of parsed arguments.
    """
    parser = argparse.ArgumentParser(description="argparse demo.")

    parser.add_argument("--a", type=int, help="argument 1")
    parser.add_argument("--b", type=int, help="argument 2")

    parser.error('Test parser error.')
    
    return parser.parse_args()


if __name__ == '__main__':
    args = get_arguments()


    print(type(args))
    print(args)
    print(args.a)
    print(args.b)
