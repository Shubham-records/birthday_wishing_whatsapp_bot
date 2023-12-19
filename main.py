import smtplib
import time
from condition_checker import Condition

condition = Condition()


class SendMessage:
    def __init__(self):
        self.MyEmail = "subhampal342@gmail.com"
        self.ToAddress = "1981monikapal@gmail.com"
        self.password = "yyuhafhopzlcwbqw"

    def send_meassages(self):
        condition.check()
        print(condition.today_wishing_messages)
        for i in condition.today_wishing_messages:
            message = f"subject:happy birthday {i['name']}\n\n{i['message']}"

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.MyEmail, password=self.password)
                connection.sendmail(
                    from_addr=self.MyEmail,
                    to_addrs=self.ToAddress,
                    msg=message
                )
            time.sleep(5)


run = SendMessage()
run.send_meassages()
