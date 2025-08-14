# def stringAnagram(dictionary):


def anagrams(dictionary):
    results = {}
    def permute(s):
        if len(s) == 1:
            return [s]
        perms = []
        for i, j in enumerate(s):
            rest = s[:i] + s[i+1:]
            for p in permute(rest):
                perms.append(j + p)
        return perms

    for w in dictionary:
        results[w] = set(permute(w))
    return results

    # anagram_map = {}
    #     for word in dictionary:
    #         sorted_word = ''.join(sorted(word))
    #         anagram_map[sorted_word] = anagram_map.get(sorted_word, 0) + 1

    #     # For each query, check how many dictionary words have the same sorted form
    #     result = []
    #     for q in query:
    #         sorted_q = ''.join(sorted(q))
    #         result.append(anagram_map.get(sorted_q, 0))
        
    #     return result


# dictionary = ["hack", "a", "rank", "khac", "ackh", "kran", "rankhacker", "a", "ab", "ba", "stairs", "raits"]
dictionary = ["hack", 'eat']
print(anagrams(dictionary))
query = ["a", "nark", "bs", "hack", "stair"]