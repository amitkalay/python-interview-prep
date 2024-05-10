import requests


def main() -> None:
    print("running the MAIN program")
    resp = requests.get('https://www.cnn.com/')
    print(f"cnn is: {resp}")


if __name__ == "__main__":
    main()
