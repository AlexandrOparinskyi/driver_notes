garage-text =
    <b>🚗 Твой гараж</b>

    Привет, { $username }! Здесь живут все твои железные кони.

    <b>Для каждой машины ты можешь:</b>
    • 📝 Редактировать данные
    • 📎 Добавлять документы (СТС, ОСАГО, VIN)
    • 📊 Смотреть детальную статистику расходов
    • 🔔 Настраивать напоминания для каждой машины

    <b>Выбери машину для просмотра и управления или добавь новую в коллекцию! 🎯</b>

    Просто нажми на авто — и откроется вся информация о нём! ✨

car-name-text =
    <b>Прекрасно! Твоя машина уже почти в гараже! 🚗💨</b>

    Осталось дать ей <b>имя</b> ✨. Это нужно, чтобы ты мог легко найти её в списке позже.
    Не пытайся вспомнить всё сразу — подойдёт просто <b>марка</b> 🏷️, <b>модель</b> 🚘 или даже <b>кличка</b>, если она есть 🤩!

    <b>Все остальные детали — год 📅, тип двигателя ⚙️, текущий пробег 🛣️ — ты сможешь легко добавить дальше.</b> Я обязательно подскажу 🔔, если что-то понадобится для точных расчетов!

    <b>Ну что, как её назовём?</b> 😊

car-offer-premium-text =
    <b>🏁 Отличный автопарк! Но есть нюанс... ✨</b>

    Вижу, ты серьёзно подходишь к учету. Но бесплатная версия ограничена 2 автомобилями.

    <b>💎 С Премиумом твой гараж станет безграничным:</b>
    ✅ Неограниченное количество машин в гараже
    ✅ Приоритетная поддержка
    ✅ Экспорт данных в Excel/PDF 2 раза в месяц

    <b>Всего { $premium_price } ₽ в месяц — инвестиция в твой комфорт! 🚗💨</b>

    Откроем безлимитный гараж? 😊

car-details-text =
    Твой авто - <b>{ $car_name }</b>

    <b>📊 Общая статистика:</b>
    💰 Всего расходов: <b>{ $total_expenses } ₽</b>
    🔧 Количество работ: <b>{ $total_records }</b>
    🛣️ Пробег: <b>{ $car_mileage } км</b>
    📅 В эксплуатации: <b>{ $days_owned } дней</b>

    <b>⚙️ Последние действия авто:</b>
    { $recent_activities }

add-car-button = ➕ Добавить машину

edit-car-name-button = ✏️ Переименовать
edit-car-data-button = 📝 Характеристики
edit-car-documents-button = 📎 Документы
car-report-button = 📑 Записи
setting-notification-button = 🔔 Настроить напоминания
delete-car-button = 🗑️ Удалить из гаража


car-records-text =
    <b>📋 Записи автомобиля { $car_name }</b>

    🔍 <b>Фильтр записей</b>
    <i>Можно выбрать несколько типов для отображения</i>
    🔧 Сервис       ⛽ Заправка
    🛒 Покупка      📝 Другое

    📊 <b>Всего записей: { $records_count }</b>

    📅 <b>Выбери запись для просмотра:</b>

garage-service-record-text =
    <b>{ $service_name }</b>

    🚗 { $car_name }
    💰 Сумма: { $amount } ₽
    🔧 Тип работ: { $service_type }
    🏢 Сервисный центр: { $service_station }

    💬 Описание работ:
    { $description }

garage-refuel-record-text =
    <b>{ $refuel_name }</b>

    🚗 { $car_name }
    💰 Сумма: { $amount } ₽
    ⛽ Тип топлива: { $fuel_type }
    ⛽ Количество: { $fuel_volume }
    🏭 АЗС: { $gas_station }


garage-refuel-filter-text = ⛽ Заправка
garage-service-filter-text = 🔧 Сервис
garage-purchase-filter-text = 🛒 Покупка
garage-other-filter-text = 📝 Другое


active-refuel-button = ✅ ⛽
active-service-button = ✅ 🔧
active-purchase-button = ✅ 🛒
active-other-button = ✅ 📝
unactive-refuel-button = ❌ ⛽
unactive-service-button = ❌ 🔧
unactive-purchase-button = ❌ 🛒
unactive-other-button = ❌ 📝

garage-edit-record-button = ✏️ Редактировать
garage-delete-record-button = 🗑️ Удалить запись
garage-download-record-button = 📥 Экспорт в PDF
