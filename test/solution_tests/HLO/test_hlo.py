from lib.solutions.HLO.hello_solution import hello
from solutions.HLO import hello_solution

def test_hello_message_prints_correctly():
    assert hello_solution.hello() == "Hello, World!"

def test_hello_message_without_name():
    assert hello_solution.hello() == "Hello, World!"

def test_hello_with_friend_name():
    friend_name = "Alex"
    assert hello_solution.hello(friend_name) == 'Hello, Alex!'

    friend_name = "John"
    assert hello_solution.hello(friend_name) == 'Hello, John!'