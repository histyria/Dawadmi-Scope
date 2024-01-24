import requests


def Send_SMS(text , name  , day, date , time):
    url = 'https://app.mobile.net.sa/api/v1/send'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer yHgwWdENWljQq51pOAqn53RDAXC7NKU7zdOFc6kp'
    }
    headline = f"مرحباً: {name}, " \
                           f"اتم تحديد موعد العملية بتاريخ  {date}  \n"\
                           f"الساعة {time}  {day}\n"\
                           f"الرجاء الدخول على الرابط التالي و تأكيد الموعد   \n"\
                           f" في حال عدم ملائمة التاريخ الرجاء إختيار تاريخ آخر و سيتم إبلاغكم برساله نصية \n" \
                           f"تجربة ارسال موعد العملية للمريض  -- نجيب" 
    data = {
    'number': text,
    'senderName': 'Mobile.SA',
    'sendAtOption': 'Now',
    'messageBody': headline
}
    response = requests.post(url, headers=headers, json=data)
    print('Status:', response.status_code)
    print('Headers:', response.headers)
    print('Body:', response.text)