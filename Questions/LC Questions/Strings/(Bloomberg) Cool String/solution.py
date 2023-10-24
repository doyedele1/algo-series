from collections import Counter

def is_cool_string(s):
  char_count = Counter(s)
  freq_count = Counter(char_count.values())
  print(char_count)
  print(freq_count)

  if len(freq_count) == 1: return True
  elif len(freq_count) == 2:
    freq1, freq2 = freq_count.keys()
    count1, count2 = freq_count.values()
    if (abs(freq1 - freq2) == 1 and
        (count1 == 1 or count2 == 1)) or (count1 == 1
                                          and freq1 == 1) or (count2 == 1
                                                              and freq2 == 1):
      return True

  return False

print(is_cool_string("aabbccdeee"))