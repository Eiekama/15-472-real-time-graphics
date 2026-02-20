import argparse
import numpy as np

'''
Prints information about frame times from input file.
The frame times are assumed to be in milliseconds and separated by newlines.
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to input file")
    parser.add_argument("-r", "--raw", action="store_true", help="print frame times as a list, to facilitate copying to say html")
    args = parser.parse_args()

    with open(args.input_path) as f:
        times = np.array([float(line.strip()) for line in f])
    if args.raw:
        print("[", ", ".join(times.astype(str)), "]")
    else:
        print(f"average: {times.mean()} ms")
        print(f"stddev: {times.std()} ms")