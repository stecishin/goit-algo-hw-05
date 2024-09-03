def caching_fibonacci():
    # Ініціалізуємо словник cache для зберігання значень
    cache = {}
    
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Перевіряємо, чи є n вже в кеші; якщо так, повертаємо значення з кешу
        elif n in cache:
            return cache[n]
        # Рекурсивно обчислюємо значення для n-1 та n-2, додаємо їх та зберігаємо в кеш
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
     
    return fibonacci

caching_fibonacci()


fib = caching_fibonacci()

print(fib(10))
print(fib(15))
