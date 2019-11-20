# string project 1: FizzBuzz multiples of3 are Fizz multiples of 5 are Buzz and multiples of 3 and 5 are FizzBuzz


for number in range(1,101):
    if number%3 == 0 and number%5 ==0:
        print('FizzBuzz')
    elif number%3 == 0:
        print('Fizz')
    elif number%5 == 0:
        print('Buzz')
    else:
        print(number)


# string project 2: reverse a string


def reverse_string():

	while True:
		result = input('Please enter a word or sentance: ')
		print(result[::-1])

		result2 = input('Would you like to try again? (enter yes or no): ')
		if result2.lower() == 'yes':
			continue
		elif result2.lower() == 'no':
			print('Thank you.')
			break
		else:
			print('Please enter yes or no.')

reverse_string()


# string project 3: pig latin translator


def pig_latin():
    while True:
        result = input('Please enter a word: ')
        result.split()
        pig_word = result[1:] + result[0] + 'ay'
        pig_word.join('')
        print (pig_word)
        
        result2 = input('Would you like to try again? (enter yes or no): ')
        if result2.lower() == 'yes':
            continue
        elif result2.lower() == 'no':
            print('Thank you.')
            break
        else:
            print('Please enter yes or no.')

pig_latin()


# project 4: vowel checker


def vowel_checker():
    while True:
        vowels = ['a','e','i','u','o']

        vowel_counter = 0

        result = input('Please enter a word or sentance: ')
        result.split()

        for vowel in vowels:
            for letter in result:
                if vowel == letter:
                    vowel_counter += 1

        print(f"There are {vowel_counter} vowels in your string.")

        result2 = input('Would you like to try again? (enter yes or no): ')
        if result2.lower() == 'yes':
            continue
        elif result2.lower() == 'no':
            print('Thank you.')
            break
        else:
            print('Please enter yes or no.')

vowel_checker()


# string project 5: plaindrome check


def plaindrome_check():

	while True:
		result = input('Please enter a word: ')

		if result == result[::-1]:
			print(f'{result} is a palindrome!')
		else:
			print(f'{result} is not a plaindrome.')

		result2 = input('Would you like to try again? (enter yes or no): ')
		if result2.lower() == 'yes':
			continue
		elif result2.lower() == 'no':
			print('Thank you.')
			break
		else:
			print('Please enter yes or no.')

plaindrome_check()

# project 6: count words in a string

def word_counter():
    while True:
       
        word_count = 0

        result = input('Please enter a sentance: ')
        word_list = result.split()

        for word in word_list:
            word_count += 1

        print(f"There are {word_count} words in your sentance.")

        result2 = input('Would you like to try again? (enter yes or no): ')
        if result2.lower() == 'yes':
            continue
        elif result2.lower() == 'no':
            print('Thank you.')
            break
        else:
            print('Please enter yes or no.')

word_counter()

# progject 7: collatz Conjecture

def collatz():

    while True:
        
        step_counter = 0

        result = int(input('Please enter a number: '))
        
        n = result

        if n <= 1:
            print('Please enter a number larger than 1')
            continue
        else:

            while n != 1:
                if n%2 == 0:
                    n = n / 2
                    step_counter += 1
                
                elif n%2 != 0:
                    n = (n * 3) + 1
                    step_counter += 1

        print(f'Using Collatz Conjecture {result} takes {step_counter} steps to reach one')

        result2 = input('Would you like to try again? (enter yes or no): ')
        
        if result2.lower() == 'yes':
            continue
        elif result2.lower() == 'no':
            print('Thank you.')
            break
        else:
            print('Please enter yes or no.')
            
collatz()

# project 8: sieve of eratosthenes


numbers_to_check = []

prime_list = []


def check_if_prime(item):
    for i in range(2, item):
        if (item % i) == 0:
            break
    else:
        prime_list.append(item)        
        
def send_number_list():

    result = int(input('Please enter a number to represent a limit: '))

    for number in range(2, result+1):
        
        numbers_to_check.append(number)



send_number_list()

for item in numbers_to_check:
    check_if_prime(item)
        
print(prime_list)

