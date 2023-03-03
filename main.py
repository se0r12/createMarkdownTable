import sys
def main():
    width: int = int(sys.argv[1])
    height: int = int(sys.argv[2])

    print("|" * (width + 1))
    print("|----" * (width), end="|\n")
    for i in range(0, height):
        print("|" * (width + 1))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("usage: python main.py number(横) number(縦)")
        quit(1)
    main()
