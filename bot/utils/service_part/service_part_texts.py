from fluentogram import TranslatorHub


def get_text_for_part_data(i18n: TranslatorHub,
                           data: dict) -> str:
    text = "\n"

    name = data.get("part_name")
    if name:
        text += f"<b>{i18n.service.part.name.button()}:</b> {name}\n"

    price = data.get("part_price")
    if price:
        text += f"<b>{i18n.service.part.price.button()}:</b> {price}\n"

    quantity = data.get("part_quantity")
    if quantity:
        text += f"<b>{i18n.service.part.quantity.button()}:</b> {quantity}\n"

    ppu = data.get("part_price_per_unit")
    if ppu:
        text += f"<b>{i18n.service.part.price.per.unit.button()}:</b> {ppu}\n"

    number = data.get("part_number")
    if number:
        text += f"<b>{i18n.service.part.number.button()}:</b> {number}\n"

    comment = data.get("part_comment")
    if comment:
        text += (f"<b>{i18n.service.part.comment.button()}:</b>"
                 f" {comment[:30]}\n")

    return text
