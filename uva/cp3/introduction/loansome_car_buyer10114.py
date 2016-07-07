
while True:

    values = input().split()

    loan_duration, down_payment, loan_amount, dep_records = map(float, values)
    deprecations = list(range(101))

    if loan_duration < 0:
        break

    for dep in range(int(dep_records)):
        x = input().split()
        month, val = int(x[0]), float(x[1])

        for i in range(month, 101):
            deprecations[i] = val

    car_value = (loan_amount + down_payment) * (1 - deprecations[0])
    owned_value = loan_amount
    monthly_payment = loan_amount/loan_duration
    current_month = 0

    while car_value < owned_value:

        current_month += 1
        owned_value -= monthly_payment
        car_value *= (1 - deprecations[current_month])

    m = 'months'

    if current_month == 1:
        m = 'month'

    print(current_month, m)
