def check_palindrome_1(avtobuska):
    reversed_avtobuska = avtobuska[::-1]
    status = 1
    if (avtobuska != reversed_avtobuska):
        status = 0
    return status

avtobuska = "fsdfdsf"
status= check_palindrome_1(avtobuska)
if(status == 1):
    print("It is a palindrome ")
else:
    print("Sorry! Try again")
