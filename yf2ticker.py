#!/usr/bin/env python3
import csv
import fileinput

SYMBOL_INDEX = 0
CURRENT_PRICE_INDEX = 1
PURCHASE_PRICE_INDEX = 10
QUANTITY_INDEX = 11


class YahooFinancePortfolio:
    def __init__(self):
        self.lots = []
        self.watchlist = []

    def add(self, row):
        if row[CURRENT_PRICE_INDEX] == 'Current Price':
            return
        if row[QUANTITY_INDEX] == '':
            self.watchlist.append(row)
        else:
            self.lots.append(row)

    def print(self):
        self.print_watchlist()
        self.print_lots()

    def print_watchlist(self):
        if len(self.watchlist) == 0:
            return
        print("watchlist:")
        for row in self.watchlist:
            symbol = row[SYMBOL_INDEX]
            print(f'  - "{symbol}"')

    def print_lots(self):
        if len(self.lots) == 0:
            return
        print("lots:")
        for row in self.lots:
            symbol = row[SYMBOL_INDEX]
            quantity = row[QUANTITY_INDEX]
            unit_cost = row[PURCHASE_PRICE_INDEX]
            print(f'  - symbol: "{symbol}"')
            print(f'    quantity: {quantity}')
            print(f'    unit_cost: {unit_cost}')


def main():
    portfolio = YahooFinancePortfolio()
    reader = csv.reader(fileinput.input())
    for row in reader:
        portfolio.add(row)
    portfolio.print()


if __name__ == '__main__':
    main()
