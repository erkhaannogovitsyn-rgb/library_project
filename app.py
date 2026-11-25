def check_availability(books_count: int) -> bool:
    """Проверяет, доступна ли книга для бронирования."""
    return books_count > 0

def calculate_fine(days_overdue: int) -> int:
    """Считает штраф за просрочку: 5 рублей за каждый день."""
    if days_overdue <= 0:
        return 0
    return days_overdue * 5
