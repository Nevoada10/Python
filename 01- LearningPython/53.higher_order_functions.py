# Higher order function is a function that:
# Either accepts functions as an argument
# or
# Returns a function

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def define_and_modify_text(func):
    text = func("Hello")    # Hello upper or Hello lowercase.
    print(text)


define_and_modify_text(loud)
define_and_modify_text(quiet)

# Nested functions
def divisor(x):
    def dividend(y):
        return y/x  # Dividend result = y/x
    return dividend

divide = divisor(2)
print(divide(10))