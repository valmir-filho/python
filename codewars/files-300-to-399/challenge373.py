"""
Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.
A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True.
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False.
"""

from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    # Verifica se os códigos são iguais (ignorando espaços e maiúsculas/minúsculas).
    if entered_code.strip().lower() != correct_code.strip().lower():
        return False
    
    # Converte as datas de string para objetos datetime.
    current_date_obj = datetime.strptime(current_date, "%B %d, %Y")
    expiration_date_obj = datetime.strptime(expiration_date, "%B %d, %Y")
    
    # Verifica se a data atual é menor ou igual à data de expiração.
    return current_date_obj <= expiration_date_obj
