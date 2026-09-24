words = ["苹果", "香蕉", "苹果", "橙子", "香蕉", "苹果"]
fruit = {}
for word in words:
    current_word = word
    fruit[current_word] = fruit.get(current_word,0) + 1
print(fruit)