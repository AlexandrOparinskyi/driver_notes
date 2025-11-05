from fluentogram import TranslatorHub

from bot.utils import get_car_marks, get_car_models
from database import EngineTypeEnum, TransmissionTypeEnum


def get_button_for_add_car(i18n: TranslatorHub) -> list[tuple]:
    return [
        (i18n.car.mark.button(), "car_mark"),
        (i18n.car.model.button(), "car_model"),
        (i18n.car.color.button(), "car_color"),
        (i18n.car.year.button(), "car_year"),
        (i18n.car.mileage.button(), "car_mileage"),
        (i18n.car.engine.button(), "car_engine"),
        (i18n.car.transmission.button(), "car_transmission"),
    ]


async def get_button_for_edit_car(i18n: TranslatorHub,
                                  part: str,
                                  mark_id: str | None) -> list[tuple] | list:
    if part == "car_mark":
        marks = await get_car_marks()
        return [(m.name, m.id) for m in marks]

    elif part == "car_model":
        models = await get_car_models(mark_id)
        return [(m.name, m.id) for m in models]

    elif part == "car_color":
        colors = [i18n.black.color.text(),
                  i18n.white.color.text(),
                  i18n.grey.color.text(),
                  i18n.red.color.text(),
                  i18n.blue.color.text(),
                  i18n.brown.color.text(), ]
        return [(c, c) for c in colors]

    elif part == "car_engine":
        return [(e.value, e.name) for e in EngineTypeEnum]

    elif part == "car_transmission":
        return [(t.value, t.name) for t in TransmissionTypeEnum]

    else:
        return []


def get_buttons_for_edit_car_data(i18n: TranslatorHub) -> list[tuple]:
    return [
        (i18n.car.documents.vin.button(), "vin_number"),
        (i18n.car.documents.cts.button(), "sts"),
        (i18n.car.documents.pts.button(), "pts"),
        (i18n.car.documents.license.button(), "gos_number"),
        (i18n.car.documents.osago.button(), "insurance_number"),
    ]
