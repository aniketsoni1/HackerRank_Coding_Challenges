def recursion_sum(n):  # 3
    if n == 0:
        return 0
    else:
        return n + recursion_sum(n - 1)  # 3 + r(2) | 3 + 2 + r(1) + 3 + 2 +1 +r(0)


print(recursion_sum(3))  # 3+2+1 = 6


def recursion_mod(n):  # 4321
    if len(str(n)) == 1:
        return str(n)
    else:
        return recursion_mod(n // 10) + '+' + str(n % 10)  # r(432) + 1 | r(43) + 2 + 1 | r(4) + 3 + 2 +1


print(recursion_mod(4321))  # 4+3+2+1


def word_split(phrase, list, output=None):  # w(themanran, ['the', 'ran', 'man'], None) |  w(manran, ['the', 'ran', 'man'], ['the']) | w(ran, ['the', 'ran', 'man'], ['the', 'man'])
    if output is None:
        output = []

    for word in list:  # ['the', 'ran', 'man']
        if phrase.startswith(word): #
            output.append(word)
            return word_split(phrase[len(word):], list, output)  # w('', ['the', 'ran', 'man'], ['the', 'man', 'ran'])

    return output


print(word_split('themanran', ['the', 'ran', 'man']))
print(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
print(word_split('themanran', ['clown', 'ran', 'man']))
