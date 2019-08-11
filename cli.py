import argparse

def main(count, max_value):
    assert count > 0
    assert max_value > 0

    print(count, max_value)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('count', type=int)
    parser.add_argument('max', type=int)

    args = parser.parse_args()
    main(args.count, args.max)
