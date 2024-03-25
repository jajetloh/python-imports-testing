from mycode.shared_one import shared_fn_one

def shared_fn_three():
    print("shared_fn_three()")

if __name__ == "__main__":
    shared_fn_three()
    shared_fn_one()