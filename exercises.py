### FIZZ BUZZ ###

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()

### ANAGRAMS ###

word1_test_a = ("Hello")
word2_test_a = ("One")

word1_test_b = ("State")
word2_test_b = ("Taste")

def anagrams(word1, word2):
    if sorted(word2.lower()) == sorted(word1.lower()):
        return True
    else:
        return False

print(anagrams(word1_test_a, word2_test_a))
print(anagrams(word1_test_b, word2_test_b))