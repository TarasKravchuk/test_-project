while True:

    number = float(input("input your float "))
    numbers_after_comma = int (input("input numbers after comma "))

    def rounding_numbers (number, numbers_after_comma):
        number_str = str(number)
        number_split = number_str.split(".")
        if numbers_after_comma is 0:
            if int(number_split[1][0]) > 4:
                return print(float(number_split[0])+1)
            elif int(number_split[1][0]) < 5:
                return print(float(number_split[0]))

        elif int(number_split[1][numbers_after_comma]) < 5 or int(number_split[1][numbers_after_comma]) is 9:
            result = print(float(number_split[0] + "." + number_split[1][: int(numbers_after_comma)]))

        elif len(number_split[1]) <= int(numbers_after_comma):
            return print (float(number_split[0] + "." + number_split[1]))

        elif int(number_split[1][numbers_after_comma]) > 4:
            old_numer_split = number_split[1]
            new_number_split = str(int(number_split[1][numbers_after_comma-1]) +1)
            str_replace = str (number_split[1][int(numbers_after_comma)])
            str_replace = str_replace + new_number_split
            result = float(str(number_split[0]) + "." + str(number_split[1][: int(numbers_after_comma-1)]) + new_number_split)
            return print(result)

        else: print("Houston we have a problem")

    rounding_numbers(number, numbers_after_comma)