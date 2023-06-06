from django.forms import ValidationError

def valid_price(price):
    if price < 0:
        raise ValidationError('Цена не может быть отрицательной или равным нулю')
    
    if not price.isdigit():
        raise ValidationError('Цена должна быть числом')
    
    num = '0123456789'
    for i in price:
        if i not in num:
            raise ValidationError('Цена должна быть числом')
         

