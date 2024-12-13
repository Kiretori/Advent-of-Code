with open("day13/input13.txt", "r") as f:
    adv_input = f.read()

adv_input = adv_input.split("\n\n")


def parse_systems(adv_input, offset=0):
    systems = []
    for section in adv_input:
        section = section.splitlines()
        line1 = section[0][12:].split(",")
        line2 = section[1][12:].split(",")
        line3 = section[2][9:].split(",")
        a1, a2 = int(line1[0]), int(line1[1][3:])
        b1, b2 = int(line2[0]), int(line2[1][3:])
        c1, c2 = offset + int(line3[0]), offset + int(line3[1][3:])
        system = {
            "a1": a1,
            "b1": b1,
            "c1": c1,
            "a2": a2,
            "b2": b2,
            "c2": c2,
        }

        systems.append(system)
    return systems


def det(a, b, c, d):
    return a * d - b * c


def get_solution(a1, b1, c1, a2, b2, c2):
    coeff_det = det(a1, b1, a2, b2)
    x_det = det(c1, b1, c2, b2)
    y_det = det(a1, c1, a2, c2)

    x = x_det // coeff_det
    y = y_det // coeff_det

    return (x, y)


# Part 1
part1_systems = parse_systems(adv_input)

sum1 = 0

for system in part1_systems:
    a1, a2 = system["a1"], system["a2"]
    b1, b2 = system["b1"], system["b2"]
    c1, c2 = system["c1"], system["c2"]

    x, y = get_solution(a1, b1, c1, a2, b2, c2)

    if (a1 * x) + (b1 * y) == c1 and (a2 * x) + (b2 * y) == c2:
        sum1 += 3 * x + y


print(sum1)


# Part 2

part2_systems = parse_systems(adv_input, offset=10000000000000)

sum2 = 0

for system in part2_systems:
    a1, a2 = system["a1"], system["a2"]
    b1, b2 = system["b1"], system["b2"]
    c1, c2 = system["c1"], system["c2"]

    x, y = get_solution(a1, b1, c1, a2, b2, c2)

    if (a1 * x) + (b1 * y) == c1 and (a2 * x) + (b2 * y) == c2:
        sum2 += 3 * x + y


print(sum2)
