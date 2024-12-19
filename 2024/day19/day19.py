with open("day19/input19.txt", "r") as f:
    adv_input = f.read()

substrings, strings = adv_input.split("\n\n")
strings = strings.split("\n")
substrings = set([sub.strip() for sub in substrings.split(",")])

def solve1(s, substrings):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in substrings:
                dp[i] = True
                break
    return dp[n]

def solve2(s, substrings):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in substrings:
                dp[i] += dp[j]
    return dp[n]

def part1(strings, substrings):
    result = 0
    for string in strings:
        result += solve1(string, substrings)

    return result

print(part1(strings,substrings))

def part2(strings, substrings):
    result = 0
    for string in strings:
        result += solve2(string, substrings)

    return result

print(part2(strings,substrings))


