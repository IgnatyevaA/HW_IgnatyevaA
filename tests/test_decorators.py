from src.decorators import log

def test_log1(capsys):
    @log(filename="mylg.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    output = capsys.readouterr()
    assert output.out == "my_function ok\n"

def test_log2():
    @log(filename="tests/mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    with open("tests/mylog.txt", "r") as file:
        reading = file.read()
        assert reading == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n"

def test_log3(capsys):
    @log(filename="mylg.txt")
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    output = capsys.readouterr()
    assert output.out == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n"
