from tkinter import *
import tkinter as tk
import random
class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg = 'light grey')
        self.option_add('*Background', 'light grey')
        self.option_add('*Foreground', 'black')
class UserWindow(Windows):
    def __init__(self):
        super().__init__()
        self.QuestionsLeft = 20
        self.question_number = -1
        self.possible_question_number = -1
        self.chosen_question_numbers = []
        self.OwnWorkLabel = None
        self.OwnWorkYes = None
        self.OwnWorkNo = None
        self.multiple_choice_questions_left = 10
        self.multiple_choice_frame = tk.Frame(padx = 100, pady = 30)
        self.user_answer = 0
        self.question_number = int(9)
        self.fill_in_the_blank_question_list = list(Fill_In_Blank_Question_Dictionary.keys())
        random.shuffle(self.fill_in_the_blank_question_list)
        self.rank_in_order_question_list = list(Rank_In_Order_Question_Dictionary.keys())
        random.shuffle(self.rank_in_order_question_list)
        self.state('zoomed')
        self.QuestionsLeftLabel = tk.Label(text = "Questions Left: " + str( self.QuestionsLeft ), font = ('arial', 18, 'bold') )
        self.QuestionsLeftLabel.pack( anchor = 'ne' )
        self.own_work( )
    def own_work( self ):
        self.OwnWorkFrame = tk.Frame( )
        self.OwnWorkFrame.pack( side = 'top' )
        self.OwnWorkLabel = tk.Label( self.OwnWorkFrame, text = "Is this all your own work?", font = ('arial', 20, 'bold'), pady = 20 )
        self.OwnWorkLabel.pack( side = 'top' )
        self.OwnWorkYes = tk.Button( self.OwnWorkFrame, text = "YES", font = ('arial', 20, 'bold'), command = self.clear_own_work, anchor = 'n',
                                     padx = 40 )
        self.OwnWorkYes.pack( side = 'left' )
        self.OwnWorkNo = tk.Button( self.OwnWorkFrame, text = "NO", font = ('arial', 20, 'bold'), command = self.destroy, anchor = 'n', padx = 40 )
        self.OwnWorkNo.pack( side = 'right' )
    def clear_own_work( self ):
        self.OwnWorkFrame.destroy( )
        self.OwnWorkLabel.destroy( )
        self.OwnWorkYes.destroy( )
        self.OwnWorkNo.destroy( )
        self.multiple_choice_questions( )
    def get_question_number( self ):
        while self.question_number == -1:
            self.question_number = random.randint( 0, 9 )
            if self.question_number not in self.chosen_question_numbers:
                self.chosen_question_numbers.append( self.question_number )
            elif len( self.chosen_question_numbers ) == 10:  # All possible numbers have been exhausted
                self.question_number = -2
                self.fill_in_the_blank_questions( )
            else:
                self.question_number = -1
    def multiple_choice_questions( self ):
        self.answered = False
        self.user_answer = 0
        self.get_question_number( )
        if len( self.chosen_question_numbers ) != 10:
            question = multiple_choice_questions_list[ self.question_number ]
            self.answer = Multiple_Choice_Question_Dictionary[ question ]
            self.answer_key = question.split( ';' )
            self.multiple_choice_frame = tk.Frame( )
            self.multiple_choice_frame.pack( side = 'top' )
            self.Multiple_choice_question = tk.Label( self.multiple_choice_frame, text = self.answer_key[ 0 ] )
            self.Multiple_choice_question.pack( side = 'top' )
            self.Multiple_choice_answer_1 = tk.Button( self.multiple_choice_frame, text = self.answer_key[ 1 ],
                                                       command = self.multiple_choice_answer_1 )
            self.Multiple_choice_answer_1.pack( side = 'left' )
            self.Multiple_choice_answer_2 = tk.Button( self.multiple_choice_frame, text = self.answer_key[ 2 ],
                                                       command = self.multiple_choice_answer_2 )
            self.Multiple_choice_answer_2.pack( side = 'left' )
            self.Multiple_choice_answer_3 = tk.Button( self.multiple_choice_frame, text = self.answer_key[ 3 ],
                                                       command = self.multiple_choice_answer_3 )
            self.Multiple_choice_answer_3.pack( side = 'left' )
            self.Multiple_choice_answer_4 = tk.Button( self.multiple_choice_frame, text = self.answer_key[ 4 ],
                                                       command = self.multiple_choice_answer_4 )
            self.Multiple_choice_answer_4.pack( side = 'left' )
        else:
            self.fill_in_the_blank_questions( )
    def multiple_choice_answer_1( self ):
        self.user_answer = 1
        self.check_answer( )
    def multiple_choice_answer_2( self ):
        self.user_answer = 2
        self.check_answer( )
    def multiple_choice_answer_3( self ):
        self.user_answer = 3
        self.check_answer( )
    def multiple_choice_answer_4( self ):
        self.user_answer = 4
        self.check_answer( )
    def check_answer( self ):
        if self.answered is False:
            self.answered = True
            self.NextQuestionButton = tk.Button( text = "Next Question", pady = 40, padx = 80, anchor = NE, command = self.next_question )
            self.NextQuestionButton.pack( )
            self.incorrect = tk.Label( text = "That's Incorrect The Answer Is " + self.answer_key[ self.answer ] )
            self.correct = tk.Label( text = "That's Correct" )
            if str( self.user_answer ) == str( self.answer ):
                self.correct.pack( side = 'top' )
            else:
                self.incorrect.pack( side = 'top' )
    def next_question( self ):
        self.multiple_choice_frame.pack_forget( )
        self.Multiple_choice_question.destroy( )
        self.Multiple_choice_answer_1.destroy( )
        self.Multiple_choice_answer_2.destroy( )
        self.Multiple_choice_answer_3.destroy( )
        self.Multiple_choice_answer_4.destroy( )
        self.NextQuestionButton.pack_forget( )
        self.incorrect.pack_forget( )
        self.correct.pack_forget( )
        self.question_number = -1
        self.QuestionsLeft -= 1
        self.QuestionsLeftLabel.destroy( )
        self.QuestionsLeftLabel = tk.Label( text = "Questions Left: " + str( self.QuestionsLeft ), font = ('arial', 18, 'bold') )
        self.QuestionsLeftLabel.pack( anchor = 'ne' )
        self.multiple_choice_questions( )
    def fill_in_the_blank_questions(self):
        if self.QuestionsLeft == 5:
            self.Rank_In_Order_Questions()
        else:
            self.user_answer_tk = tk.StringVar()
            print(self.fill_in_the_blank_question_list)
            print(self.QuestionsLeft)
            self.question = self.fill_in_the_blank_question_list[ self.QuestionsLeft - 6 ]
            self.answer_key = self.question.split( ';' )
            self.Fill_In_Blank_Label_1 = tk.Label( text = self.answer_key[ 0 ] )
            self.Fill_In_Blank_Label_1.pack( )
            self.Fill_In_Blank_Fill = tk.Entry( textvariable = self.user_answer_tk )
            self.Fill_In_Blank_Fill.pack( )
            self.Fill_In_Blank_Label_2 = tk.Label( text = self.answer_key[ 1 ] )
            self.Fill_In_Blank_Label_2.pack( )
            self.Fill_In_Blank_Submit = tk.Button( text = "Submit Answer", command = self.fill_in_blank_submit )
            self.Fill_In_Blank_Submit.pack( )

    def fill_in_blank_submit( self ):
            self.answer = Fill_In_Blank_Question_Dictionary[ self.question ]
            is_correct = self.user_answer_tk.get( ).lower( ) == self.answer.lower( )

            feedback_text = "That's Correct" if is_correct else "That's Incorrect the Answer Is " + self.answer
            feedback_label = tk.Label( text = feedback_text )
            feedback_label.pack( )

            self.next_question_button = tk.Button( text = "Next Question", command = self.Fill_Next_Question).pack()

            self.Fill_In_Blank_Submit.destroy( )
    def Fill_Next_Question(self):
        self.next_question_button.destroy()
        self.Fill_In_Blank_Label_1.destroy()
        self.Fill_In_Blank_Label_2.destroy()
        self.Fill_In_Blank_Fill.destroy()
        self.QuestionsLeft -= 1
        self.QuestionsLeftLabel.destroy()
        self.QuestionsLeftLabel = tk.Label(text = "Questions Left: " + str( self.QuestionsLeft ), font = ('arial', 18, 'bold'))
        self.QuestionsLeftLabel.pack(anchor = 'ne')
        self.correct.destroy()
        self.incorrect.destroy()
        self.fill_in_the_blank_questions( )
    def show(self):
        self.Rank_In_Order_Answer_1_Label( text = self.clicked.get( ) )
    def Rank_In_Order_Questions( self ):
        if self.QuestionsLeft == 0:
            print( 'Quiz completed!' )
            return
        self.rank_order_frame = tk.Frame( )
        self.rank_order_frame.pack( side = 'top' )
        self.rank_order_question = self.rank_in_order_question_list[ self.QuestionsLeft - 1 ]
        self.rank_order_options = self.rank_order_question.split( ';' )[ 1: ]
        random.shuffle( self.rank_order_options )
        self.rank_order_label = tk.Label( self.rank_order_frame, text = self.rank_order_question.split( ';' )[ 0 ] )
        self.rank_order_label.pack( side = 'top' )
        self.rank_order_entries = [ ]
        for i in range( len( self.rank_order_options ) ):
            entry = tk.Entry( self.rank_order_frame )
            entry.pack( side = 'left' )
            self.rank_order_entries.append( entry )
        self.rank_order_submit = tk.Button( self.rank_order_frame, text = 'Submit', command = self.check_rank_order_answer )
        self.rank_order_submit.pack( side = 'bottom' )
    def check_rank_order_answer( self ):
        user_answers = [ entry.get( ) for entry in self.rank_order_entries ]
        correct_order = Rank_In_Order_Question_Dictionary[ self.rank_order_question ]
        if user_answers == correct_order:
            result_label = tk.Label( self.rank_order_frame, text = 'Correct!', fg = 'green' )
        else:
            result_label = tk.Label( self.rank_order_frame, text = 'Incorrect!', fg = 'red' )
        result_label.pack( side = 'top' )
        next_button = tk.Button( self.rank_order_frame, text = 'Next Question', command = self.next_rank_order_question )
        next_button.pack( side = 'bottom' )
    def next_rank_order_question( self ):
        self.rank_order_frame.destroy( )
        self.QuestionsLeft -= 1
        self.QuestionsLeftLabel.destroy( )
        self.QuestionsLeftLabel = tk.Label( text = "Questions Left: " + str( self.QuestionsLeft ), font = ('arial', 18, 'bold') )
        self.QuestionsLeftLabel.pack( anchor = 'ne' )
        self.Rank_In_Order_Questions( )
