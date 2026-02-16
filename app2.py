import gradio as gr

# Step 1: Create a class
class Book:
    def __init__(self, title , author,isbn):
        self.title = title 
        self.author = author
        self.isbn =isbn

# Step 2: Function to use the class
def create_book(titl,author,isbn):
    book1 = Book(title, author,isbn)
    return f"title : {book1.title}\n author: {book1.author}\ isbn"

# Step 3: Gradio Interface
app = gr.Interface(
    fn=create_book,
    inputs=[
        gr.Textbox(label="Enter title"),
        gr.Textbox(label="Enter author")
    ],
    outputs=gr.Textbox(label="Bike Details"),
    title="The bike details by Akshay ",
    description="Enter bike name and number to see details using class & object"
)

app.launch()