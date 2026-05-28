def apply_discount(amount, discount_percent):
    """Возвращает сумму после применения процентной скидки."""
    discount_value = amount * (discount_percent / 100)
    final_amount = amount - discount_value
    print(final_amount)
    return final_amount


if __name__ == "__main__":
    apply_discount(1000, 15)
