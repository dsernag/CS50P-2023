def convert(mass):
    C__ = 300000000
    return mass * (C__ **2)

if __name__ == "__main__":
    mass = int(input("m: "))
    energy = convert(mass)
    print(f"E: {energy}")