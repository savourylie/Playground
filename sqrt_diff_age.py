def get_age_pair_from_sq_diff(low, high, diff=195):
    for i in range(low, high):
        for j in range(i + 1, high + 1):
            if j**2 - i**2 == diff:
                print(i, j)

if __name__ == '__main__':
    # print("Old: (60, 100)")
    get_age_pair_from_sq_diff(10, 120)


