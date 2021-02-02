from pyrustic.app import App
from jupitest import about
from jupitest.misc.builder import MainViewBuilder
from jupitest.misc import my_theme


def main():
    app = App(about.ROOT_DIR)
    app.root.title("Jupitest - Pyrustic Test Runner")
    app.theme = my_theme.get_theme()
    app.view = MainViewBuilder().build(app)
    app.center()
    app.start()

if __name__ == "__main__":
    main()
