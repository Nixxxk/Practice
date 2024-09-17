if __name__ == '__main__':
    alist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_heighest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_heighest])))