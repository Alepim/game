number = 42

while True:
	
	answer = input("Введите число: ")
	if not answer or answer == "exit":
		break
		
	if not answer.isdigit():
		print("Введите правильное число !")
		continue
		
	user_answer = int(answer)
		
	if user_answer > number:
		print("Загаданное число меньше")
	elif user_answer < number:
		print("Загаданное число больше")
	else:
		print("Число угадано")
		break
