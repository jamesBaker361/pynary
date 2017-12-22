def test():
    try:
        1/0
    except ZeroDivisionError as err:
        print err
        print type(err)
        for prop in err:
            print prop
        print err.args