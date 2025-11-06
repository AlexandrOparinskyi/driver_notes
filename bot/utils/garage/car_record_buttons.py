from fluentogram import TranslatorHub

from database import ServiceRecord, RefuelRecord


def get_car_record_buttons_to_dict(i18n: TranslatorHub,
                                   records: list,
                                   size: int = 10) -> dict:
    result = {}
    for i in range(0, len(records)):
        chunk_num = i // size
        chunk_key = f"page_{chunk_num}"

        if chunk_key not in result:
            result[chunk_key] = []

        if isinstance(records[i], ServiceRecord):
            button = (f"{i18n.garage.service.filter.text()} "
                      f"{records[i].service_date.strftime('%d.%m.%Y')}",
                      f"service_{records[i].id}")
        elif isinstance(records[i], RefuelRecord):
            button = (f"{i18n.garage.refuel.filter.text()} "
                      f"{records[i].refuel_date.strftime('%d.%m.%Y')}",
                      f"refuel_{records[i].id}")
        else:
            button = ("Error", 10)

        result[chunk_key].append(button)

    return result
