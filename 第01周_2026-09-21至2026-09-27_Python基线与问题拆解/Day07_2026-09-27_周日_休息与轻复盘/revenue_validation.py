def parse_revenue(value):
    try:
        if float(value) >= 0:
            return float(value)
        else:
            return None
    except (ValueError,TypeError):
        return None
        

for value in [60, "40", "四十元", None, -10, 0]:
    print(value, "->", parse_revenue(value))

for value in ["19.9", -0.5]:
    print(value, "->", parse_revenue(value))
    
