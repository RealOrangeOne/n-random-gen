#!/usr/bin/env python3
import argparse
import secrets


def main(count, min_value, max_value):
    assert count > 0
    assert min_value < max_value

    for i in range(count):
        print("{}: {}".format(i, secrets.choice(range(min_value, max_value + 1))))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int)
    parser.add_argument("min", type=int, help="(Inclusive)")
    parser.add_argument("max", type=int, help="(Inclusive)")

    args = parser.parse_args()

    main(args.count, args.min, args.max)
