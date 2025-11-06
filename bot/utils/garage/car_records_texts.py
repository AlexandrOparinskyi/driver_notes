from fluentogram import TranslatorHub

from ..database import (get_service_by_id,
                        get_refuel_by_id)


def get_car_records_filters(i18n: TranslatorHub,
                            checked_service_filter: bool = True,
                            checked_refuel_filter: bool = False,
                            checked_purchase_filter: bool = False,
                            checked_other_filter: bool = False,
                            **kwargs) -> str:
    text = "\n"

    if checked_service_filter:
        text += "• " + i18n.garage.service.filter.text() + "\n"

    if checked_refuel_filter:
        text += "• " + i18n.garage.refuel.filter.text() + "\n"

    if checked_purchase_filter:
        text += "• " + i18n.garage.purchase.filter.text() + "\n"

    if checked_other_filter:
        text += "• " + i18n.garage.other.filter.text() + "\n"

    return text


async def get_record_text(i18n: TranslatorHub,
                          record_type: str,
                          record_id: int) -> str:
    not_found = i18n.field.no.filled()

    if record_type == "service":
        service = await get_service_by_id(record_id)
        service_name = (service.title if service.title
                        else f"{i18n.garage.service.filter.text()} "
                             f"{service.service_date.strftime('%d.%m.%Y')}")
        service_type = (service.service_type.value
                        if service.service_type else not_found)
        service_station = (service.service_center
                           if service.service_center else not_found)
        description = (service.description
                       if service.description else not_found)
        text = i18n.garage.service.record.text(
            service_name=service_name,
            car_name=service.car.name,
            amount=service.total_price if service.total_price else 0,
            service_type=service_type,
            service_station=service_station,
            description=description
        )

    elif record_type == "refuel":
        refuel = await get_refuel_by_id(record_id)
        refuel_name = (f"{i18n.garage.refuel.filter.text()} "
                       f"{refuel.refuel_date.strftime('%d.%m.%Y')}")
        fuel_type = (refuel.fuel_type.value
                     if refuel.fuel_type else not_found)
        gas_station = (refuel.gas_station.value
                       if refuel.gas_station else not_found)
        text = i18n.garage.refuel.record.text(
            refuel_name=refuel_name,
            car_name=refuel.car.name,
            amount=refuel.total_price if refuel.total_price else 0,
            fuel_type=fuel_type,
            fuel_volume=refuel.liters if refuel.liters else not_found,
            gas_station=gas_station
        )

    else:
        text = i18n.no.found.back()

    return text
