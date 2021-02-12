#
import BrowserFrame


def main():
    Frame = BrowserFrame.BrowserFrame()

    Frame.add_link("https://tv2.dk/")
    Frame.add_link("https://en.hbonordic.com/")

    Frame.execute()

    pass


if __name__ == '__main__':
    main()
