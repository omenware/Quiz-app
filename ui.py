from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window =Tk()
        self.window.title('Quizzler app')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.my_label=Label(text='Score=0',bg=THEME_COLOR,fg='white')
        self.my_label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,highlightthickness=0)
        self.question_text=self.canvas.create_text(150,100,width=250,text='Some Question Text',font=('Arial',20,'italic'),fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)

        self.true_image=PhotoImage(file='./images/true.png')
        self.button1=Button(image=self.true_image,highlightthickness=0,command=self.true_answer)
        self.button1.grid(row=2,column=0)

        self.false_image = PhotoImage(file='./images/false.png')
        self.button2 = Button(image=self.false_image,highlightthickness=0,command=self.false_answer)
        self.button2.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.my_label.config(text=f'Score={self.quiz.score}')
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text='You have reached the end of the questions.')
            self.button1.config(state='disabled')
            self.button2.config(state='disabled')


    def true_answer(self):

        self.feedback(self.quiz.check_answer('True'))

    def false_answer(self):
        # is_false=self.quiz.check_answer('False')
        self.feedback(self.quiz.check_answer('False'))

    def feedback(self,is_right):
        if is_right==True:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)








