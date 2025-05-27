class Converter:
    def convert_to_integer(self, expression):
        i = 0
        result = 0
        roman_numerals_list = list(expression)

        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        while i < len(roman_numerals_list):
            if roman_numerals_list[i] not in values:
                return None

            current_value = values[roman_numerals_list[i]]

            if i + 1 < len(roman_numerals_list):
                if roman_numerals_list[i + 1] not in values:
                    return None

                next_value = values[roman_numerals_list[i + 1]]

                if current_value < next_value:
                    result += next_value - current_value
                    i += 2
                    continue

            result += current_value
            i += 1

        return result

    def main(self):
        roman_numeral = input("Enter a Roman Numeral: ")
        integer_value = self.convert_to_integer(roman_numeral)

        if integer_value is not None:
            print(f"The integer value is: {integer_value}")
        else:
            print("Invalid Roman numeral entered.")

if __name__ == "__main__":
    converter = Converter()
    converter.main()