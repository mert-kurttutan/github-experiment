

if __name__ == '__main__':
    import argparse
    # take single cli integer argument
    parser = argparse.ArgumentParser(description="This script takes a single integer argument")
    parser.add_argument("integer", type=int, help="an integer")
    args = parser.parse_args()
    print(f"Argument: {args.integer}")