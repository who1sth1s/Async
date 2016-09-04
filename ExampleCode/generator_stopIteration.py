def sendme():
    while 1:
        something = yield
        if something is None:
            raise StopIteration()
        print(something)

gen = sendme()
next(gen)
gen.send('a')  # return : a
gen.send('b')  # return : b
gen.send(None)  # return : exception StopIteration
