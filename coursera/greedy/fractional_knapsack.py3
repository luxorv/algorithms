import sys

def ratio(x):

    if len(x) == 2 and x[0] is not 0:
        return float(x[1])/float(x[0])
    return x[0]

def sort_items(weights, values):
    val_weights = zip(values, weights)

    val_weights = sorted(val_weights, key=ratio)

    return val_weights

def get_optimal_value(capacity, weights, values):
    value = 0.

    val_weights = sort_items(weights, values)

    for vi, wi in val_weights:

        if not capacity:
            return value

        a = min(wi, capacity)
        capacity -= a
        value += a * (vi/wi)

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2::2]
    weights = data[3::2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
