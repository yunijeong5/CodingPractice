def intToRoman(num):
      # examples
      # 49 => 40 + 9 => XLIX
      # 46 => 40 + 5 + 1 => XLVI
      # 45 => 40 + 5 => XLV
      # 44 => 40 + 4 => XLIV
      # 33 => 10 + 10 + 10 + 1 + 1 + 1 => XXXIII
      
      # map of symbols and values
      romans = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
      }
      
      result = ''
      
      # go through 1000 ... 1, and extract (subtract) chunck of numbers that can be mapped into a symbol
      # might have to extract multiple chuncks of the same size
      
      chunks = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
      
      for i in chunks:
        while num >= i:
          result += romans[i]
          num -= i
      
      return result