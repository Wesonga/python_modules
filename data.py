try:
    num = input("Enter a number: ")


    num_int = int(num)
    num_float = float(num)

    int_add_10 = num_int + 10
    int_mult_2 = num_int * 2

    float_add_10 = num_float + 10
    float_mult_2 = num_float * 2

    # interger results
    print(f"value: {num_int}, data type: {type(num_int)}")
    print(f"After + 10: {int_add_10}, data type: {type(int_add_10)}")
    print(f"After * 10: {int_mult_2}, data type: {type(int_mult_2)}")

    # float results
    print(f"value: {num_float}, data type: {type(num_float)}")
    print(f"After + 10: {float_add_10}, data type: {type(float_add_10)}")
    print(f"After * 10: {float_mult_2}, data type: {type(float_mult_2)}")

except ValueError:
    print("Error: You entered a non numerical string.")