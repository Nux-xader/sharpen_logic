def date_less_than(date1, date2):
    if date1 == date2:
        return False

    fdate, sdate = [int(i) for i in date1.split("-")], [int(i) for i in date2.split("-")]
    result = True

    for i in range(len(fdate)):
        if (fdate[i] > sdate[i]):
            result = False

    return result

print(not date_less_than("2022-04-01", "2022-04-20"))