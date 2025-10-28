from fluentogram import TranslatorHub

from database import ServiceRecord


def get_recent_activities_car(i18n: TranslatorHub,
                              lst: list) -> str:
    if not lst:
        return i18n.car.recent.activities.no.found()

    text = ""

    for i in lst:
        if isinstance(i, ServiceRecord):
            s_date = i.service_date.strftime("%d.%m.%Y")

            if i.service_type:
                s_type = (f"{i.service_type.get_smile()} "
                          f"{i.service_type.value}")
            else:
                s_type = i18n.car.service.type()

            text += f"{s_type} · {s_date} · {i.total_price} ₽\n"

    return text
