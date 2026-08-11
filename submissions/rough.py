"""
1.LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

"""
def lesser_of_two_evens(num1,num2):

    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1,num2)
    else:
        return max(num1,num2)


print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

def animal_crackers(text):

    list_of_words = text.split()



    letter_1 = list_of_words[0][0]
    lestter_2 = list_of_words[1][0]

    if letter_1 == lestter_2:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))


def makes_twenty(num1,num2):

    sum_of_two = num1 + num2
    if num1 == 20 or num2 == 20:
        return True
    elif sum_of_two == 20:
        return True
    else:
        return False


print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))


# LEVEL 1 PROBLEMS

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(text):

    new_string = text.strip()

    string = f"{new_string[0].upper()+new_string[1:3]+new_string[3].upper()+new_string[4:]}"

    # for i in range(len(new_string)):

    #     if i == 0 or i == 3:
    #         string.join(new_string[i].upper())
    #     else:
    #         string.join(new_string(i))

    return string


print(old_macdonald('macdonald'))


"""
MASTER YODA: Given a sentence, return a sentence with the words reversed

"""

def master_yoda(text):

    list_of_words = text.split()

    reversert = " "

    for word in range(len(list_of_words)-1,-1,-1):
        reversert += list_of_words[word]

    return reversert

print(master_yoda('I am home'))
