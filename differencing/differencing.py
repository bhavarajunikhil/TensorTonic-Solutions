def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    # series_1 = []
    for j in range(order):
        series_1 = []
        for i in range(len(series) - 1):
            series_1.append(series[i + 1] - series[i])
        series = series_1
    return series

        