import Pyro5.api

def main():

    ns = Pyro5.api.locateNS()
    uri = ns.lookup("calculator.server")
    calculator = Pyro5.api.Proxy(uri)

    while True:
        print("\n--- Kalkulator Pyro5 ---")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == '5':
            break

        try:
            x = float(input("Masukkan angka pertama: "))
            y = float(input("Masukkan angka kedua: "))

            if pilihan == '1':
                hasil = calculator.add(x, y)
                print(f"Hasil: {x} + {y} = {hasil}")
            elif pilihan == '2':
                hasil = calculator.subtract(x, y)
                print(f"Hasil: {x} - {y} = {hasil}")
            elif pilihan == '3':
                hasil = calculator.multiply(x, y)
                print(f"Hasil: {x} * {y} = {hasil}")
            elif pilihan == '4':
                hasil = calculator.divide(x, y)
                print(f"Hasil: {x} / {y} = {hasil}")
            else:
                print("Pilihan tidak valid!")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()