from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    books_per_day = books_goal / 365
    if day_of_year is None:
        day_of_year = int(datetime.now().strftime("%j"))
    current_books_read = books_per_day * day_of_year
    return books_read >= current_books_read
