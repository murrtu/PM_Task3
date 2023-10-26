"""
In this task you need to simulate a self-checkout check.
You can change template code as needed, but all "while" and "if" functions as well as comments are to stay.

Carefully read all instructions.

Correct if..elif..else structure - 1point
Instructions for input in scan variable - 1point
Input for item price with instructions - 1point (0.5 if input w/ no instructions)
Price is converted to float - 1point
The total is calculated - 1point
Answer theoretical questions - 2points
List output - 1point
Formatted output - 2points (1 for just output and 1 for decimals)
"""

# create an empty list named "items"

scan = ""
# theoretical question - explain why and how "while(True)" works
while (True):
    # write instructions for input - write item name to continue with shopping or write STOP to end scanning
    scan = input()

    if (scan == "STOP"): # this case is done, no code to add here

        # theoretical question - explain what "break" does
        break
    elif(scan): # edit the condition in elif to check for blank input

        # theoretical question - explain what "continue" does
        continue

    else: # here we work with item if it has been input

        # ask for item value - convert to float, let's assume that user will input a correct value

        # add item name and price to items list

        # theoretical question - explain what "pass" does
        pass 

# calculate total for all items, use given variable
sum = 0

# calculate total item count, use given variable
item_count = 0

# output all items in orderly manner, with no built in list symbols

# Output item count and total in given format. 
# output:
# X items   Total Y.YY
# for this task you need to use formatted output with f""
# instructions for formatted string to create two numbers after comma can be found in https://docs.python.org/3/tutorial/inputoutput.html in Formatted String Literals section
