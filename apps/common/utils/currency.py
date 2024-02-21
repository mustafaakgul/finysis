import xml.etree.ElementTree as ET
from urllib.request import urlopen


class CurrencyExchange():

    def __init__(self):
        pass

    def __update_data(self, zaman="today"):
        try:

            if zaman == "today":
                self.url = "http://www.tcmb.gov.tr/kurlar/today.xml"
            else:
                self.url = zaman

            tree = ET.parse(urlopen(self.url))

            root = tree.getroot()
            self.son = {}
            self.Kur_Liste = []
            i = 0
            for kurlars in root.findall('Currency'):
                Kod = kurlars.get('Kod')
                Unit = kurlars.find('Unit').text  # <Unit>1</Unit>
                isim = kurlars.find('Isim').text  # <Isim>ABD DOLARI</Isim>
                CurrencyName = kurlars.find('CurrencyName').text  # <CurrencyName>US DOLLAR</CurrencyName>
                ForexBuying = kurlars.find('ForexBuying').text  # <ForexBuying>2.9587</ForexBuying>
                ForexSelling = kurlars.find('ForexSelling').text  # <ForexSelling>2.964</ForexSelling>
                BanknoteBuying = kurlars.find('BanknoteBuying').text  # <BanknoteBuying>2.9566</BanknoteBuying>
                BanknoteSelling = kurlars.find('BanknoteSelling').text  # <BanknoteSelling>2.9684</BanknoteSelling>
                CrossRateUSD = kurlars.find('CrossRateUSD').text  # <CrossRateUSD>1</CrossRateUSD>
                self.Kur_Liste.append(Kod)
                # self.son [Kod] = [Kod,isim,CurrencyName,Unit,ForexBuying,ForexSelling,BanknoteBuying,BanknoteSelling,CrossRateUSD]
                self.son[Kod] = {
                    "Kod": Kod,
                    "isim": isim,
                    "CurrencyName": CurrencyName,
                    "Unit": Unit,
                    "ForexBuying": ForexBuying,
                    "ForexSelling": ForexSelling,
                    "BanknoteBuying": BanknoteBuying,
                    "BanknoteSelling": BanknoteSelling,
                    "CrossRateUSD": CrossRateUSD
                }

            return self.son

        except Exception as e:
            return e

    def get_current_rate(self, *sor):
        self.__update_data()
        if not (any(sor)):
            return self.son
        else:
            return self.son.get(sor[0]).get(sor[1])

    def get_archive_rate(self, day, month, year, *sor):
        a = self.__update_data(self.__create_url(day, month, year))
        if not (any(sor)):
            if a == "HATA":
                return {"Hata": "TATIL GUNU"}
            return self.son
        else:
            if a == "HATA":
                return "Holiday"
            else:
                return self.son.get(sor[0]).get(sor[1])

    def get_archive_rate_by_date(self, Tarih="", *sor):
        takvim = Tarih.split(".")
        day = takvim[0]
        month = takvim[1]
        year = takvim[2]
        a = self.__update_data(self.__create_url(day, month, year))
        if not (any(sor)):
            if a == "HATA":
                return {"Hata": "TATIL GUNU"}
            return self.son
        else:
            if a == "HATA":
                return "Holiday"
            else:
                return self.son.get(sor[0]).get(sor[1])

    def __create_url(self, day, month, year):
        if len(str(day)) == 1:
            day = "0" + str(day)
        if len(str(month)) == 1:
            month = "0" + str(month)

        self.url = ("http://www.tcmb.gov.tr/kurlar/" + str(year) + str(month) + "/" + str(day) + str(month) + str(
            year) + ".xml")
        return self.url
