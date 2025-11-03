def fizzbuzz(n):
    """Returns 'Fizz' for multiples of 3, 'Buzz' for multiples of 5,
    and 'FizzBuzz' for multiples of both 3 and 5. Otherwise, returns the number as a string."""
    
    # Fix: Added the missing return statement for Buzz
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"  # Fix: Added the missing return statement for Buzz
    else:
        return str(n)

def test_fizzbuzz():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(30) == "FizzBuzz"

print("Please input a number:")
user_input = int(input())
print(fizzbuzz(user_input))
print(fizzbuzz(user_input))
print(fizzbuzz(user_input))
print(fizzbuzz(user_input))
print(fizzbuzz(user_input))
print(fizzbuzz(user_input))

test_fizzbuzz()
print("Thank you for using the FizzBuzz program!")