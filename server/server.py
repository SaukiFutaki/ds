import Pyro5.api
import Pyro5.server


@Pyro5.api.expose
class CalculatorServer:
    def add(self, x, y):
        """Fungsi penjumlahan"""
        return x + y

    def subtract(self, x, y):
        """Fungsi pengurangan"""
        return x - y

    def multiply(self, x, y):
        """Fungsi perkalian"""
        return x * y

    def divide(self, x, y):
        """Fungsi pembagian"""
        if y == 0:
            raise ValueError("Pembagian oleh nol tidak diizinkan")
        return x / y


def main():
    daemon = Pyro5.api.Daemon(host='0.0.0.0')
    ns = Pyro5.api.locateNS()
    uri = daemon.register(CalculatorServer)
    ns.register("calculator.server", uri)

    print(f"Calculator server siap. URI: {uri}")
    daemon.requestLoop()


if __name__ == "__main__":
    main()