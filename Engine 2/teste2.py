def funcao(a, b, ref, func):
    if (a == ""):
        print("A nulo")
    if (b == ""):
        print("B nulo")
    if (ref == ""):
        print("ref nulo")
    if (func == ""):
        print("func nulo")
    print("*** FIM ***")


def main():
    funcao(1, 2, 3, 4);
    funcao("", "", "ref", "func")
    funcao(1, 2, "", "")


if __name__ == "__main__":
    main()
