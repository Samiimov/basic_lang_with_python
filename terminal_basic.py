from basic import BasicLang
def basic_terminal():
    basic = BasicLang()
    line = 10
    while True:
        user_input = input(str(line) + " : ")
        basic.handle_input(user_input)
        line += 10

if __name__ == "__main__":
    basic_terminal()