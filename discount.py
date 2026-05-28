def apply_discount(amount, discount_percent):
    """Возвращает сумму после применения процентной скидки."""
    if not isinstance(amount, (int, float)):
        raise TypeError("Сумма должна быть числом")
    if not isinstance(discount_percent, (int, float)):
        raise TypeError("Скидка должна быть числом")
    if amount < 0:
        raise ValueError("Сумма не может быть отрицательной")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100")

    discount_value = amount * (discount_percent / 100)
    final_amount = amount - discount_value
    print(final_amount)
    return final_amount


if __name__ == "__main__":
    apply_discount(1000, 15)
