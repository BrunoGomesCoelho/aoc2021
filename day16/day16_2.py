from math import prod

def parse_input(inp):
    return "".join(f"{int(x, 16):04b}" for x in inp)


def parse_operator(id, numbers):
    match int(id, 2):
        case 0: return sum(numbers)
        case 1: return prod(numbers)
        case 2: return min(numbers)
        case 3: return max(numbers)

        case 5 if len(numbers) == 2:
            return int(numbers[0] > numbers[1])

        case 6 if len(numbers) == 2:
            return int(numbers[0] < numbers[1])

        case 7 if len(numbers) == 2:
            return int(numbers[0] == numbers[1])

    raise NotImplementedError(f"{numbers=}")


def parse_binary(binary):
    """ returns operation(numbers), end
    """
    version, id = binary[:3], binary[3:6]
    version_sum = int(version, 2)

    if id == "100":  # literal value
        num, count = "", 0

        while True:
            flag, *partial_num = binary[6+5*count:6+5*(count+1)]
            num += "".join(partial_num)
            count += 1
            if flag == "0":
                break

        end = 6+5*count
        return int(num, 2), end

    else:  # operator
        len_type_id = binary[6]
        numbers = []

        if len_type_id == "0":
            # the next 15 bits are a number that represents the total length in bits
            # of the sub-packets contained by this packet.
            sub_packet_len = int(binary[7:22], 2)
            beg, end = 22, 22+sub_packet_len

            while beg != end:
                next_num, next_end = parse_binary(binary[beg:end])
                numbers.append(next_num)
                beg = beg+next_end

        else:
            # the next 11 bits are a number that represents the number of sub-packets
            # immediately contained by this packet.
            num_sub_packet = int(binary[7:18], 2)
            beg, end = 18, len(binary)

            for _ in range(num_sub_packet):
                next_num, next_end = parse_binary(binary[beg:end])
                numbers.append(next_num)
                beg = beg+next_end
            end = beg

        return parse_operator(id, numbers), end

assert parse_binary(parse_input("C200B40A82"))[0] == 3
assert parse_binary(parse_input("04005AC33890"))[0] == 54
assert parse_binary(parse_input("880086C3E88112"))[0] == 7
assert parse_binary(parse_input("CE00C43D881120"))[0] == 9
assert parse_binary(parse_input("D8005AC2A8F0"))[0] == 1
assert parse_binary(parse_input("F600BC2D8F"))[0] == 0
assert parse_binary(parse_input("9C005AC2F8F0"))[0] == 0
assert parse_binary(parse_input("9C0141080250320F1802104A08"))[0] == 1

print(parse_binary(parse_input(input()))[0])
