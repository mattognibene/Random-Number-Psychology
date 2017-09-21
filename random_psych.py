#Matt Ognibene 9/21/17
#MIT License

#Theory:
#When people are asked to pick a random three digit number, they pick numbers that are not as random as they think.
#Most people will choose a number that appears random to them. For example, people are more likely to choose a number
#where there are no repeating digits (123, 492, etc) becuase it appears to be more random.

#Purpose:
#Collect test data (ask someone to give a random three digit number) and see if this theory is valid.
import random
test_data = open("test.txt", "r")
baseline_read = open("baseline.txt", "r")
pseudorandom_read = open("pseudorandom.txt", "r")

def main():
    generate_pseudorandom()
    present_data()

# -> Print
#prints out statistics
def present_data():
    print("Percentage of entrys that do not contain repeating digits")
    print("Test Data: "+ str(statistics(test_data)))
    print("Baseline: " + str(statistics(baseline_read)))
    print("Random Distribution: " + str(statistics(pseudorandom_read)))

#File -> Number
#reads in a file of test data containing 3 digit numbers on each
#line. it then checks for repeating digits, and returns a percentage
#of how many numbers DO NOT have repeating digits
def statistics(test_data):
    false_sum = 0
    total = 0
    for entry in test_data:
        entry = cleave(entry)
        total+=1
        if not check_repeats(entry):
            false_sum+=1

    return 100 * (false_sum/total)

#String -> Boolean
#if str has repeating digits, it returns true. false otherwise
def check_repeats(str):
    for i in range(len(str)-1):
        for p in range(i+1, len(str)):
            if str[i] == str[p]:
                return True
    return False

#String -> String
#cleaves of last char of str
def cleave(str):
    return str[0:(len(str)-1)]

# ->File
#generates a file of all numbers 000 -> 999 with each number being on its own line
#surves as a baseline to compare to
def generate_baseline():
    baseline_write = open("baseline.txt" "w")
    for i in range(0, 1000):
        string = str(i)
        while len(string)<3:
            string = "0" + string
        string = string + "\n"
        baseline_write.writelines(string)
    baseline_write.close()

# ->File
#generates a file of 1000 pseudo random numbers
def generate_pseudorandom():
    pseudorandom_write  = open("pseudorandom.txt", "w")
    for i in range(0, 1000):
        string = str(random.randint(0,1000))
        string+= "\n"
        pseudorandom_write.write(string)
    pseudorandom_write.close()

main()