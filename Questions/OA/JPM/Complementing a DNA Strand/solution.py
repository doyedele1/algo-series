def solution(s):
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    reversed_complement = ""

    for char in s:
        reversed_complement = complement[char] + reversed_complement

    return reversed_complement

# print(solution("GTCAG"))