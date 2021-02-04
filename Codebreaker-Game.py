#!/usr/bin/env python

# Code breaking game
# Written by TeknoBen96
# Up-to-par on 2/1/2021
# Thought up on 1/18/2021


import random
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--max", dest="max_value", help="The highest value allowed in the code (0-max). Defaults to 5 (0-5)")
    parser.add_argument("-l", "--length", dest="code_length", help="The length of the code. Defaults to 4")
    args = parser.parse_args()

    if not args.max_value:
        args.max_value = 5
    if not args.code_length:
        args.code_length = 4
    return int(args.code_length), int(args.max_value)


class Codebreaker:
    def __init__(self, code_len, high):
        self.code_len = code_len
        self.high = high


    def rand(self, low, high):
        float_num = round(random.random() * high) + low
        num = str(float_num).split(".")[0]
        return int(num)

    def generate_random_array(self, length, high):
        rand_array = []
        for i in range(0, length, 1):
            num = self.rand(0, high)
            rand_array.append(str(num))
        return rand_array

    def guess(self, code_length):
        guess_array = []
        guess_string = str(raw_input("Guess the " + str(self.code_len) + " digit code, max value is " + str(self.high) + " >> "))
        guess_len = len(guess_string)
        while guess_len < code_length or guess_len > code_length:
            guess_string = str(raw_input("Your guess needs to be " + str(code_length) + " characters long >> "))
            guess_len = len(guess_string)

        for i in range(0, self.code_len, 1):
            guess_array.append(guess_string[i])
        # print(str(guess_array))
        return guess_array

    # I could do this using array[i] = some_value. But this gives me the index of the value.
    def change_item_in_array(self, array, item, new_value):
        index_of_item = array.index(item)
        item = array[index_of_item]
        array[index_of_item] = new_value
        return item, index_of_item

    # This updates the items in "array" with the values provided by updated_array
    def update_items_in_array(self, array, updated_array):
        for i in range(0, len(updated_array), 1):
            array[updated_array[i][0]] = updated_array[i][1]

    def proccess_guess(self, guess_array, code_array):
        updated_code_items = []
        updated_guess_items = []
        result = ""
        length = len(code_array)
        if guess_array == code_array:
            return "CORRECT"

        # If guess not == to code, compare individual index's values
        elif not guess_array == code_array:
            for i in range(0, length, 1):
                if guess_array[i] == code_array[i]:
                    # this keeps track of which indices were changed, so they can be changed back later.
                    #################################################
                    item_in_code, index_of_item_in_code = self.change_item_in_array(code_array, guess_array[i], "random-value-zero")
                    updated_code_items.append([index_of_item_in_code, item_in_code])
                    item_in_guess, index_of_item_in_guess = self.change_item_in_array(guess_array, guess_array[i], "jahgaha621")
                    updated_guess_items.append([index_of_item_in_guess, item_in_guess])
                    #################################################
                    result += "X"

            # This is used after the first check is run on all of the indices
            second_guess_array = guess_array
            for i in range(0, length, 1):
                if second_guess_array[i] in code_array:
                    item, index_of_item = self.change_item_in_array(code_array, second_guess_array[i], "random-value-three")
                    updated_code_items.append([index_of_item, item])
                    result += "O"
            # Since code_array will probably have some items changed to a random value,
            # and I was having some strange problems with the code array in the outer-scope
            # being modified by this method, this for loop resets the
            # indices with their original value
            # for i in range(0, len(updated_code_items), 1):
            #     # updated_items = [[INDEX_1, x], [INDEX_2, x]] x = value
            #     # updated_items[0][0] -> INDEX_1
            #     # updated_items[0][1] -> x
            #     code_array[updated_code_items[i][0]] = updated_code_items[i][1]
            self.update_items_in_array(code_array, updated_code_items)
            self.update_items_in_array(second_guess_array, updated_guess_items)

        return result

    def run(self):
        is_winning = True
        guess_num = 0
        code_array = self.generate_random_array(self.code_len, self.high)
        result = ""
        command = ["s", "h", "o", "w"]
        while not result == "CORRECT":
            try:
                guess_array = self.guess(self.code_len)
                if guess_array == command:
                    print(code_array)
                    is_winning = False

                result = self.proccess_guess(guess_array, code_array)
                print("Your guess >> " + str(guess_array))
                print("Result >> " + result)
                guess_num += 1
            except KeyboardInterrupt:
                exit("\nGoodbye.")
        if is_winning:
            print("You win!\nIt took you " + str(guess_num) + " guesses.")
        else:
            print("You looked at the code. You lose.")


code_length, max_value = get_args()
game = Codebreaker(code_length, max_value)
game.run()
