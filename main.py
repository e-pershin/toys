import sys
import traceback
from datetime import timedelta
from datetime import date
from datetime import datetime

from analytics import analytics
from products import products
from shipments import shipments
from transactionV3 import transaction
from stock_on_warehouses import stock_on_warehouses
from mailer import mail
from warehouses import warehouses
#from log import InsertIntegrationActivities, InsertFinishIntegrationActivities

ERRS = list()

def err_handle(txt):
    err = txt + "\n"
    err += str(sys.exc_info()[1]) + "\n"
    for i in traceback.extract_tb(sys.exc_info()[2]):
        err += str(i) + "\n"
    print(err)
    ERRS.append(err)


def main():
    #InsertIntegrationActivities(18)
    dt = date.today() - timedelta(days=30)

    try:
        print("Загрузка данных аналитики за ", (date.today() - timedelta(days=1)))
        print("Загрузка данных начата в ", datetime.now())
        analytics((date.today() - timedelta(days=1)).isoformat())
        print("Загрузка данных закончена в ", datetime.now())
    except:
        err_handle("Произошла ошибка при обработке данных аналитики за {}!".format(dt))

    while dt < date.today():
        print(dt)
 if __name__ == "__main__":
    main()

