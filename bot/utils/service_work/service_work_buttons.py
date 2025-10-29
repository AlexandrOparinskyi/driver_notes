from fluentogram import TranslatorHub


def get_buttons_for_edit_service_work(i18n: TranslatorHub) -> list:
    return [
        (i18n.service.work.name.button(), "work_name"),
        (i18n.service.work.price.button(), "work_price"),
        (i18n.service.work.description.button(), "work_description"),
    ]
