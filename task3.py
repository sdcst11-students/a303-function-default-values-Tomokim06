#!python3

"""
Create a function called title that creates a single line of output to display the word
"Title" with a box around it.  
The function will have 1 optional input:
symbol : string.  The symbolt to use as the border. Default symbol is "="

The return value is the output string with escaped line breaks.

example assertion:
assert title("*") == "*********\n* Title *\n*********"
assert title() == "=========\n= Title =\n========="
(2 points)

"""
def title(sym = "="):
    
    bt = sym*9
    x = (f"{bt}\n{sym} Title {sym}\n{bt}")
    return x

if __name__ == "__main__":
    assert title("*") == "*********\n* Title *\n*********"
    assert title() == "=========\n= Title =\n========="