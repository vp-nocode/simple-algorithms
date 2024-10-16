'''
Алгоритм для определения является ли строка палиндромом
1. Приведение строки к нижнему регистру
2. Удаление из строки пробелов и всех символов, кроме цифр и букв
3. Инвертирование строки
4. Сравнение исходной и инвеертированной строк - если равны, то строка -
    палиндром (True), иначе не палиндром (False)
'''

def is_palindrome(s):
    # Приведение строки к нижнему регистру и удаление пробелов
    s = s.lower().replace(" ", "")
    # Удаление всех символов, кроме букв и цифр
    s = ''.join(char for char in s if char.isalnum())
    # Проверка является ли строка палиндромом
    return s == s[::-1]

print(is_palindrome("А роза упала на лапу Азора"))  # True
print(is_palindrome("Тут как тут"))                        # True
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Was it a car or a cat I saw"))  # True
print(is_palindrome("Hello, World!"))                # False
