
import engine_generator

def calculate_firing_order(cylinderCount):
    firing_order = []
    for i in range(1, cylinderCount + 1):
        firing_order.append(i)
    return firing_order

def generate_inline(style, cylinderCount):
    print("Generating inline style engine...")
    cylinders = calculate_firing_order(cylinderCount)
    cylinders0 = []

    for i in range(1, cylinderCount + 1):
        cylinders0.append(i)
    
    bank = engine_generator.Bank(cylinders0, 0)
    engine = engine_generator.Engine([bank], cylinders)
    engine.engine_name = "V69"
    engine.starter_torque = 10000
    engine.crank_mass = 2000
    engine.bore = 197.9
    engine.stroke = 197.9
    engine.chamber_volume = 3000
    engine.rod_length = engine.stroke * 1.75
    engine.simulation_frequency = 1200
    engine.max_sle_solver_steps = 4
    engine.fluid_simulation_steps = 4
    engine.idle_throttle_plate_position = 0.9

    engine.generate()
    engine.write_to_file("i4.mr")


def generate_v(style, cylinderCount):
    print("Generating V style engine...")

def generate_custom_engine():
    print("Generating custom engine...")
    print("Engine Styles:\n   - Inline\n   - V")
    style = input("Enter style: ")
    if style.lower() != "inline" or style.lower() != "v":
        print("Invalid style. Must either be inline or v.")
        return
    cylinderCount = int(input("Enter cylinder count: "))
    if cylinderCount <= 0:
        print("Invalid cylinders, must be greater than 0.")
        return
    if cylinderCount == 1 and style.lower() == "v":
        print("Invalid cylinders, must be greater than 1 for V style.")
        return
    if style.lower() == "inline":
        generate_inline(style, cylinderCount)
    elif style.lower() == "v":
        generate_v(style, cylinderCount)

def generate_v24():
    cylinders0 = []
    cylinders1 = []
    cylinders = []

    for i in range(12):
        cylinders0.append(i * 2)
        cylinders1.append(i * 2 + 1)
        cylinders += [i * 2, i * 2 + 1]

    b0 = engine_generator.Bank(cylinders0, -45)
    b1 = engine_generator.Bank(cylinders1, 45)
    engine = engine_generator.Engine([b0, b1], cylinders)
    engine.engine_name = "V24"
    engine.starter_torque = 400
    engine.crank_mass = 200

    engine.generate()
    engine.write_to_file("test.mr")

def generate_v69():
    cylinders0 = []
    cylinders1 = []
    cylinders = []

    for i in range(34):
        cylinders0.append(i * 2)
        cylinders1.append(i * 2 + 1)
        cylinders += [i * 2, i * 2 + 1]

    cylinders0.append(68)
    cylinders.append(68)

    b0 = engine_generator.Bank(cylinders0, -34.5)
    b1 = engine_generator.Bank(cylinders1, 34.5)
    b1.flip = True
    engine = engine_generator.Engine([b0, b1], cylinders)
    engine.engine_name = "V69"
    engine.starter_torque = 10000
    engine.crank_mass = 2000
    engine.bore = 197.9
    engine.stroke = 197.9
    engine.chamber_volume = 3000
    engine.rod_length = engine.stroke * 1.75
    engine.simulation_frequency = 1200
    engine.max_sle_solver_steps = 4
    engine.fluid_simulation_steps = 4
    engine.idle_throttle_plate_position = 0.9

    engine.generate()
    engine.write_to_file("v69_engine.mr")

if __name__ == "__main__":
    generate_i4()
