from drivers import AliexpressParser


def main():
    driver = AliexpressParser()
    driver.get_category()
    for category in driver.category:
        print(f'category: {driver.category[category]}')
    print(driver.get_products_list('Компьютеры'))


if __name__ == '__main__':
    main()
