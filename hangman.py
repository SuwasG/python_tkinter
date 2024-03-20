import tkinter as tk 
import random 

class HangmanGame:
    def __init__(self, master) :
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("900x650")
        self.master.configure(bg='dodgerblue')
        self.word_list=['python', 'javascript', 'html', 'css', 'react']
        self.secret_word=self.choose_secret_word()
        self.correct_guess= set()
        self.incorrect_guess= set()
        self.attempt_left=7
        self.initialize_gui()

    def initialize_gui(self):
        btn_bg='orange'
        btn_fg='white'
        btn_font=('Helvetica', 12, 'bold')
        self.hangman_canvas=tk.Canvas(self.master, width=300, height=300, bg='green')
        self.hangman_canvas.pack(padx=20, pady=10)
        self.word_display=tk.Label(self.master, text='_'*len(self.secret_word), font=('Helvetica', 30, 'bold'), bg='light green')
        self.word_display.pack(pady=20, padx=40)
        self.reset_btn=tk.Button(self.master,text='RESET', command=self.reset_game, height=3, width=20, bg=btn_bg, fg=btn_fg, font=btn_font)
        self.reset_btn.pack(pady=10)
        self.btn_frame=tk.Frame(self.master)
        self.btn_frame.pack(pady=20)
        self.setup_alphabet_buttons()
    
    def setup_alphabet_buttons(self):
        btn_bg='orange'
        btn_fg='white'
        btn_font=('Helvetica', 12, 'bold')
        alphabet="abcdefghijklmnopqrstuvwxyz"
        upper_row=alphabet[:13]
        lower_row=alphabet[13:]
        upper_frame=tk.Frame(self.btn_frame)
        upper_frame.pack()
        lower_frame=tk.Frame(self.btn_frame)
        lower_frame.pack()

        for letter in upper_row:
            btn=tk.Button(upper_frame, text=letter, command=lambda l =letter:self.guess_letter(l), bg=btn_bg, fg=btn_fg, font=btn_font, width=4, height=2)
            btn.pack(side='left', padx=2, pady=3)

        for letter in lower_row:
            btn=tk.Button(lower_frame, text=letter, command=lambda l =letter:self.guess_letter(l), bg=btn_bg, fg=btn_fg, font=btn_font, width=4, height=2)
            btn.pack(side='left', padx=2, pady=3)
        
    def choose_secret_word(self):
        return random.choice(self.word_list)
    
    def update_hangman_canvas(self):
        self.hangman_canvas.delete('all')
        stages=[self.draw_head, self.draw_body, self.draw_left_arm, self.draw_right_arm,self.draw_left_leg, self.draw_right_leg, self.draw_face]

        for i in range(len(self.incorrect_guess)):
            if i<len(stages):
                stages[i]()
                # draw_head()
    def draw_head(self):
        self.hangman_canvas.create_oval(125, 50, 185, 110, outline='black')

    def draw_body(self):
        self.hangman_canvas.create_line(155,110, 155, 170, fill='black')
    
    def draw_left_arm(self):
        self.hangman_canvas.create_line(155, 130, 125, 150, fill='black')

    def draw_right_arm(self):
        self.hangman_canvas.create_line(155, 130,185, 150, fill='black' )

    def draw_left_leg(self):
        self.hangman_canvas.create_line(155,170, 125, 200, fill='black')

    def draw_right_leg(self):
        self.hangman_canvas.create_line(155, 170, 185, 200, fill='black')

    def draw_face(self):
        self.hangman_canvas.create_line(140, 70, 150,80, fill='black'  )
        self.hangman_canvas.create_line(160, 70, 170, 80, fill='black')
        self.hangman_canvas.create_arc(140, 85,70, 105, start=0, extent=180, fill='black')

def main():
    root = tk.Tk()
    game=HangmanGame(root)
    root.mainloop()
if __name__=='__main__':
    main()

