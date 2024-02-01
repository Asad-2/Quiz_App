import tkinter as tk   # tkinter is a Python library used for creating graphical user interfaces (GUIs).
from functools import partial

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option
        self.user_answer = None

class TreeNode:
    def __init__(self, question=None, left=None, right=None):
        self.question = question
        self.left = left
        self.right = right

class Topic:
    def __init__(self, name, root_node, questions):
        self.name = name
        self.root_node = root_node
        self.questions = questions

class QuizApp:
    def __init__(self):
        self.topics = self.initialize_question_bank()
        self.user_answers = []

    def initialize_question_bank(self):
        programming_fundamentals_questions = [
            Question("What is a variable?", ["A container for data", "A function", "A loop", "A class"], 0),
            Question("What is the result of 5 + 3?", ["6", "7", "8", "9"], 2),
            Question("Which of the following is NOT a programming language?" , ["C++" , "Java" ,"Lotus" , "python"],2),
            Question("Which of the following programming languages is used to write queries in database applications?",["python" , "Java" ,"SQL" , "Fortan"],2),
            Question("Which of the following is NOT a type of algorithm?",["Program" , "Flowchart" , "Decision Table" , "Pseudocode"],0) ,
            Question("What is the output of the following code snippet? \n\nx = 10\ny = 5\nif x > 10:\n    print('x is greater than 10')\nelif x == 10:\n    print('x is equal to 10')\nelse:\n    print('x is less than 10')", ["x is greater than 10", "x is equal to 10", "x is less than 10", "SyntaxError"], 1),
            Question("What will be the value of arr[3] after executing the following code snippet? \n\narr = [1, 2, 3, 4, 5]\narr[3] = arr[3] * 2\nprint(arr[3])", ["3", "4", "6", "8"], 3),
            Question("Which of the following is a correct syntax for a 'for' loop in Python?", ["for i = 0; i < 5; i++:", "for i in range(5):", "for (int i = 0; i < 5; i++):", "for (i = 0; i < 5; i++):"], 1),
            Question("What does the 'continue' statement do in a loop?", ["Exits the loop", "Skips the current iteration and continues with the next iteration", "Stops the program execution", "Returns a value from the loop"], 1),
            Question("Which of the following is NOT a valid comparison operator in Python?", ["==", "!=", "<>", "<="], 2)
        ]

        programming_fundamentals_tree = TreeNode(programming_fundamentals_questions[0])
        current_node = programming_fundamentals_tree
        for question in programming_fundamentals_questions[1:]:
            current_node.right = TreeNode(question)
            current_node = current_node.right

        programming_fundamentals = Topic("Programming Fundamentals", programming_fundamentals_tree, programming_fundamentals_questions)

        oop_questions = [
            Question("What does OOP stand for?", ["Object-Oriented Programming", "Operator Overloading Principle", "Object-Oriented Principles", "Object-Oriented Process"], 0),
            Question("Which is not an OOP principle?", ["Encapsulation", "Inheritance", "Polymorphism", "Recursion"], 3),
            Question("What is the main benefit of inheritance in OOP?", ["Code reuse", "Polymorphism", "Encapsulation", "Abstraction"], 0),
            Question("Which OOP concept allows different classes to have methods with the same name?", ["Inheritance", "Encapsulation", "Polymorphism", "Abstraction"], 2),
            Question("What is the process of bundling data and methods that operate on the data into a single unit called?", ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"], 0),
            Question("What is the term used to describe the ability of an object to take many forms?", ["Encapsulation", "Abstraction", "Polymorphism", "Inheritance"], 2),
            Question("Which of the following is NOT a characteristic of OOP?", ["Encapsulation", "Abstraction", "Modularity", "Iteration"], 3),
            Question("Which OOP principle is violated when a method accesses a private attribute of another object directly?", ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"], 0),
            Question("Which OOP principle allows a class to have more than one method with the same name but different parameters?", ["Inheritance", "Encapsulation", "Polymorphism", "Abstraction"], 2),
            Question("What is the term used to describe the ability of an object to hide its implementation details and only provide a high-level interface?", ["Encapsulation", "Abstraction", "Polymorphism", "Inheritance"], 1)
        ]

        oop_tree = TreeNode(oop_questions[0])
        current_node = oop_tree
        for question in oop_questions[1:]:
            current_node.right = TreeNode(question)
            current_node = current_node.right

        oop = Topic("OOP", oop_tree, oop_questions)

        data_structures_questions = [
            Question("What is a linked list?", ["A linear data structure", "A hierarchical data structure", "A non-linear data structure", "A graph data structure"], 0),
            Question("Which data structure uses the Last In, First Out (LIFO) principle?", ["Queue", "Stack", "Heap", "Tree"], 1),
            Question("What is the time complexity of searching in a binary search tree (BST) in the worst case?", ["O(1)", "O(log n)", "O(n)", "O(n log n)"], 1),
            Question("Which data structure is used to represent a hierarchical relationship between elements?", ["Queue", "Stack", "Tree", "Graph"], 2),
            Question("What is the purpose of a hash table?", ["To store data in a sorted order", "To reduce the complexity of searching", "To store key-value pairs", "To represent hierarchical relationships"], 2),
            Question("Which data structure is best suited for implementing a priority queue?", ["Array", "Stack", "Queue", "Heap"], 3),
            Question("What is the primary advantage of using a linked list over an array?", ["Constant-time random access", "Dynamic size", "Cache locality", "Sequential allocation"], 1),
            Question("What is the time complexity of inserting an element into a heap?", ["O(1)", "O(log n)", "O(n)", "O(n log n)"], 1),
            Question("Which data structure uses the First In, First Out (FIFO) principle?", ["Queue", "Stack", "Heap", "Tree"], 0),
            Question("What is the main drawback of using a stack data structure?", ["Limited size", "Complex implementation", "No random access", "High memory consumption"], 2)
        ]

        data_structures_tree = TreeNode(data_structures_questions[0])
        current_node = data_structures_tree
        for question in data_structures_questions[1:]:
            current_node.right = TreeNode(question)
            current_node = current_node.right

        data_structures = Topic("Data Structures", data_structures_tree, data_structures_questions)

        web_dev_questions = [
            Question("What does HTML stand for?", ["Hyper Text Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "Hyperlinks and Textual Markup Language"], 0),
            Question("Which HTML tag is used to define an unordered list?", ["<ul>", "<ol>", "<li>", "<list>"], 0),
            Question("Which CSS property is used to change the text color of an element?", ["color", "text-color", "font-color", "foreground-color"], 0),
            Question("What is the correct HTML for adding a background color?", ["<body style='background-color:yellow;'>", "<background>yellow</background>", "<bg color='yellow'>", "<body bg='yellow'>"], 0),
            Question("Which attribute is used to provide an image alternative for screen readers?", ["alt", "title", "src", "href"], 0),
            Question("What does CSS stand for?", ["Cascading Style Sheets", "Computer Style Sheets", "Colorful Style Sheets", "Creative Style Sheets"], 0),
            Question("Which HTML tag is used to define a hyperlink?", ["<a>", "<link>", "<ref>", "<url>"], 0),
            Question("What is the correct way to insert a JavaScript into an HTML document?", ["<script src='script.js'>", "<script href='script.js'>", "<javascript src='script.js'>", "<js href='script.js'>"], 0),
            Question("What is the purpose of the CSS 'float' property?", ["To specify how an element should float", "To specify the color of an element", "To specify the font size of an element", "To specify the alignment of an element"], 0),
            Question("Which HTML tag is used to define a table?", ["<table>", "<tab>", "<tr>", "<td>"], 0)
        ]

        web_dev_tree = TreeNode(web_dev_questions[0])
        current_node = web_dev_tree
        for question in web_dev_questions[1:]:
            current_node.right = TreeNode(question)
            current_node = current_node.right

        web_dev = Topic("Web Development", web_dev_tree, web_dev_questions)

        sql_questions = [
            Question("What does SQL stand for?", ["Structured Query Language", "Sequential Query Language", "Structured Question Language", "Sequential Question Language"], 0),
            Question("Which statement is used to insert new data in a SQL database?", ["INSERT INTO", "ADD RECORD", "INSERT", "CREATE"], 0),
            Question("Which SQL clause is used to filter records based on a specified condition?", ["WHERE", "FILTER", "SELECT", "HAVING"], 0),
            Question("What is the primary key in a SQL table?", ["A column that uniquely identifies each row in a table", "A column that stores only numeric values", "A column that allows NULL values", "A column that is indexed"], 0),
            Question("Which SQL keyword is used to retrieve a unique set of records?", ["UNIQUE", "DISTINCT", "DIFFERENT", "SINGULAR"], 1),
            Question("Which SQL statement is used to update existing records in a table?", ["UPDATE", "MODIFY", "CHANGE", "ALTER"], 0),
            Question("What does the SQL command 'DELETE FROM table_name;' do?", ["Deletes all records from the table", "Deletes the table structure", "Deletes the table itself", "Deletes a specific record from the table"], 0),
            Question("Which SQL function is used to return the current date and time?", ["NOW()", "DATE()", "TIME()", "CURRENT()"], 0),
            Question("Which SQL clause is used to group rows that have the same values into summary rows?", ["GROUP BY", "SUMMARIZE", "COLLECT", "AGGREGATE"], 0),
            Question("What is the purpose of the SQL command 'SELECT * FROM table_name;'?", ["Selects all records from the table", "Selects only the first record from the table", "Selects a specific record from the table", "Selects the table structure"], 0)
        ]

        sql_tree = TreeNode(sql_questions[0])
        current_node = sql_tree
        for question in sql_questions[1:]:
            current_node.right = TreeNode(question)
            current_node = current_node.right

        sql = Topic("SQL", sql_tree, sql_questions)

        return [programming_fundamentals, oop, data_structures, web_dev, sql]

    def select_topic(self):
        print("Available Topics:")
        for i, topic in enumerate(self.topics):
            print(f"{i + 1}. {topic.name}")

        selected_topic_index = int(input("Select a topic (1-{}): ".format(len(self.topics)))) - 1

        if 0 <= selected_topic_index < len(self.topics):
            selected_topic = self.topics[selected_topic_index]
            self.ask_questions(selected_topic.root_node, selected_topic)
            self.display_result(selected_topic)
        else:
            print("Invalid topic selection.")

    def ask_questions(self, current_node, selected_topic):
        if current_node is None:
            return

        current_question = current_node.question
        print(current_question.text)
        for i, option in enumerate(current_question.options, start=1):
            print(f"{i}. {option}")

        user_answer = int(input("Enter your choice (1-{}): ".format(len(current_question.options))))

        while user_answer not in range(1, len(current_question.options) + 1):
            print("Invalid input. Please enter a number between 1 and {}.".format(len(current_question.options)))
            user_answer = int(input("Enter your choice (1-{}): ".format(len(current_question.options))))

        current_question.user_answer = user_answer - 1
        self.user_answers.append(current_question.user_answer)

        self.ask_questions(current_node.left, selected_topic)
        self.ask_questions(current_node.right, selected_topic)

    def display_result(self, selected_topic):
        total_marks = sum(1 for user_ans, question in zip(self.user_answers, selected_topic.questions) if user_ans == question.correct_option)
        total_questions = len(selected_topic.questions)
        percentage = (total_marks / total_questions) * 100 if total_questions != 0 else 0

        print("\nQuiz Completed!")
        print(f"Total Marks: {total_marks}/{total_questions}")
        print(f"Percentage: {percentage:.2f}%")

    def get_all_questions(self):
        all_questions = []

        for topic in self.topics:
            self.in_order_traversal(topic.root_node, all_questions)

        return all_questions

    def in_order_traversal(self, current_node, question_list):
        if current_node is not None:
            self.in_order_traversal(current_node.left, question_list)
            question_list.append(current_node.question)
            self.in_order_traversal(current_node.right, question_list)

class QuizAppGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Application")
        self.master.geometry("600x400")
        self.master.configure(bg="#2C3E50")

        self.current_question_index = 0
        self.user_answers = []

        self.topic_label = tk.Label(self.master, text="Select Quiz Topic", font=("Helvetica", 16), bg="#2C3E50", fg="white")
        self.topic_label.pack()

        self.topics = ["Programming Fundamentals", "OOP", "Data Structures", "Web Development", "SQL"]
        self.selected_topic = tk.StringVar()
        self.selected_topic.set(self.topics[0])
        self.topic_menu = tk.OptionMenu(self.master, self.selected_topic, *self.topics)
        self.topic_menu.pack()

        self.start_button = tk.Button(self.master, text="Start Quiz", command=self.start_quiz, font=("Helvetica", 12), bg="#E74C3C", fg="white")
        self.start_button.pack(pady=10)

    def start_quiz(self):
        self.topic_label.pack_forget()
        self.topic_menu.pack_forget()
        self.start_button.pack_forget()

        selected_topic_index = self.topics.index(self.selected_topic.get())
        selected_topic = quiz_app.topics[selected_topic_index]

        self.questions = selected_topic.questions
        self.show_next_question()

    def show_next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]

            question_frame = tk.Frame(self.master, bg="#2C3E50")
            question_frame.pack(pady=20)

            question_label = tk.Label(question_frame, text=question_data.text, font=("Helvetica", 14), bg="#2C3E50", fg="white")
            question_label.pack(pady=10)

            options_frame = tk.Frame(question_frame, bg="#2C3E50")
            options_frame.pack()

            for i, option in enumerate(question_data.options):
                option_button = tk.Button(options_frame, text=option, command=partial(self.record_answer, i), font=("Helvetica", 12), bg="#E74C3C", fg="white")
                option_button.grid(row=0, column=i, padx=10)

            self.current_question_index += 1
        else:
            self.display_result()

    def record_answer(self, selected_option):
        self.user_answers.append(selected_option)
        for widget in self.master.winfo_children():
            widget.destroy()
        self.show_next_question()

    def display_result(self):
        total_marks = sum(1 for user_ans, question in zip(self.user_answers, self.questions) if user_ans == question.correct_option)
        total_questions = len(self.questions)
        percentage = (total_marks / total_questions) * 100 if total_questions != 0 else 0

        result_text = f"Quiz Completed!\nTotal Marks: {total_marks}/{total_questions}\nPercentage: {percentage:.2f}%"
        result_label = tk.Label(self.master, text=result_text, font=("Helvetica", 16), bg="#2C3E50", fg="white")
        result_label.pack(pady=50)

        review_button = tk.Button(self.master, text="Review Answers", command=self.review_answers, font=("Helvetica", 12), bg="#E74C3C", fg="white")
        review_button.pack()

    def review_answers(self):
        review_window = tk.Toplevel(self.master)
        review_window.title("Review Answers")
        review_window.geometry("600x400")
        review_window.configure(bg="#2C3E50")

        scrollbar = tk.Scrollbar(review_window)
        scrollbar.pack(side="right", fill="y")

        review_text = tk.Text(review_window, wrap="word", yscrollcommand=scrollbar.set, bg="#2C3E50", fg="white", font=("Helvetica", 12))
        review_text.pack(fill="both", expand=True)

        for i, question in enumerate(self.questions):
            review_text.insert("end", f"Question {i + 1}: {question.text}\n")
            review_text.insert("end", f"Your Answer: {question.options[self.user_answers[i]]}\n")
            review_text.insert("end", f"Correct Answer: {question.options[question.correct_option]}\n\n")

        scrollbar.config(command=review_text.yview)

    def back_to_main_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.__init__(self.master)

if __name__ == "__main__":
    quiz_app = QuizApp()

    root = tk.Tk()
    app = QuizAppGUI(root)
    root.mainloop()
