import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f", default="_temp.txt", help="name of output file")
    parser.add_argument("--num_steps", "-n", type=int, default=100, help="number of frames to render")
    parser.add_argument("--fps", type=int, default=60, help="frames per second to render at")
    parser.add_argument("--render_dir", "-r", default="", help="render frames to output directory")
    args = parser.parse_args()

    dt = 1 / args.fps
    with open(args.filename, "w") as f:
        for i in range(args.num_steps):
            line = f"AVAILABLE {dt}\n" if args.render_dir == "" else f"AVAILABLE {dt} {args.render_dir}/frame_{i}.ppm\n"
            f.write(line)