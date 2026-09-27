def summarize_sales(sales):
    if sales == []:
        return None

    maximum = 0
    total = 0
    for sale in sales:
        total += sale
        if sale > maximum:
            maximum = sale
    average = total / len(sales)
    summarize_sales = {
        "total": total,
        "average": average,
        "maximum": maximum
    }
    return summarize_sales    

sales = [100, 200, 300, 0, 150]
print(summarize_sales(sales))
print(summarize_sales([]))
