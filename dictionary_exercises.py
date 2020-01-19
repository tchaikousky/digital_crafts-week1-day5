####################################################################
#Provided dictionary                                               #
# Print Elizabeth's phone number.                                  #
# Add an entry to the dictionary: Kareem's number is 938-489-1234. #
# Delete Alice's phone entry.                                      #
# Change Bob's phone number to '968-345-2345'.                     #
# Print all the phone entries.                                     #
####################################################################
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict["Elizabeth"])
phonebook_dict["Kareem"] = "938-345-2345"
del phonebook_dict["Alice"]
phonebook_dict["Bob"] = "968-345-1234"
print(phonebook_dict)
#########################################################################
#Provided dictionaries                                                  #
# Write a python expression that gets the email address of Ramit.       #
# Write a python expression that gets the first of Ramit's interests.   #
# Write a python expression that gets the email address of Jasmine.     #
# Write a python expression that gets the second of Jan's two interests.#
#########################################################################

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print(ramit["name"])
print(ramit["interests"][0])
print(ramit["friends"][0]["email"])
print(ramit["friends"][1]["interests"][1])
###########################################################################################
# Write a letter_histogram program that asks the user for input, and prints a dictionary  #
# containing the tally of how many times each letter in the alphabet was used in the word.#
###########################################################################################

user_input = input("Please enter a word: ")
my_dict = {}
count = 0
input_list = []
loop_count = 0

while(count < len(user_input)):
    if(user_input[count] not in input_list):
        input_list.append(user_input[count])
    my_dict[user_input[count]] = 0
    count += 1

for letter in input_list:
    current_test = input_list[loop_count]
    letter_count = 0 
    count = 0
    loop_count +=1

    for character in user_input:
        if(current_test == user_input[count]):
            letter_count += 1
            my_dict[user_input[count]] += 1
        count += 1
        # print(str(current_test) + "-------" + str(letter_count))

print(my_dict)
#######################################################################################################
# Write a word_histogram program that asks the user for a sentence as its input, and prints           #
# a dictionary containing the tally of how many times each word in the alphabet was used in the text. #
#######################################################################################################

user_input = input("Please enter a sentence: ")
my_dict = {}
count = 0
input_list = []
loop_count = 0
word_list = []
current_word = ""

while(count < len(user_input)):
  
  if(user_input[count] != " "):
    current_word += user_input[count]
    # count += 1
    if(count == (len(user_input) -1)):
      input_list.append(current_word)
    count += 1
  else:
    input_list.append(current_word)
    current_word = ""
    count += 1

count = 0

while(count < len(input_list)):
    if(input_list[count] not in word_list):
        word_list.append(input_list[count])
    my_dict[input_list[count]] = 0
    count += 1

for word in word_list:
    current_test = word_list[loop_count]
    letter_count = 0 
    count = 0
    loop_count +=1

    for character in input_list:
        if(current_test == input_list[count]):
            letter_count += 1
            my_dict[input_list[count]] += 1
        count += 1

print(my_dict)
################################################################################
# Given a histogram tally (one returned from either letter_histogram           #
# or word_summary), print the top 3 words or letters.                          #
# Ignoring edge case of period on the end of the sentence(counting as new word)#
################################################################################

user_input = input("Please enter a sentence: ")
my_dict = {}
count = 0
input_list = []
loop_count = 0
word_list = []
current_word = ""
first_word = ""
second_word = ""
third_word = ""
first_word_value = 0
second_word_value = 0
third_word_value = 0
key_list = []
value_list = []
place_count = 0

while(count < len(user_input)):
  
  if(user_input[count] != " "):
    current_word += user_input[count]
    # count += 1
    if(count == (len(user_input) -1)):
      input_list.append(current_word)
    count += 1
  else:
    input_list.append(current_word)
    current_word = ""
    count += 1

count = 0

while(count < len(input_list)):
    if(input_list[count] not in word_list):
        word_list.append(input_list[count])
    my_dict[input_list[count]] = 0
    count += 1

for word in word_list:
    current_test = word_list[loop_count]
    letter_count = 0 
    count = 0
    loop_count +=1

    for character in input_list:
        if(current_test == input_list[count]):
            letter_count += 1
            my_dict[input_list[count]] += 1
        count += 1

for word in my_dict:
  key_list.append(word)
  value_list.append(my_dict[word])

for value in value_list:
  if(value > first_word_value):
    third_word = second_word
    third_word_value = second_word_value
    second_word = first_word
    second_word_value = first_word_value
    first_word = key_list[place_count]
    first_word_value = value_list[place_count]
    place_count += 1
  elif(value > second_word_value):
    third_word = second_word
    third_word_value = second_word_value
    second_word = key_list[place_count]
    second_word_value = value_list[place_count]
    place_count += 1
  elif(value > third_word_value):
    third_word = key_list[place_count]
    third_word_value = value_list[place_count]

print("The top three words are: \n%s: %d\n%s: %d\n%s: %d" % (first_word, first_word_value, 
second_word, second_word_value, third_word, third_word_value))
