def find_lock_code():
    lock_code = 0
    for number in range(1, 1001):
        if number % 3 == 0 or number % 5 == 0:
            lock_code += number
    return lock_code

# Kincsesláda számzár kódja
kod = find_lock_code()
print("A kincsesláda számzár kódja:", kod)
