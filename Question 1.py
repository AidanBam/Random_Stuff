print("Hello, my name is Eliza. What would you like to talk about?")
while True:
    question = input()
    question = question.lower()
    feel_test = question.count("feel")
    struggle_test = question.count("i am")
    easy_test_1 = question.count("you")
    easy_test_2 = question.count("me")
    print(feel_test)
    print(struggle_test)
    print(easy_test_1)
    print(easy_test_2)

    if feel_test == 1:
        print("Do you often feel that way?.")
    elif struggle_test == 1:
        print("2")
        question_list = question.split()
        question_list.
        print(question_list)
    elif easy_test_1 == 1 and easy_test_2 == 1:
        print("3")
        #DO
    elif question == "go away":
        print("I hope I have helped you!")
        exit()
        #Done
    else:
        print("Please go on")
        #Done