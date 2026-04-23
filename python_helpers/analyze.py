import argparse, os
import numpy as np

'''
Prints information about frame times from input data file.
The frame times are assumed to be in milliseconds and separated by newlines.
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to input file")
    parser.add_argument("-r", "--raw", action="store_true", help="print frame times as a list, to facilitate copying to say html")
    parser.add_argument("--ignore", "-i", type=int, default=0, help="number of initial frame times to ignore (e.g. to ignore warmup frames)")
    args = parser.parse_args()

    if os.path.isdir(args.input_path):
        names, averages, stds = [], [], []
        for e in os.scandir(args.input_path):
            if e.is_file() and e.name.endswith(".txt"):
                with open(e.path, "r") as f:
                    times = np.array([float(line.strip()) for line in f if line.strip()[0] != "#"])
                times = times[args.ignore:]
                names.append(e.name)
                if args.raw:
                    print(f"{e.name}:")
                    print("[", ", ".join(times.astype(str)), "]")
                else:
                    averages.append(times.mean().item())
                    stds.append(times.std().item())
        if not args.raw:
            print(f"names: {names}")
            print(f"average (ms): {averages}")
            print(f"stddev (ms): {stds}")
    else:
        with open(args.input_path) as f:
            times = np.array([float(line.strip()) for line in f if line.strip()[0] != "#"])
        times = times[args.ignore:]
        if args.raw:
            print("[", ", ".join(times.astype(str)), "]")
        else:
            print(f"average: {times.mean()} ms")
            print(f"stddev: {times.std()} ms")