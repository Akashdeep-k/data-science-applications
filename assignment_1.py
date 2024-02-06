# 1
s = "Hi there Class!"
ans = s.split()
print(ans)

# 2
planet = "Earth"
diameter = 12742
ans = "The diameter of {} is {}".format(planet, diameter)
print(ans)

# 3
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

# 4
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

# 5
def get_email(email):
    try:
        l1 = email.split('@')[1]
        l2 = l1.split('.')[1]
        return True
    except IndexError:
        return False

print(get_email("user@domain.com"))

# 6 & 7
def count_dog(text):
    return text.lower().count('dog')

print(count_dog("I have a dog and my neighbor has a dog too."))

# 8
seq = ['soup', 'dog', 'salad', 'cat', 'great']
filtered_seq = list(filter(lambda word: word[0].lower() == 's', seq))
print(filtered_seq)

# 9
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return "No Challan"
    elif 61 <= speed <= 80:
        return "Small Challan"
    else:
        return "Heavy Challan"

print(caught_speeding(81, True))
print(caught_speeding(81, False))

# 10
list1 = ["M", "na", "i", "She"]
list2 = ["y", "me", "s", "lly"]
ans = [a + b for a, b in zip(list1, list2)]
print(ans)

# 11
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
ans = [a + b for a in list1 for b in list2]
print(ans)

# 12
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# 13
list1 = [5, 20, 15, 20, 25, 50, 20]
list1 = [x for x in list1 if x != 20]
print(list1)

# 14
d1 = {'a': 100, 'b': 200, 'c': 300}
print(200 in d1.values())

# 15
def sum_of_series(n):
    series_sum = 0
    current_term = 2
    for _ in range(n):
        series_sum += current_term
        current_term = current_term * 10 + 2
    return series_sum

n_terms = 5
ans = sum_of_series(n_terms)
print(ans)