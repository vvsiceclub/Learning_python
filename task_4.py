import random


def get_jokes(n, repeat=False):

    result = []
    while n:
        if repeat:
            joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
            result.append(joke)
        else:
            joke = f'{nouns.pop(random.randrange(len(nouns)))} {adverbs.pop(random.randrange(len(adverbs)))} {adjectives.pop(random.randrange(len(adjectives)))}'
            result.append(joke)
        n -= 1
    return result


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

number = int(input("Введите количество шуток: "))

print(get_jokes(number, False))
