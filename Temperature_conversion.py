# Global Constants
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_C = -273.15


def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)


def get_temperature_type():
    while True:
        temperature_type = input("Enter temperature type (C or F): ").upper()

        if temperature_type == "C" or temperature_type == "F":
            return temperature_type

        print("Invalid temperature type. Please enter C or F.")


def get_temperature(temperature_type):
    while True:
        try:
            temperature = float(input("Enter temperature: "))

            if temperature_type == "C":
                if temperature >= ABSOLUTE_ZERO_C:
                    return temperature
                print("Invalid temperature! Cannot be below absolute zero.")

            else:
                if temperature >= ABSOLUTE_ZERO_F:
                    return temperature
                print("Invalid temperature! Cannot be below absolute zero.")

        except ValueError:
            print("Invalid temperature! Please enter a number.")


def display_conversion(temperature_type, temperature):
    if temperature_type == "C":
        fahrenheit = (temperature * 9 / 5) + 32
        print("Temperature in Celsius:", temperature)
        print("Temperature in Fahrenheit:", fahrenheit)

    else:
        celsius = (temperature - 32) * 5 / 9
        print("Temperature in Fahrenheit:", temperature)
        print("Temperature in Celsius:", celsius)


if __name__ == "__main__":
    main()
