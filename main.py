#Entry point for the Crisis Connect desktop application

from gui import CrisisConnectApp


def main() -> None:
    #Create and run the Crisis Connect application
    app = CrisisConnectApp()
    app.run()


if __name__ == "__main__":
    main()
