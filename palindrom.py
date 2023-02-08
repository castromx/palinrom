#паліндром, це ті слова які читаються однаково (зараз, око), або рядок по типу fghhgf
#найпростіші паліндроми, це коли в нас буде пустий рядок, або рядок з одного символу '' 'a'
def palindrom(s):
	if len(s)<=1:#якщо довжина нашого рядка буде менше, або дорівнювати 1, отже це поліндром
		return True
	#а якщо маємо слово більше, тоді виконуємо наступні перевірки
	if s[0]!=s[-1]:#якщо перший символ і останній буде недорівнювати один одному, повертаємо False
		return False
	return palindrom(s[1:-1])#і перевіряємо останні символ 

print(palindrom('зараз'))#True
print(palindrom('asddsa'))#True
print(palindrom(''))#True
print(palindrom('e'))#True
print(palindrom('ee'))#True
print(palindrom('рядок'))#False