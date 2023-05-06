import random
import PySimpleGUI as sg


def generate_numbers():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(1, 9)) # Rastgele bir rakam ekle
    two_digit_number = random.randint(10, 99) # Rastgele 2 basamaklı sayı oluştur
    random_number = random.randint(500, 999) # 500 ile 999 arasında rastgele bir sayı oluştur
    numbers.append(two_digit_number)
    numbers.append(random_number)
    return numbers
def generate_letters():
    sessiz= ['b', 'c','ç', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    sesli = ['a', 'e', 'i', 'o','ö', 'u','ü','ı']
    letters = []
    for i in range(5):
        letters.append(random.choice(sessiz)) # Rastgele bir sessiz harf ekle
        letters.append(random.choice(sesli)) # Rastgele bir sesli harf ekle
    return letters

if __name__ == '__main__':
    sayilar = generate_numbers()
    harfler = generate_letters()
    layout = [[sg.Canvas(size=(300))],
            [sg.Text(', '.join(map(str,sayilar)), font=50)],
            [sg.Text(', '.join(harfler), font=50)],
            [sg.Exit('Kapat')] ]
    window = sg.Window('Bir sayi bir kelime', layout)
    event, values = window.read()
    if event == 'Exit':
        window.close()