def get_nearest_lucky_ticket(ticket_number):
    middle = str(ticket_number).__len__() // 2
    end = 1000000
    ticket_temp_lucky = ticket_number
    if sum_digits(ticket_temp_lucky[:middle]) == sum_digits(ticket_temp_lucky[-middle:]):
        k = int(ticket_temp_lucky)
    else:
        for loop in range(int(ticket_temp_lucky) + 1, end):
            ticket_one = list(map(int, str(loop)))
            if check(ticket_one, ticket_temp_lucky) > 0:
                break
        temp = int(ticket_temp_lucky) + 1
        while temp > 0:
            ticket_two = list(map(int, str(temp)))
            if check(ticket_two, temp) >= 0:
                break
            temp -= 1
        k = choose_nearest(ticket_one, ticket_two, ticket_number)
    return k


def sum_digits(s):
    return sum(map(int, s))


def check(ticket, ticket_number):
    middle = str(ticket_number).__len__() // 2
    difference = -1
    if sum_digits(ticket[:middle]) == sum_digits(ticket[-middle:]):
        string_ticket = ''
        for i in range(len(ticket)):
            string_ticket += str(ticket[i])
        difference = abs(int(string_ticket) - int(ticket_number))
    return difference


def choose_nearest(ticket_one, ticket_two, ticket_number):
    temp = 100000
    first_ticket = 0
    second_ticket = 0
    for i in range(len(ticket_one)):
        first_ticket += ticket_one[i] * temp
        second_ticket += ticket_two[i] * temp
        temp //= 10
    if abs(first_ticket - int(ticket_number)) < abs(second_ticket - int(ticket_number)):
        result = first_ticket
    else:
        result = second_ticket
    return result


#if __name__ == '__main__':
    #print(get_nearest_lucky_ticket(input()))
