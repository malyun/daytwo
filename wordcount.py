def words(strings):
    word = {}

    for j in strings.split():
        if j.isdigit():
            j = int(j)

        if word.get(j):
            word [j] += 1
        else:
            word [j] = 1

    return word

