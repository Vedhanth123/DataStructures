print("lets start")


# case 1: [1,2,3,4,5]
def input_array_format_comma_seperated():

    new_list = list(map(int, input().strip("[]").split(",")))
    return new_list


def input_array_space_seperated():

    new_list = list(map(int, input().split()))
    return new_list


def input_array_comma_seperated():

    new_list = list(map(int, input().split(",")))
    return new_list

def input_array_size_not_given():

    arr = []
    while True:
        try:
            num = input().strip()
            if not num:
                break
            arr.extend(map(int, num.split()))
        except ValueError:
            print("Enter integer values")

    return arr

