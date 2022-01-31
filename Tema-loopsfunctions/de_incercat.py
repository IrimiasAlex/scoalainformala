def este_int(n):
    try:
        int(n)
        print("Numarul", n, "este intreg")
    except ValueError:
        print(0)
este_int('abc')
