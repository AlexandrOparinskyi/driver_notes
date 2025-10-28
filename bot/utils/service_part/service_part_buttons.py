from fluentogram import TranslatorHub


def get_buttons_for_edit_service_part(i18n: TranslatorHub) -> list:
    return [
        (i18n.service.part.name.button(), "part_name"),
        (i18n.service.part.price.button(), "part_price"),
        (i18n.service.part.quantity.button(), "part_quantity"),
        (i18n.service.part.price.per.unit.button(), "part_price_per_unit"),
        (i18n.service.part.number.button(), "part_number"),
        (i18n.service.part.comment.button(), "part_comment")
    ]
