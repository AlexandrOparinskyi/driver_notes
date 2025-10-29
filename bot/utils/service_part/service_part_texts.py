from fluentogram import TranslatorHub


def get_text_for_part_data(i18n: TranslatorHub,
                           data: dict) -> str:
    text = "\n"

    name = data.get("part_name")
    if name:
        text += f"<b>{i18n.service.part.name.button()}:</b> {name}\n"

    price = data.get("part_price")
    if price:
        text += (f"<b>{i18n.service.part.price.button()}:</b> "
                 f"{price.replace(',', '.')}\n")

    quantity = data.get("part_quantity")
    if quantity:
        text += f"<b>{i18n.service.part.quantity.button()}:</b> {quantity}\n"

    ppu = data.get("part_price_per_unit")
    if ppu:
        text += (f"<b>{i18n.service.part.price.per.unit.button()}:</b> "
                 f"{ppu.replace(',', '.')}\n")

    number = data.get("part_number")
    if number:
        text += f"<b>{i18n.service.part.number.button()}:</b> {number}\n"

    comment = data.get("part_comment")
    if comment:
        text += (f"<b>{i18n.service.part.comment.button()}:</b>"
                 f" {comment[:30]}\n")

    return text


def get_text_for_edit_part_param(i18n: TranslatorHub,
                                 part_param: str) -> str:
    part_param_data = {
        "part_name": i18n.service.part.edit.name.text(),
        "part_price": i18n.service.part.edit.price.text(),
        "part_quantity": i18n.service.part.edit.quantity.text(),
        "part_price_per_unit": i18n.service.part.edit.price.per.unit.text(),
        "part_number": i18n.service.part.edit.number.text(),
        "part_comment": i18n.service.part.edit.comment.text(),
    }

    return part_param_data.get(part_param,
                               i18n.service.part.edit.error.param.text())
