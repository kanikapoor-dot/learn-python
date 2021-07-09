def loggers(func):
    def word():
        print("h=started")
        func()
        print("end...")
    return word

@loggers
def scap():
    print("hello")

scap()