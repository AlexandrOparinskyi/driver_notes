car-edit-menu-text =
    <b>📋 Complete Dossier of Your Car:</b>

    Here is all the information about <b>{ $car_name }</b> currently in the system:
    { $car_data }
    <b>🛠️ Choose which characteristic to adjust:</b>

car-edit-mark-text = <b>🚗 Specify the Car Brand</b>

                 You can:
                 🔘 Choose from the list
                 ✍️ Or enter manually

car-edit-model-text = <b>🚙 Specify the Car Model</b>

                  You can:
                  🔘 Choose from suggested options
                  ✍️ Or enter your own model

car-edit-color-text = <b>🎨 Specify the Car Color</b>

                  What color is the car? 🌈

                  You can:
                  🔘 Choose from options
                  ✍️ Or enter manually (e.g., "Gray metallic" or "#FF0000")

car-edit-year-text = <b>📅 Specify the Year of Manufacture</b>

                 Enter or select the car's year of manufacture 🎂

                 Valid values:
                 🔢 Numbers only
                 📆 From 1900 to { $current_year }

car-edit-mileage-text = <b>🛣️ Specify the Current Mileage</b>

                    Enter the mileage in kilometers 🚗

                    Allowed:
                    🔢 Numbers only
                    🚫 No spaces, letters, or symbols

car-edit-engine-text = <b>⚙️ Select the Engine Type</b>

                   What engine does your car have? 🔧

                   Available options:
                   ⛽ Gasoline — the most common
                   🛢️ Diesel — economical and reliable
                   ⚡ Electric — modern and quiet
                   🔋 Hybrid — combination of engine and electric motor

car-edit-transmission-text = <b>🔄 Select the Transmission Type</b>

                         What transmission is installed? 🎚️

                         Available options:
                         🤖 Automatic — convenient in traffic
                         🎛️ Manual — full control
                         📊 CVT — smooth ride
                         ⚙️ Automated Manual — fast shifting

car-rename-text =
    <b>🚙 Let's Give Your Car a New Name!</b>

    You can use:
    • Brand and model 🏷️
    • Nickname or pet name 🤩
    • Something personal and memorable ✨

    <b>Simply enter the new name below:</b>


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

car-documents-text =
    📋 Documents for Car <b>{ $car_name }</b>

    <b>🔍 Identification Data:</b>
    VIN: { $vin }
    License Plate: { $car_number }
    Registration Certificate: { $sts }
    Vehicle Passport: { $pts }

    <b>📅 Validity Periods:</b>
    Insurance Policy: { $insurance_number }
    ⏱️ Days until insurance expires: { $insurance_days }

    <b>Select a document to add or edit:</b>

car-doc-add-vin-text =
    <b>🔢 Adding/Changing VIN Number</b>

    VIN is a 17-character vehicle identification number.

    <b>Example:</b> <code>Z8T4C5S9D2M1P6L3K</code>

    📍 <b>Where to find it:</b>
    • On the left side of the dashboard (visible through the windshield)
    • In the engine compartment
    • In the vehicle documents

    ✏️ <b>Enter the VIN number:</b>

car-doc-add-license-text =
    <b>🚘 Adding/Changing License Plate</b>

    Vehicle license plate number.

    <b>Examples:</b>
    <code>А123БВ777</code> (Russia)
    <code>AB1234CD</code> (other countries)

    ✏️ <b>Enter the license plate:</b>

car-doc-add-cts-text =
    <b>📄 Adding/Changing Registration Certificate (СТС) Data</b>

    Vehicle Registration Certificate.

    <b>Example number:</b> <code>45КМ №123456</code>
    <b>Example series:</b> <code>77 01 123456</code>

    📍 <b>Usually located:</b> in the car, with documents

    ✏️ <b>Enter the Registration Certificate number:</b>

car-doc-add-pts-text =
    <b>📑 Adding/Changing Vehicle Passport (ПТС) Data</b>

    Vehicle Passport.

    <b>Example number:</b> <code>78УТ №789012</code>
    <b>Example series:</b> <code>64 02 345678</code>

    ✏️ <b>Enter the Vehicle Passport number:</b>

car-doc-add-osago-text =
    <b>🛡️ Adding/Changing Insurance (ОСАГО) Data</b>

    Compulsory Motor Third-Party Liability Insurance policy.

    <b>Example number:</b> <code>XXX123456789</code>

    ✏️ <b>Enter the insurance policy number:</b>

car-doc-add-osago-date-text =
    <b>📅 Select the Insurance PURCHASE DATE</b>

    📍 <b>Important:</b>
    The insurance validity period will be automatically calculated
    as <b>1 year</b> from the specified purchase date.

    ✏️ <b>Select the policy purchase date:</b>


add-documents-button = 📝 Add/Edit Documents

car-documents-vin-button = 🔢 VIN
car-documents-license-button = 🚘 License Plate
car-documents-cts-button = 📄 Registration Certificate
car-documents-pts-button = 📑 Vehicle Passport
car-documents-osago-button = 🛡️ Insurance