if __name__ == '__main__':
    Multiple_Choice_Question_Dictionary = {
            "What colour is the sky;Blue;Purple;Green;Pink":                     1,
            "What color is grass;Green;Blue;Pink;Purple":                        1,
            "is grass green;Chlorophyll;1;2;3;4":                                1,
            "14144;1;2;3;4":                                                     4,
            "1114414;1;2;3;4":                                                   1,
            "1145414;1;2;3;4":                                                   1,
            "1149414;1;2;3;4":                                                   1,
            "1164414;1;2;3;4":                                                   1,
            "11441994;1;2;3;4":                                                  1,
            "114999414;1;2;3;4":                                                 1,
            "1144999914;1;2;3;4":                                                1
    }
    Fill_In_Blank_Question_Dictionary = {
            "Fill in the ; with the answer1": "blank",
            "Fill in the ; with the answer2": "blank",
            "Fill in the ; with the answer3": "blank",
            "Fill in the ; with the answer4": "blank",
            "Fill in the ; with the answer5": "blank"}
    Rank_In_Order_Question_Dictionary = {
            "Highest to lowest number;1;2;3;4": "4321",
            "1Highest to lowest number;1;2;3;4": "4321",
            "2Highest to lowest number;1;2;3;4": "4321",
            "3Highest to lowest number;1;2;3;4": "4321",
            "4Highest to lowest number;1;2;3;4": "4321"
    }
    multiple_choice_questions_list = list(Multiple_Choice_Question_Dictionary.keys())
    UserWindow().mainloop()