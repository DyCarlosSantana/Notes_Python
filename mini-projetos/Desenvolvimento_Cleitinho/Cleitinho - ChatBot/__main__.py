from Interface import MeuApp
from rich.traceback import install
install()

if __name__ == "__main__":
    app = MeuApp()
    app.mainloop() 