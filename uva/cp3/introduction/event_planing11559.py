
while True:

    try:
        people, budget, hotels, weeks = map(int, input().split())
        minimum_price = budget
        not_found = True

    except EOFError:
        break
    else:

        for i in range(hotels):
            price_per_person = int(input())
            available = list(map(int, input().split()))
            hotel_minimum_price = price_per_person * people
            available_beds = max(available)

            if hotel_minimum_price > budget:
                continue

            if available_beds < people:
                continue

            if hotel_minimum_price < minimum_price:
                minimum_price = hotel_minimum_price
                not_found = False

        if not_found:
            print('stay home')
        else:
            print(minimum_price)
