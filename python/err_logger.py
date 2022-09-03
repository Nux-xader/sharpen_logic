import traceback, sys
from datetime import datetime


# Decorator model
def write_log(func):
    def inner():
        try:
            return func()
        except:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            print(f"\n[{datetime.now()}]\n"+str(
                "\n".join(
                    tuple(
                        f"File {trace[0]}, Line {trace[1]}, in {trace[2]}\n{trace[3]}" for trace in traceback.extract_tb(ex_traceback)
                    )
                )+f"\n{ex_type.__name__}: {ex_value}\n{50*'_'}")
           )
    return inner


@write_log
def test1():
    print(1/0)
test1()



# anonymouse function model
def write_log(func):
    try:
        return func()
    except:
        ex_type, ex_value, ex_traceback = sys.exc_info()
        print(f"\n[{datetime.now()}]\n"+str(
            "\n".join(
                tuple(
                    f"File {trace[0]}, Line {trace[1]}, in {trace[2]}\n{trace[3]}" for trace in traceback.extract_tb(ex_traceback)
                )
            )+f"\n{ex_type.__name__}: {ex_value}\n{50*'_'}")
       )
def test2():
    print(1/0)
write_log(test2)


# basic model
def write_log():
    ex_type, ex_value, ex_traceback = sys.exc_info()
    print(f"\n[{datetime.now()}]\n"+str(
        "\n".join(
            tuple(
                f"File {trace[0]}, Line {trace[1]}, in {trace[2]}\n{trace[3]}" for trace in traceback.extract_tb(ex_traceback)
            )
        )+f"\n{ex_type.__name__}: {ex_value}\n{50*'_'}")
   )


def test3():
    try: print(1/0)
    except: write_log()
test3()

