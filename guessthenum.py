import random

nums = [0,1,2,3,4,5]
tries = 10
code_length = 4

def generate():
	code = []
	for _ in range(code_length):
		x = random.choice(nums)
		code.append(x)
	return code


def user_input():
    while True:
        guess = input("Guess:").split(",")
    
        if len(guess) != code_length:
            print("You must enter {} numbers".format(code_length))
            continue
        try:
            guess = [int(num) for num in guess]
            if all(0<=num<=9 for num in guess):
                return guess
            else:
                print("Enter numbers between 0 and 9 only.")
        except ValueError:
            print("Enter numbers only")
def check(guess_code, real_code):
    guess_nums = {}
    cpos = 0
    ipos = 0

    for guess in guess_code:
        if guess not in guess_nums:
            guess_nums[guess] = 0
        guess_nums[guess] += 1

    for guess_num, real_num in zip(guess_code, real_code):
        if int(guess_num) == int(real_num):
            cpos += 1
            guess_nums[guess_num] -= 1
     

    for guess_num, real_num in zip(guess_code, real_code):
        if guess_num in real_code and guess_nums[guess_num] > 0:
            ipos += 1
            guess_nums[guess_num] -= 1
       
    return cpos, ipos

def main():
	code = generate()
	print(code)
	for attempt in range(tries):
		guess = user_input()
		cpos,ipos = check(guess,code)
		if cpos == code_length: 
			print("You guessed the code in {} attempts.".format(attempt))
			play_again()
			break
		print("Correct positons : {} | Incorrect positions: {} ".format(cpos,ipos))
		
	else:
	    print("You couldn't guess the right code. The correct code is {}".format(code))
	    play_again()
	    
def play_again():
    x = input("Wanna play again? Type y or n: ").upper()
    if (x == 'Y'):
	    main()
	    

main()