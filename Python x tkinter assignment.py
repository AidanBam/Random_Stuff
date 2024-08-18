import tkinter as tk
import random

class PyQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyQuiz")
        self.geometry("800x600")
        self.configure(bg="light gray")
        self.option_add('*Background', 'light gray')
        self.option_add('*Foreground', 'black')

        self.questions = {
            "multiple_choice": {
                "Which data type would you use for storing a sentence": ["String", "Integer", "Boolean", "Floating point", 0, 1],
                "Which data type would you use for storing a number": ["String", "Integer", "Boolean", "Floating point", 1, 1],
                "Which data type would you use for storing a decimal": ["String", "Integer", "Boolean", "Floating point", 3, 1],
                "Which data type would you use for storing True or False": ["String", "Integer", "Boolean", "Floating point", 2, 1],
                "What is the primary purpose of encapsulation in object-oriented programming": ["To hide implementation details and restrict access to data", "To organise code into reusable components", "To define the relationship between classes and objects", "To enable code execution in multiple threads simultaneously", 0, 2],
                "Which term describes the ability of an object to take on multiple forms?": ["Encapsulation", "Polymorphism", "Inheritance", "Abstraction", 1, 2],
                "What is a class in object-oriented programming?": ["An instance of an object", "A method for modifying object properties", "A variable used to store object data", "A blueprint for creating objects", 3, 2],
                "What does inheritance enable in object-oriented programming?": ["Reusability of code and behaviour", "Encapsulation of data and behaviour", "Polymorphism across different classes", "Dynamic binding of methods and properties", 0, 3],
                "What is the purpose of the constructor method in a class?": ["To initialise the state of an object", "To create new instances of the class", "To define the behaviour of the class", "To destroy objects when they are no longer needed", 0, 3],
                "Which OOP concept emphasises bundling data and methods that operate on the data into a single unit?": ["Encapsulation", "Abstraction", "Inheritance", "Polymorphism", 0, 3]
            },
            "fill_in_the_blank": {
                "Computers themselves are physical devices that are manufactured and don't inherently possess the ability to execute complex tasks without ___________.": ["programming", 1, 1],
                "Initially, computers were programmed using low-level languages like ___________ or assembly language.": ["machine code", 3, 3],
                "Higher-level languages abstract away many of the complexities of the underlying hardware and provide more ___________ syntax.": ["readable", 1, 1],
                "Regardless of the programming language used, the code is written on a variety of platforms, ranging from simple text editors to integrated development environments (IDEs) like ___________.": ["Visual Studio", 2, 2],
                "In object-oriented programming, data and operations are treated as self-contained units called ___________.": ["objects", 2, 2]
            },
            "rank_in_order": {
                "Rank the following programming languages in order of their popularity for object-oriented programming: Python, Java, C++, Ruby.": ["Java", "Python", "C++", "Ruby", 1],
                "Rank the following stages of the software development process in order of occurrence: Alpha testing, Beta testing, Code optimization, Requirement analysis.": ["Requirement analysis", "Code optimization", "Alpha testing", "Beta testing", 0],
                "Rank the following programming paradigms in order of their historical emergence: Imperative programming, Object-oriented programming, Functional programming, Logic programming.": ["Imperative programming", "Object-oriented programming", "Functional programming", "Logic programming", 0],
                "Rank the following components of an object-oriented paradigm in order of their importance for creating self-contained units: Encapsulation, Polymorphism, Inheritance, Abstraction.": ["Encapsulation", "Abstraction", "Inheritance", "Polymorphism", 0],
                "Rank the following programming techniques in order of their importance for developing well-structured solutions: Use of a clear modular structure, Elegance of solution, Writing for subsequent maintenance, Mainline approach to complex solution.": ["Writing for subsequent maintenance", "Use of a clear modular structure", "Elegance of solution", "Mainline approach to complex solution", 0]
            }
        }

        self.current_question = None
        self.question_type = None
        self.question_frame = tk.Frame(self, bg="light gray")
        self.question_frame.pack(pady=20)
        self.answered_questions = set()

        self.own_work_frame = tk.Frame(self, bg="light gray")
        self.own_work_frame.pack(pady=20)
        own_work_label = tk.Label(self.own_work_frame, text="Is this all your own work?", font=("Arial", 16), bg="light gray")
        own_work_label.pack(pady=10)
        yes_button = tk.Button(self.own_work_frame, text="YES", font=("Arial", 12), bg="white", fg="black", command=self.start_quiz)
        yes_button.pack(side="left", padx=10)
        no_button = tk.Button(self.own_work_frame, text="NO", font=("Arial", 12), bg="white", fg="black", command=self.destroy)
        no_button.pack(side="right", padx=10)

    def start_quiz( self ):
        self.own_work_frame.pack_forget( )
        self.clear_question_frame( )
        self.answered_questions = set( )  # Reset answered questions set
        self.question_types = [ "multiple_choice", "fill_in_the_blank", "rank_in_order" ]
        random.shuffle( self.question_types )  # Shuffle the question types
        self.display_next_question( )

    def display_next_question( self ):
        if len( self.answered_questions ) == sum( len( self.questions[ q_type ] ) for q_type in self.questions ):
            self.show_result( )
            return

        if not self.question_types:
            self.show_result( )
            return

        self.question_type = self.question_types.pop( 0 )

        if self.question_type == "multiple_choice":
            remaining_questions = [ question for question in self.questions[ "multiple_choice" ] if question not in self.answered_questions ]
            if not remaining_questions:
                self.display_next_question( )
                return
            self.current_question = random.choice( remaining_questions )
            self.display_multiple_choice_question( )
        elif self.question_type == "fill_in_the_blank":
            remaining_questions = [ question for question in self.questions[ "fill_in_the_blank" ] if question not in self.answered_questions ]
            if not remaining_questions:
                self.display_next_question( )
                return
            self.current_question = random.choice( remaining_questions )
            self.display_fill_in_the_blank( )
        elif self.question_type == "rank_in_order":
            remaining_questions = [ question for question in self.questions[ "rank_in_order" ] if question not in self.answered_questions ]
            if not remaining_questions:
                self.display_next_question( )
                return
            self.current_question = random.choice( remaining_questions )
            self.display_rank_in_order()

    def display_multiple_choice_question( self ):
        self.clear_question_frame( )

        question_data = self.questions[ self.question_type ][ self.current_question ]
        question_text = self.current_question
        options = question_data[ 0:-2 ]  # Extracting the options (from index 1 to second last element)
        correct_index = question_data[ -2 ]  # Last but one element is the correct index
        difficulty = question_data[ -1 ]  # Last element is the difficulty level

        question_label = tk.Label( self.question_frame, text = question_text, font = ("Arial", 14), wraplength = 400 )
        question_label.pack( pady = 10 )

        for i, option_text in enumerate( options ):
            option_button = tk.Button( self.question_frame, text = option_text, font = ("Arial", 12), bg = "white", fg = "black",
                                       command = lambda i = i: self.check_answer( i ) )
            option_button.pack( pady = 5 )

    def display_fill_in_the_blank(self):
        self.clear_question_frame()

        question_data = self.questions[ self.question_type ][ self.current_question ]
        question_text = self.current_question
        correct_answer = question_data[0]
        difficulty = question_data[2]
        question_label = tk.Label(self.question_frame, text=question_text, font=("Arial", 14), wraplength=400)
        question_label.pack(pady=10)

        answer_entry = tk.Entry(self.question_frame, font=("Arial", 12))
        answer_entry.pack(pady=10)

        submit_button = tk.Button(self.question_frame, text="Submit", font=("Arial", 12), bg="white", fg="black", command=lambda: self.check_fill_in_the_blank(answer_entry.get(), correct_answer))
        submit_button.pack(pady=5)

    import tkinter as tk
    import random

    class PyQuiz( tk.Tk ):
        def __init__( self ):
            super( ).__init__( )
            self.title( "PyQuiz" )
            self.geometry( "800x600" )
            self.configure( bg = "light gray" )
            self.option_add( '*Background', 'light gray' )
            self.option_add( '*Foreground', 'black' )

            self.questions = {
                    "multiple_choice":   {
                            "Which data type would you use for storing a sentence":                                                [ "String",
                                                                                                                                     "Integer",
                                                                                                                                     "Boolean",
                                                                                                                                     "Floating point",
                                                                                                                                     0, 1 ],
                            "Which data type would you use for storing a number":                                                  [ "String",
                                                                                                                                     "Integer",
                                                                                                                                     "Boolean",
                                                                                                                                     "Floating point",
                                                                                                                                     1, 1 ],
                            "Which data type would you use for storing a decimal":                                                 [ "String",
                                                                                                                                     "Integer",
                                                                                                                                     "Boolean",
                                                                                                                                     "Floating point",
                                                                                                                                     3, 1 ],
                            "Which data type would you use for storing True or False":                                             [ "String",
                                                                                                                                     "Integer",
                                                                                                                                     "Boolean",
                                                                                                                                     "Floating point",
                                                                                                                                     2, 1 ],
                            "What is the primary purpose of encapsulation in object-oriented programming":                         [
                                    "To hide implementation details and restrict access to data", "To organise code into reusable components",
                                    "To define the relationship between classes and objects",
                                    "To enable code execution in multiple threads simultaneously", 0, 2 ],
                            "Which term describes the ability of an object to take on multiple forms?":                            [ "Encapsulation",
                                                                                                                                     "Polymorphism",
                                                                                                                                     "Inheritance",
                                                                                                                                     "Abstraction", 1,
                                                                                                                                     2 ],
                            "What is a class in object-oriented programming?":                                                     [
                                    "An instance of an object", "A method for modifying object properties", "A variable used to store object data",
                                    "A blueprint for creating objects", 3, 2 ],
                            "What does inheritance enable in object-oriented programming?":                                        [
                                    "Reusability of code and behaviour", "Encapsulation of data and behaviour",
                                    "Polymorphism across different classes", "Dynamic binding of methods and properties", 0, 3 ],
                            "What is the purpose of the constructor method in a class?":                                           [
                                    "To initialise the state of an object", "To create new instances of the class",
                                    "To define the behaviour of the class", "To destroy objects when they are no longer needed", 0, 3 ],
                            "Which OOP concept emphasises bundling data and methods that operate on the data into a single unit?": [ "Encapsulation",
                                                                                                                                     "Abstraction",
                                                                                                                                     "Inheritance",
                                                                                                                                     "Polymorphism",
                                                                                                                                     0, 3 ]
                    },
                    "fill_in_the_blank": {
                            "Computers themselves are physical devices that are manufactured and don't inherently possess the ability to execute complex tasks without ___________.":                                       [
                                    "programming", 1, 1 ],
                            "Initially, computers were programmed using low-level languages like ___________ or assembly language.":                                                                                        [
                                    "machine code", 3, 3 ],
                            "Higher-level languages abstract away many of the complexities of the underlying hardware and provide more ___________ syntax.":                                                                [
                                    "readable", 1, 1 ],
                            "Regardless of the programming language used, the code is written on a variety of platforms, ranging from simple text editors to integrated development environments (IDEs) like ___________.": [
                                    "Visual Studio", 2, 2 ],
                            "In object-oriented programming, data and operations are treated as self-contained units called ___________.":                                                                                  [
                                    "objects", 2, 2 ]
                    },
                    "rank_in_order": {
                            "Question 1": {
                                    "text":          "Rank the following programming languages in order of their popularity for object-oriented programming:",
                                    "options":       [ "Java", "Python", "C++", "Ruby" ],
                                    "correct_order": [ "Java", "Python", "C++", "Ruby" ],
                                    "difficulty":    1
                            },
                            "Question 2": {
                                    "text":          "Rank the following stages of the software development process in order of occurrence:",
                                    "options":       [ "Requirement analysis", "Code optimization", "Alpha testing", "Beta testing" ],
                                    "correct_order": [ "Requirement analysis", "Code optimization", "Alpha testing", "Beta testing" ],
                                    "difficulty":    2
                            },
                            "Question 3": {
                                    "text":          "Rank the following programming paradigms in order of their historical emergence:",
                                    "options":       [ "Imperative programming", "Object-oriented programming", "Functional programming",
                                                       "Logic programming" ],
                                    "correct_order": [ "Imperative programming", "Object-oriented programming", "Functional programming",
                                                       "Logic programming" ],
                                    "difficulty":    3
                            },

                    }

            }

            self.current_question = None
            self.question_type = None
            self.question_frame = tk.Frame( self, bg = "light gray" )
            self.question_frame.pack( pady = 20 )
            self.answered_questions = set( )

            self.own_work_frame = tk.Frame( self, bg = "light gray" )
            self.own_work_frame.pack( pady = 20 )
            own_work_label = tk.Label( self.own_work_frame, text = "Is this all your own work?", font = ("Arial", 16), bg = "light gray" )
            own_work_label.pack( pady = 10 )
            yes_button = tk.Button( self.own_work_frame, text = "YES", font = ("Arial", 12), bg = "white", fg = "black", command = self.start_quiz )
            yes_button.pack( side = "left", padx = 10 )
            no_button = tk.Button( self.own_work_frame, text = "NO", font = ("Arial", 12), bg = "white", fg = "black", command = self.destroy )
            no_button.pack( side = "right", padx = 10 )

        def start_quiz( self ):
            self.own_work_frame.pack_forget( )
            self.clear_question_frame( )
            self.answered_questions = set( )  # Reset answered questions set
            self.question_types = [ "multiple_choice", "fill_in_the_blank", "rank_in_order" ]
            random.shuffle( self.question_types )  # Shuffle the question types
            self.display_next_question( )

        def display_next_question( self ):
            total_parts = sum(
                    len( question_data ) - 2 for question_type in self.questions for question_data in self.questions[ question_type ].values( ) )
            answered_parts = sum( 1 for question_type in self.questions for question_data in self.questions[ question_type ].values( ) if
                                  question_data in self.answered_questions )

            if answered_parts == total_parts:
                self.show_result( )
                return

            # If there are no more question types or the question types list is empty, show results
            if not self.question_types:
                self.show_result( )
                return

            # Get the next question type and remove it from the list
            self.question_type = self.question_types.pop( 0 )

            # Display the next question based on the question type
            if self.question_type == "multiple_choice":
                self.display_multiple_choice_question( )
            elif self.question_type == "fill_in_the_blank":
                self.display_fill_in_the_blank( )
            elif self.question_type == "rank_in_order":
                self.display_rank_in_order( )

        def display_multiple_choice_question( self ):
            self.clear_question_frame( )

            question_data = self.questions[ self.question_type ][ self.current_question ]
            question_text = self.current_question
            options = question_data[ 0:-2 ]  # Extracting the options (from index 1 to second last element)
            correct_index = question_data[ -2 ]  # Last but one element is the correct index
            difficulty = question_data[ -1 ]  # Last element is the difficulty level

            question_label = tk.Label( self.question_frame, text = question_text, font = ("Arial", 14), wraplength = 400 )
            question_label.pack( pady = 10 )

            for i, option_text in enumerate( options ):
                option_button = tk.Button( self.question_frame, text = option_text, font = ("Arial", 12), bg = "white", fg = "black",
                                           command = lambda i = i: self.check_answer( i ) )
                option_button.pack( pady = 5 )

        def display_fill_in_the_blank( self ):
            self.clear_question_frame( )

            question_data = self.questions[ self.question_type ][ self.current_question ]
            question_text = self.current_question
            correct_answer = question_data[ 0 ]
            difficulty = question_data[ 2 ]
            question_label = tk.Label( self.question_frame, text = question_text, font = ("Arial", 14), wraplength = 400 )
            question_label.pack( pady = 10 )

            answer_entry = tk.Entry( self.question_frame, font = ("Arial", 12) )
            answer_entry.pack( pady = 10 )

            submit_button = tk.Button( self.question_frame, text = "Submit", font = ("Arial", 12), bg = "white", fg = "black",
                                       command = lambda: self.check_fill_in_the_blank( answer_entry.get( ), correct_answer ) )
            submit_button.pack( pady = 5 )

        def display_rank_in_order( self ):
            self.clear_question_frame( )

            question_data = self.questions[ self.question_type ][ self.current_question ]
            question_text = question_data[ "text" ]
            options = question_data[ "options" ]
            difficulty = question_data[ "difficulty" ]

            question_label = tk.Label( self.question_frame, text = question_text, font = ("Arial", 14), wraplength = 400 )
            question_label.pack( pady = 10 )

            for i, option_text in enumerate( options, start = 1 ):
                option_label = tk.Label( self.question_frame, text = f"{i}. {option_text}", font = ("Arial", 12), wraplength = 400 )
                option_label.pack( pady = 5 )

            option_entries = [ tk.Entry( self.question_frame, font = ("Arial", 12) ) for _ in range( len( options ) ) ]
            for entry in option_entries:
                entry.pack( pady = 5 )

            submit_button = tk.Button( self.question_frame, text = "Submit", font = ("Arial", 12), bg = "white", fg = "black",
                                       command = lambda: self.check_rank_order_answer( option_entries, question_data[ "correct_order" ] ) )
            submit_button.pack( pady = 10 )

        def check_answer( self, option_index ):
            question_data = self.questions[ self.question_type ][ self.current_question ]
            correct_index = question_data[ -2 ]  # Last but one element is the correct index
            difficulty = question_data[ -1 ]  # Last element is the difficulty level

            is_correct = option_index == correct_index
            points_earned = 0

            if is_correct:
                points_earned = self.get_points_for_difficulty( difficulty )
                result_message = f"Correct! You earned {points_earned} points."
            else:
                correct_answer = question_data[ correct_index ]
                result_message = f"Incorrect. The correct answer is: {correct_answer}"

            result_label = tk.Label( self.question_frame, text = result_message, font = ("Arial", 14), bg = "light gray",
                                     fg = "green" if is_correct else "red" )
            result_label.pack( pady = 10 )

            next_button = tk.Button( self.question_frame, text = "Next", font = ("Arial", 12), bg = "white", fg = "black",
                                     command = self.display_next_question )
            next_button.pack( pady = 10 )

            self.answered_questions.add( self.current_question )  # Add the question text to answered set

        def check_fill_in_the_blank( self, user_answer, correct_answer ):
            user_answer = user_answer.strip( ).lower( )
            correct_answer = correct_answer.lower( )
            is_correct = user_answer == correct_answer

            result_label = tk.Label( self.question_frame, text = "Correct!" if is_correct else "Incorrect", font = ("Arial", 14), bg = "light gray",
                                     fg = "green" if is_correct else "red" )
            result_label.pack( pady = 10 )

            next_button = tk.Button( self.question_frame, text = "Next", font = ("Arial", 12), bg = "white", fg = "black",
                                     command = self.display_next_question )
            next_button.pack( pady = 10 )

        def check_rank_order_answer( self, entries, correct_order ):
            user_order = [ entry.get( ) for entry in entries ]
            is_correct = user_order == correct_order

            result_label = tk.Label( self.question_frame, text = "Correct!" if is_correct else "Incorrect", font = ("Arial", 14), bg = "light gray",
                                     fg = "green" if is_correct else "red" )
            result_label.pack( pady = 10 )

            next_button = tk.Button( self.question_frame, text = "Next", font = ("Arial", 12), bg = "white", fg = "black",
                                     command = self.display_next_question )
            next_button.pack( pady = 10 )

        def get_points_for_difficulty( self, difficulty ):
            if difficulty == 1:
                return 1
            elif difficulty == 2:
                return 2
            elif difficulty == 3:
                return 3
            else:
                return 0

        def show_result( self ):
            result_window = tk.Toplevel( self )
            result_window.title( "Quiz Result" )
            result_window.geometry( "400x200" )
            result_window.configure( bg = "light gray" )

            total_questions = sum( len( self.questions[ q_type ] ) for q_type in self.questions )
            correct_answers = len( self.answered_questions )
            percentage = (correct_answers / total_questions) * 100
            grade = self.calculate_grade( percentage )
            total_points_earned = sum(
                    self.get_points_for_difficulty( self.questions[ question_type ][ question ][ -1 ] ) for
                    question_type in self.questions for question in self.questions[ question_type ] if question in self.answered_questions )

            result_label = tk.Label( result_window,
                                     text = f"Score: {correct_answers}/{total_questions}\nPercentage: {percentage:.2f}%\nGrade: {grade}\nTotal Points Earned: {total_points_earned}",
                                     font = ("Arial", 16), bg = "light gray" )
            result_label.pack( pady = 20 )

        def calculate_grade( self, percentage ):
            if percentage == 100:
                return "S"
            elif percentage >= 90:
                return "A"
            else:
                return "F"

        def clear_question_frame( self ):
            for widget in self.question_frame.winfo_children( ):
                widget.destroy( )

    if __name__ == "__main__":
        app = PyQuiz( )
        app.mainloop( )

    def check_answer( self, option_index ):
        question_data = self.questions[ self.question_type ][ self.current_question ]
        correct_index = question_data[ -2 ]  # Last but one element is the correct index
        difficulty = question_data[ -1 ]  # Last element is the difficulty level

        is_correct = option_index == correct_index
        points_earned = 0

        if is_correct:
            points_earned = self.get_points_for_difficulty( difficulty )
            result_message = f"Correct! You earned {points_earned} points."
        else:
            correct_index = self.questions[self.question_type][self.current_question][-2]
            result_message = f"Incorrect. The correct answer is: {question_data[correct_index]}"

        result_label = tk.Label( self.question_frame, text = result_message, font = ("Arial", 14), bg = "light gray",
                                 fg = "green" if is_correct else "red" )
        result_label.pack( pady = 10 )

        next_button = tk.Button( self.question_frame, text = "Next", font = ("Arial", 12), bg = "white", fg = "black",
                                 command = self.display_next_question )
        next_button.pack( pady = 10 )

        self.answered_questions.add( self.current_question )  # Add the question to answered set

    def check_fill_in_the_blank(self, user_answer, correct_answer):
        user_answer = user_answer.strip().lower()
        correct_answer = correct_answer.lower()
        is_correct = user_answer == correct_answer

        result_label = tk.Label(self.question_frame, text="Correct!" if is_correct else "Incorrect", font=("Arial", 14), bg="light gray", fg="green" if is_correct else "red")
        result_label.pack(pady=10)

        next_button = tk.Button(self.question_frame, text="Next", font=("Arial", 12), bg="white", fg="black", command=self.display_next_question)
        next_button.pack(pady=10)

    def check_rank_order_answer(self, entries, correct_order):
        user_order = [entry.get() for entry in entries]
        is_correct = user_order == correct_order

        result_label = tk.Label(self.question_frame, text="Correct!" if is_correct else "Incorrect", font=("Arial", 14), bg="light gray", fg="green" if is_correct else "red")
        result_label.pack(pady=10)

        next_button = tk.Button(self.question_frame, text="Next", font=("Arial", 12), bg="white", fg="black", command=self.display_next_question)
        next_button.pack(pady=10)

    def get_points_for_difficulty(self, difficulty):
        if difficulty == 1:
            return 1
        elif difficulty == 2:
            return 2
        elif difficulty == 3:
            return 3
        else:
            return 0

    def show_result(self):
        result_window = tk.Toplevel(self)
        result_window.title("Quiz Result")
        result_window.geometry("400x200")
        result_window.configure(bg="light gray")

        total_questions = sum(len(self.questions[q_type]) for q_type in self.questions)
        correct_answers = len(self.answered_questions)
        percentage = (correct_answers / total_questions) * 100
        grade = self.calculate_grade(percentage)
        total_points_earned = sum(
                self.get_points_for_difficulty(self.questions[question_type][question][-1]) for
                question_type in self.questions for question in self.questions[question_type] if question in self.answered_questions)

        result_label = tk.Label(result_window,
                                 text=f"Score: {correct_answers}/{total_questions}\nPercentage: {percentage:.2f}%\nGrade: {grade}\nTotal Points Earned: {total_points_earned}",
                                 font=("Arial", 16), bg="light gray")
        result_label.pack(pady=20)

    def calculate_grade(self, percentage):
        if percentage >= 100:
            return "S"
        elif percentage >= 95:
            return "A"
        else:
            return "F"

    def clear_question_frame(self):
        for widget in self.question_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = PyQuiz()
    app.mainloop()
