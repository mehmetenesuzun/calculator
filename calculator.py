# This is a test change to trigger a commit.
#!/usr/bin/env python3

def add(a, b):
    """İki sayıyı toplar."""
    return a + b

def subtract(a, b):
    """İki sayı arasındaki farkı verir."""
    return a - b

def multiply(a, b):
    """İki sayıyı çarpar."""
    return a * b

def divide(a, b):
    """İki sayıyı böler; sıfıra bölme hatasını kontrol eder."""
    if b == 0:
        raise ValueError("Sıfıra bölme hatası: İkinci sayı sıfır olamaz!")
    return a / b

def main():
    print("Basit Komut Satırı Hesap Makinesi")
    print("Çıkmak için 'q' tuşlayın.\n")
    
    while True:
        try:
            num1_input = input("İlk sayı: ")
            if num1_input.lower() == 'q':
                print("Çıkış yapılıyor...")
                break
            num1 = float(num1_input)

            operator = input("İşlem seçiniz (+, -, *, /): ")
            if operator.lower() == 'q':
                print("Çıkış yapılıyor...")
                break

            num2_input = input("İkinci sayı: ")
            if num2_input.lower() == 'q':
                print("Çıkış yapılıyor...")
                break
            num2 = float(num2_input)

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Geçersiz operatör girdiniz. Lütfen (+, -, *, /) kullanın.\n")
                continue

            print(f"Sonuç: {result}\n")

        except ValueError as ve:
            # Kullanıcı geçerli bir sayı girmediyse veya sıfıra bölmeye çalıştıysa
            print(f"Hata: {ve}\n")
        except Exception as e:
            print(f"Beklenmeyen hata: {e}\n")

if __name__ == '__main__':
    main()
