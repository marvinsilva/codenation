from datetime import datetime, timedelta

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

FLAT_RATE = 0.36
DAY_PERIOD_RATE = 0.09
DAY_RATE_BEGIN = 6
NIGHT_RATE_BEGIN = 22


def classify_by_phone_number(records):
    """ Sorts calls by source number and groups them with the total value of calls made by that number.
        Return a list containing a dictionary with two keys 'source' and 'total' for each source number,
        ordered by the highest value.
    """
    total_by_source = {}

    for record in records:
        start = datetime.fromtimestamp(record['start'])
        end = datetime.fromtimestamp(record['end'])
        qty_of_call_minutes = (end - start).seconds // 60
        call_hour = start.hour

        # Considering only the flat rate if call is not between daytime period
        call_fee = FLAT_RATE

        # Tariff calculation considering the hour of each minute from the call
        for minute in range(qty_of_call_minutes):
            if DAY_RATE_BEGIN <= call_hour < NIGHT_RATE_BEGIN:
                call_fee += DAY_PERIOD_RATE

            start += timedelta(0, 60)

        source = record['source']
        total_by_source[source] = round(total_by_source.setdefault(source, 0) + call_fee, 2)

    bill_report = [{'source': record, 'total': total_by_source[record]} for record in total_by_source]

    return sorted(bill_report, key=lambda k: k['total'], reverse=True)


if __name__ == '__main__':
    print(classify_by_phone_number(records))
