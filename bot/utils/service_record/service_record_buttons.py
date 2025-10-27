from fluentogram import TranslatorHub


def get_button_for_add_service_record(i18n: TranslatorHub) -> list:
    return [
        (i18n.service.car.button(), "service_car"),
        (i18n.service.mileage.button(), "service_mileage"),
        (i18n.service.title.button(), "service_title"),
        (i18n.service.description.button(), "service_description"),
        (i18n.service.date.button(), "service_date"),
        (i18n.service.type.button(), "service_type"),
        (i18n.service.price.button(), "service_price"),
        (i18n.service.name.button(), "service_name"),
    ]
