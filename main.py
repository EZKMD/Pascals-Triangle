def factorial(n):
  result = 1
  for i in range(1, n+1):
      result *= i
  return result

def pascals_triangle(n):
    array = []
    for k in range(n + 1):
        coefficient = factorial(n) // (factorial(k) * factorial(n - k))
        term = coefficient
        array.append(term)
    return array

def main():
  choice = "y"
  while choice == "y":
    n = int(input("Which line of the pascals triangle do you want to be presented? "))
    print("=================================================================")
    expansion = pascals_triangle(n)
    print(expansion)
    print("=================================================================")  
    choice = str(input("Again? y/n "))
main()
