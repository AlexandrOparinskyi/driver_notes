from fluentogram import TranslatorHub


def get_text_for_work_data(i18n: TranslatorHub,
                           data: dict) -> str:
    text = "\n"

    name = data.get("work_name")
    if name:
        text += f"<b>{i18n.service.work.name.button()}:</b> {name}\n"

    price = data.get("work_price")
    if price:
        text += (f"<b>{i18n.service.work.price.button()}:</b> "
                 f"{price.replace(',', '.')}\n")

    description = data.get("work_description")
    if description:
        text += (f"<b>{i18n.service.work.description.button()}:</b> "
                 f"{description[:30]}\n")

    return text


def get_text_for_edit_work_param(i18n: TranslatorHub,
                                 work_param: str) -> str:
    work_param_data = {
        "work_name": i18n.service.work.edit.name.text(),
        "work_price": i18n.service.work.edit.price.text(),
        "work_description": i18n.service.work.edit.description.text(),
    }
    return work_param_data.get(work_param,
                               i18n.service.work.edit.error.param.text())