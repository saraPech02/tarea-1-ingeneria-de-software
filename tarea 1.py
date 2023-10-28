user_input = input("por favor ingrese su numero de serie procura dejar espacios: ")
numbers_str = user_input.split()
numbers = [int(num) for num in numbers_str]
sorted_numbers = sorted(numbers, reverse=True)
print("aqui tiene sus numeros ordenados:", sorted_numbers)
print ("fue un placer para mi ayudar")  
