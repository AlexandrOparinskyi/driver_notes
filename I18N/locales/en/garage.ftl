garage-text =
    <b>🚗 Your Garage</b>

    Hello, { $username }! This is where all your steel steeds live.

    <b>For each car you can:</b>
    • 📝 Edit data
    • 📎 Add documents (Registration, Insurance, VIN)
    • 📊 View detailed expense statistics
    • 🔔 Set up reminders for each car

    <b>Select a car to view and manage, or add a new one to your collection! 🎯</b>

    Just tap on a car - and all information about it will open! ✨

car-name-text =
    <b>Excellent! Your car is almost in the garage! 🚗💨</b>

    Just need to give it a <b>name</b> ✨. This is so you can easily find it in the list later.
    Don't try to remember everything at once - just the <b>brand</b> 🏷️, <b>model</b> 🚘, or even a <b>nickname</b> if it has one 🤩 will work!

    <b>All other details - year 📅, engine type ⚙️, current mileage 🛣️ - you can easily add later.</b> I'll definitely remind you 🔔 if something is needed for accurate calculations!

    <b>So, what shall we call it?</b> 😊

car-offer-premium-text =
    <b>🏁 Great fleet! But there's a nuance... ✨</b>

    I see you're serious about tracking. But the free version is limited to 2 cars.

    <b>💎 With Premium, your garage becomes limitless:</b>
    ✅ Unlimited number of cars in the garage
    ✅ Priority support
    ✅ Data export to Excel/PDF twice a month

    <b>Only { $premium_price } ₽ per month - an investment in your comfort! 🚗💨</b>

    Shall we open the unlimited garage? 😊

car-details-text =
    Your car - <b>{ $car_name }</b>

    <b>📊 Overall Statistics:</b>
    💰 Total expenses: <b>{ $total_expenses } ₽</b>
    🔧 Number of records: <b>{ $total_records }</b>
    🛣️ Mileage: <b>{ $car_mileage } km</b>
    📅 In operation: <b>{ $days_owned } days</b>

    <b>⚙️ Recent vehicle activities:</b>
    { $recent_activities }

add-car-button = ➕ Add Car

edit-car-name-button = ✏️ Rename
edit-car-data-button = 📝 Specifications
edit-car-documents-button = 📎 Documents
car-report-button = 📑 Records
setting-notification-button = 🔔 Set Up Reminders
delete-car-button = 🗑️ Remove from Garage


car-records-text =
    <b>📋 Records for Car { $car_name }</b>

    🔍 <b>Record Filter</b>
    <i>You can select multiple types to display</i>
    🔧 Service       ⛽ Refueling
    🛒 Purchase      📝 Other

    📊 <b>Total records: { $records_count }</b>

    📅 <b>Select a record to view:</b>

garage-service-record-text =
    <b>{ $service_name }</b>

    🚗 { $car_name }
    💰 Amount: { $amount } ₽
    🔧 Type of work: { $service_type }
    🏢 Service center: { $service_station }

    💬 Work description:
    { $description }

garage-refuel-record-text =
    <b>{ $refuel_name }</b>

    🚗 { $car_name }
    💰 Amount: { $amount } ₽
    ⛽ Fuel type: { $fuel_type }
    ⛽ Quantity: { $fuel_volume }
    🏭 Gas station: { $gas_station }


garage-refuel-filter-text = ⛽ Refueling
garage-service-filter-text = 🔧 Service
garage-purchase-filter-text = 🛒 Purchase
garage-other-filter-text = 📝 Other


active-refuel-button = ✅ ⛽
active-service-button = ✅ 🔧
active-purchase-button = ✅ 🛒
active-other-button = ✅ 📝
unactive-refuel-button = ❌ ⛽
unactive-service-button = ❌ 🔧
unactive-purchase-button = ❌ 🛒
unactive-other-button = ❌ 📝

garage-edit-record-button = ✏️ Edit
garage-delete-record-button = 🗑️ Delete Record
garage-download-record-button = 📥 Export to PDF