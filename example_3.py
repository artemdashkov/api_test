import random

len_articles = 10
list_1 = list(range(10))

print(list_1)

three_random_article = random.sample(list_1, 3)
three_random_article = sorted(three_random_article)
print(three_random_article)
