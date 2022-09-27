# 2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково слева-направо и справа-налево.
# Иначе – False.

def proverka(word):
    if word == word[::-1]: return True
    else: return False

print(proverka('шалаш'))
print(proverka('косяк'))
print(proverka('121'))
