def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    try:
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                return "Sıfıra bölme hatası!"
            result /= num
        return result
    except ZeroDivisionError:
        return "Sıfıra bölme hatası!"

def get_numbers():
    numbers = []
    print("Lütfen sayıları girin (işlem tamamlandığında 'a' tuşuna basın):")
    while True:
        entry = input("Sayı girin: ")
        if entry.lower() == 'a':
            if len(numbers) > 1:
                return numbers
            else:
                print("En az iki sayı girmeniz gerekiyor. Lütfen tekrar girin.")
        else:
            try:
                number = float(entry)
                numbers.append(number)
            except ValueError:
                print("Geçersiz giriş. Lütfen geçerli bir sayı girin.")

def get_operation():
    print("Yapmak istediğiniz işlemi seçin:")
    print("1: Toplama")
    print("2: Çıkarma")
    print("3: Çarpma")
    print("4: Bölme")

    while True:
        choice = input("Seçiminizi yapın (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Geçersiz seçim. Lütfen 1, 2, 3 veya 4 seçin.")

def calculate(numbers, operation):
    if operation == '1':
        return add(numbers)
    elif operation == '2':
        return subtract(numbers)
    elif operation == '3':
        return multiply(numbers)
    elif operation == '4':
        return divide(numbers)

def main():
    print("Hesap Makinesine Hoşgeldiniz!")

    numbers = get_numbers()
    operation = get_operation()

    result = calculate(numbers, operation)

    operations = {
        '1': "Toplama",
        '2': "Çıkarma",
        '3': "Çarpma",
        '4': "Bölme"
    }

    print(f"Seçilen işlem: {operations[operation]}")
    print(f"Sonuç: {result}")

if __name__ == "__main__":
    main()
