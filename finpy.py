"""
Financial functions and modeling
"""

from __future__ import print_function


def calc_total_price(sale_price, sales_tax=0.1025):
    """Calculate total price given base and sales tax."""
    return sale_price + (sale_price * sales_tax)


if __name__ == '__main__':
    base_price = 4.99
    total_price = calc_total_price(base_price)
    print(f'Base price: ${base_price:,.2f} '
          f'- total price: ${total_price:,.2f}')
