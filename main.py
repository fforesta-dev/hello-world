from hello.greeter import Greeter


def main():
    greeter = Greeter()
    message = greeter.greet()
    print(message)


if __name__ == "__main__":
    main()
