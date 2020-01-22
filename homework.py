import datetime as dt

date_format = '%d.%m.%Y'


class Calculator:
    def __init__(self, limit):
        self.limit = int(limit)
        self.records = [] 

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        count = 0
        today = dt.date.today() 
        for record in self.records:
            if record.date == today:
                count += record.amount        
        return count
    
    def get_week_stats(self):
        weekly_sum = 0
        day_week_ago = dt.datetime.today().date() - dt.timedelta(days=7)
        for record in self.records:
            if day_week_ago <= record.date <= dt.datetime.now().date(): 
                weekly_sum += record.amount 
        return weekly_sum       


class CaloriesCalculator(Calculator):
    
    def get_calories_remained(self):
        today_calories = self.get_today_stats()
        available_calories = self.limit - today_calories
        if today_calories <= self.limit:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {available_calories} кКал"
        else:
            return 'Хватит есть!' 


class CashCalculator(Calculator):  
    USD_RATE = 60.00
    EURO_RATE = 70.00

    def get_today_cash_remained(self, currency):
        balance = self.limit - self.get_today_stats()
        balance_usd = round((balance / self.USD_RATE), 2)
        balance_eur = round((balance / self.EURO_RATE), 2)
        
        if self.get_today_stats() == self.limit:
            return 'Денег нет, держись'
        
        elif self.get_today_stats() < self.limit:
            if currency == "rub":
                return f'На сегодня осталось {balance} руб'
            elif currency == "eur":
                return f'На сегодня осталось {balance_eur} Euro'
            elif currency == "usd":
                return f'На сегодня осталось {balance_usd} USD'

        elif self.get_today_stats() > self.limit:
            if currency == "rub":
                return f'Денег нет, держись: твой долг - {abs(balance) } руб'
            elif currency == "eur":
                return f'Денег нет, держись: твой долг - {abs(balance_eur)} Euro'
            elif currency == "usd":
                return f'Денег нет, держись: твой долг - {abs(balance_usd)} USD'
                

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = int(amount)     
        self.comment = comment
        if date:
            self.date = dt.datetime.strptime(date, date_format).date()
        else:
            self.date = dt.datetime.now().date()      