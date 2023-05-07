def bond_profit_calculator(purchase_rate, sale_rate, term):
    purchase_price = (1 + purchase_rate) ** (-term)
    sale_price = (1 + sale_rate) ** (-term)
    profit_ratio = (sale_price - purchase_price) / purchase_price
    return profit_ratio

def main():
    purchase_rate = float(input("请输入债券买入时的利率（例如：0.05 代表 5%）："))
    sale_rate = float(input("请输入债券卖出时的利率（例如：0.05 代表 5%）："))
    term = int(input("请输入债券的期限（以年为单位）："))

    profit_ratio = bond_profit_calculator(purchase_rate, sale_rate, term)
    print("实际盈亏比例为：{:.2%}".format(profit_ratio))

if __name__ == "__main__":
    main()
