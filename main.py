from parser_class import Parser


def main():
    try:
        #list = [0 - ID, 1 - NAME, 2 - ID, 3 - ID, 4 - CSS.SELECTOR](index - element)
        list = ["oper_user", "passwd", "capcher", "cap_field", "input[value='Войти']"]
        parser = Parser(
            'https://issaold.beltelecom.by/main.html',
            'https://www.prepostseo.com/ru/image-to-text',
            'HelloWorld',
            '1234567809', 
            list)

        parser.byflyRegistration()
    except Exception:
        parser.byflyRegistration()
    finally:
        print('BEBRA')


if __name__ == '__main__':
    main()