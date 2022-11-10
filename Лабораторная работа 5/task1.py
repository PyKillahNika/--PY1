# TODO решить с помощью list comprehension и распечатать его
import pprint as p
n = 15  # наибольшее число для генерации (включительно)
p.pprint([({"bin": bin(each), "dec": each, "hex": hex(each), "oct": oct(each)}) for each in range(n+1)])
