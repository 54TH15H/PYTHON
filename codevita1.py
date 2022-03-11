def fun():
	t = "fklcaedwxstimghbjnyzqropvu"
	inp = input()
	temp = []
	for i in inp:
		temp.append(t.index(i))
	temp.sort()
	for i in temp:
		print(t[i],end="")

fun()