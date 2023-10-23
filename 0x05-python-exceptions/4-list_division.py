#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            value1 = my_list_1[i] if i < len(my_list_1) else 0
            value2 = my_list_2[i] if i < len(my_list_2) else 0
            division = value1 / value2
        except ZeroDivisionError:
            division = 0
            print("division by 0")
        except (ValueError, TypeError):
            division = 0
            print("wrong type")
        except IndexError:
            division = 0
            print("out of range")
        finally:
            result.append(division)
    return (result)
