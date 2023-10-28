# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44
numbers_of_pages = 100
numbers_of_strings = 50
numbers_of_symbols = 25
for_one_symbol = 4

symbols_on_the_page = numbers_of_symbols * numbers_of_strings
symbols_in_the_book = symbols_on_the_page * numbers_of_pages
volume_for_one_book = for_one_symbol * symbols_in_the_book
bayts = volume * 1024 * 1024
print("Количество книг, помещающихся на дискету:", int(bayts // volume_for_one_book))
