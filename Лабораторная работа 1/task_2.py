# TODO Найдите количество книг, которое можно разместить на дискете
volume_Mbytes = 1.44 #байт Мб
pages = 100
strings = 50
symbols = 25
heavy_symbols_bytes = 4 #байт
heavy_whole_book_bytes = pages * strings * symbols * heavy_symbols_bytes
heavy_whole_book_Mbytes = heavy_whole_book_bytes / 1024 / 1024
books_count = int(volume_Mbytes//heavy_whole_book_Mbytes)
print("Количество книг, помещающихся на дискету:", books_count)
