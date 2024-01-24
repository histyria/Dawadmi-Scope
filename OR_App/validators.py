import datetime
from django.core.exceptions import ValidationError
import re

def validate_day(day):
    today = datetime.date.today()
    if day < today:
        raise ValidationError('Blocked Date cannot be in the Past.')
    
    
def check_mobile_validate(phone_num):
    regex = re.compile(r"^(009665|9665|\+9665|05|5)(5|0|3|6|4|9|1|8|7)([0-9]{7})$", flags=re.IGNORECASE)
    return regex.search(phone_num)




import re

def validateContact(thisObj):
    fieldValue = thisObj
    pattern = r'^(009665|9665|\+9665|05|5)(5|0|3|6|4|9|1|8|7)([0-9]{7})$'
    if re.match(pattern, fieldValue):
        thisObj.addClass('is-valid')
    else:
        thisObj.addClass('is-invalid')

