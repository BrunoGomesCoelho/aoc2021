def parse_input(inp):
    return "".join(f"{int(x, 16):04b}" for x in inp)


def parse_binary(binary):
    """ returns version_sum, end
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
        return version_sum, end

    else:  # operator
        len_type_id = binary[6]

        if len_type_id == "0":
            # the next 15 bits are a number that represents the total length in bits
            # of the sub-packets contained by this packet.
            sub_packet_len = int(binary[7:22], 2)
            beg, end = 22, 22+sub_packet_len

            while beg != end:
                next_sum, next_end = parse_binary(binary[beg:end])
                version_sum += next_sum
                beg = beg+next_end

        else:
            # the next 11 bits are a number that represents the number of sub-packets
            # immediately contained by this packet.
            num_sub_packet = int(binary[7:18], 2)
            beg, end = 18, len(binary)

            for _ in range(num_sub_packet):
                next_sum, next_end = parse_binary(binary[beg:end])
                version_sum += next_sum
                beg = beg+next_end
            end = beg

        return version_sum, end

assert parse_binary(parse_input("D2FE28"))[0] == 6
assert parse_binary(parse_input("38006F45291200"))[0] == 9
assert parse_binary(parse_input("EE00D40C823060"))[0] == 14
assert parse_binary(parse_input("8A004A801A8002F478"))[0] == 16
assert parse_binary(parse_input("620080001611562C8802118E34"))[0] == 12
assert parse_binary(parse_input("C0015000016115A2E0802F182340"))[0] == 23
assert parse_binary(parse_input("A0016C880162017C3686B18A3D4780"))[0] == 31

print(parse_binary(parse_input(input()))[0])
