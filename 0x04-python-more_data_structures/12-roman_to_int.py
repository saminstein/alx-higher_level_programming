def roman_to_int(roman_string):
  r_numerals = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000
    }
    
  if roman_string is None or type(roman_string) is not str:
    return 0
    
  result = 0
  for i in range(0, len(roman_string)):
    value = r_numerals[roman_string[i]]
    if i + 1 < len(roman_string) and r_numerals[roman_string[i + 1]] > value:
      result -= value
    else:
      result += value
  return result