import sys


def main():
    height = int(input("Height: "))
    if height >=20:
        main()
    else




def draw_pyramid(height):
    for i in range(1, height + 1, 1):
        for j in range(1, i + 1, 1):
            print("x", end="")
        print()


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
