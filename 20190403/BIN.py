def get_celebrator(char):
    def print_style(func):
        def inner():
            print(char*15)
            func()
        return inner
    return print_style


# @get_celebrator('=')
# def myprint():
#     print("小白联盟")


@get_celebrator('=')
@get_celebrator('*')
def myprint():
    print("小白联盟")


if __name__ == '__main__':

    myprint()