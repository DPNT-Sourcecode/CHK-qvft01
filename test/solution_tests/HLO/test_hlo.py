from solutions.HLO import hello_solution

def test_hello_message_prints_correctly():
    assert hello_solution.hello() == "hello to the world"

def test_parameter_not_required():
    assert hello_solution.hello('This is not used') == "hello to the world"