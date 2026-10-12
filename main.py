def find_DDT(S: list[int], N: int) -> list:
    DDT = [[0] * N for _ in range(N)]
    for delta_X in range(N):
        for X in range(N):
            delta_Y = S[X] ^ S[X ^ delta_X]
            DDT[delta_X][delta_Y] += 1
    return DDT



if __name__ == '__main__':
    # S = [0, 2, 13, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 14, 15]
    # S = [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15]
    S = list(map(int, input("S: ").split(", ")))
    N = len(S)
    DDT = find_DDT(S, N)
    print("\t".join(["X"] + [str(x) for x in range(N)]))
    for i in range(N):
        print("\t".join([str(i)] + [str(x) for x in DDT[i]]))
