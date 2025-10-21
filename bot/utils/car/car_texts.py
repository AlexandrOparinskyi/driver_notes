from datetime import datetime

from fluentogram import TranslatorHub


def get_text_for_edit_part(i18n: TranslatorHub,
                           part: str) -> str:
    current_year = str(datetime.now().year)

    text_data = {
        "car_mark": i18n.car.edit.mark.text(),
        "car_model": i18n.car.edit.model.text(),
        "car_color": i18n.car.edit.color.text(),
        "car_year": i18n.car.edit.year.text(current_year=current_year),
        "car_mileage": i18n.car.edit.mileage.text(),
        "car_engine": i18n.car.edit.engine.text(),
        "car_transmission": i18n.car.edit.transmission.text(),
    }

    return text_data.get(part, i18n.no.found.back())
