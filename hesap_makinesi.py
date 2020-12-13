print("""
Sihirli Hesap Makinesi'ne Hoşgeldiniz

1. işlem = toplama
2. işlem = çıkarma
3. işlem = çarpma 
4. işlem = bölme
""")

x = int(input("1. sayıyı giriniz: "))
y = int(input("1. sayıyı giriniz: "))

islem = int(input("işlemi giriniz: "))

if islem == 1:
    print("{} ile {} nin toplamı = {}".format(x,y,x+y))
elif islem == 2:
    print("{} ile {} nin çıkarımı = {}".format(x, y, x - y))
elif islem == 3:
    print("{} ile {} nin çarpımı = {}".format(x, y, x * y))
elif islem == 4:
    print("{} ile {} nin bölümü = {}".format(x, y, x / y))
else:
    print("hatalı giriş")