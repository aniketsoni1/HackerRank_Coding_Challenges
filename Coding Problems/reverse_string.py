"""
hello
01234
ello + h   ->  reverse(s[1:]) + s[0]
llo + e + h
lo + l + e + h
o + l + l + e + h
''olleh
"""


def reverse(s):
    if len(s) <= 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


print(reverse('hello'))  # 'olleh'
print(reverse('hello world'))
print(reverse('world'))
print(reverse('12345'))
print(reverse(''))