from fluentogram import TranslatorHub

from database import ServiceRecord, RefuelRecord


def get_last_records(i18n: TranslatorHub,
                           lst: list,
                           count: int,) -> str:
    not_fount_text = i18n.car.recent.activities.no.found()

    if not lst:
        return not_fount_text

    text = ""

    for i in lst[:count]:
        if isinstance(i, ServiceRecord):
            s_date = i.service_date.strftime("%d.%m.%Y")

            if i.service_type:
                s_type = (f"{i.service_type.get_smile()} "
                          f"{i.service_type.value}")
            else:
                s_type = i18n.car.service.type()

            text += f"{s_type} · {s_date} · {i.total_price} ₽\n"

        if isinstance(i, RefuelRecord):
            r_date = i.refuel_date.strftime("%d.%m.%Y")

            r_price = i.total_price if i.total_price else "0.00"

            text += f"{i18n.car.refuel.type()} · {r_date} · {r_price}  ₽\n"

    return text