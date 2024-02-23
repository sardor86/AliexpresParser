from drivers import Parser


def main():
    category_name = input("Enter category name: ")

    driver = Parser()
    driver.get_category()
    driver.get_products_list(category_name)


if __name__ == '__main__':
    main()
