car-edit-menu-text =
    <b>📋 Complete Dossier of Your Car:</b>

    Here is all the information about <b>{ $car_name }</b> currently in the system:
    { $car_data }
    <b>🛠️ Choose which characteristic to edit:</b>

car-edit-mark-text = <b>🚗 Enter the car's brand</b>

                 You can:
                 🔘 Choose from the list
                 ✍️ Or enter manually

car-edit-model-text = <b>🚙 Enter the car's model</b>

                  You can:
                  🔘 Choose from the suggested ones
                  ✍️ Or enter your model

car-edit-color-text = <b>🎨 Enter the car's color</b>

                  What's the car's color? 🌈

                  You can:
                  🔘 Choose from the options
                  ✍️ Or enter manually (e.g., "Gray metallic" or "#FF0000")

car-edit-year-text = <b>📅 Enter the manufacturing year</b>

                 Enter or select the car's manufacturing year 🎂

                 Allowed values:
                 🔢 Numbers only
                 📆 From 1900 to { $current_year }

car-edit-mileage-text = <b>🛣️ Enter the current mileage</b>

                    Enter the mileage in kilometers 🚗

                    Allowed:
                    🔢 Numbers only
                    🚫 No spaces, letters, or symbols

car-edit-engine-text = <b>⚙️ Select the engine type</b>

                   What kind of engine does your car have? 🔧

                   Available options:
                   ⛽ Gasoline — the most common
                   🛢️ Diesel — economical and reliable
                   ⚡ Electric — modern and quiet
                   🔋 Hybrid — combination of engine and electric motor

car-edit-transmission-text = <b>🔄 Select the transmission type</b>

                         What transmission is installed? 🎚️

                         Available options:
                         🤖 Automatic — convenient in traffic
                         🎛️ Manual — full control
                         📊 CVT — smooth ride
                         ⚙️ Automated Manual — fast shifting

car-rename-text =
    <b>🚙 Let's give your car a new name!</b>

    You can use:
    • Brand and model 🏷️
    • Nickname or alias 🤩
    • Something personal and memorable ✨

    <b>Simply enter the new name below:</b>

car-documents-text =
    📋 Documents for car <b>🚗 { $car_name }</b>

    <b>🔍 Identification Data:</b>
    VIN: { $vin }
    License Plate: { $car_number }
    Vehicle Registration Certificate: { $sts }
    Vehicle Passport: { $pts }

    <b>📅 Validity Periods:</b>
    OSAGO Insurance: <code>{ $insurance_number }</code>
    ⏱️ Insurance expires in: { $insurance_days }

car-mark-button = 🚗 Brand
car-model-button = 🚙 Model
car-color-button = 🎨 Color
car-year-button = 📅 Year
car-mileage-button = 🛣️ Mileage
car-engine-button = ⚙️ Engine
car-transmission-button = 🔄 Transmission

black-color-text = ⚫ Black
white-color-text = ⬤ White
grey-color-text = ⚪ Gray
red-color-text = 🔴 Red
blue-color-text = 🔵 Blue
brown-color-text = 🟤 Brown

add-documents-button = 📝 Add/Edit documents