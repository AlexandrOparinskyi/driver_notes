from datetime import datetime

from fluentogram import TranslatorHub

from database import EngineTypeEnum, TransmissionTypeEnum


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


def get_text_for_car_data(data: dict) -> str:
    text = "\n"

    mark = data.get("car_mark")
    if mark:
        text += f"<b>• 🚗 Марка:</b> {mark}\n"

    model = data.get("car_model")
    if model:
        text += f"<b>• 🚙 Модель:</b> {model}\n"

    color = data.get("car_color")
    if color:
        text += f"<b>• 🎨 Цвет:</b> {color}\n"

    year = data.get("car_year")
    if year:
        text += f"<b>• 📅 Год:</b> {year}\n"

    mileage = data.get("car_mileage")
    if mileage:
        text += f"<b>• 🛣️ Пробег:</b> {mileage}\n"

    engine = data.get("car_engine")
    if engine:
        text += f"<b>• ⚙️ Двигатель:</b> {EngineTypeEnum[engine].value}\n"

    transmission = data.get("car_transmission")
    if transmission:
        value = TransmissionTypeEnum[transmission].value
        text += f"<b>• 🔄 Коробка передач:</b> {value}\n"

    return text
