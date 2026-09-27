def encryption(P: list, B: list, K: list[int]):
    if len(K) != len(P):
        print("Неверный размер K")
        return None
    for p in P:
        if p not in B:
            print(f"Байта {p} нет в алфавите")
            return None

    C = [None] * len(P)
    for i in range(len(K)):
        k = K[i]
        if not (1 <= k <= len(P)):
            print(f"Неверное значение ключа: {k}")
            return None
        C[i] = P[k - 1]
    return C


def preprocessing(P: str, B: str, K: str):
    P_list = P.split(",")
    B_list = B.split(",")
    K_list = K.split(",")
    P_list = [int(x.strip()) for x in P_list]
    B_list = [int(x.strip()) for x in B_list]
    K_list = [int(x.strip()) for x in K_list]
    return P_list, B_list, K_list


if __name__ == "__main__":
    # P = [75,73,76,73,77,81,74, 78, 77,75,77]
    # B = [72,73,74,75,76,77,78,79,80,81]
    # K = [4,7,1,9,3,6,2,11,8,10,5]

    P = input("Введите строку байт открытого текста: ")
    B = input("Введите алфавит: ")
    K = input("Введите ключ: ")
    C = encryption(*preprocessing(P, B, K))
    print(f"Шифровка: {C}")
