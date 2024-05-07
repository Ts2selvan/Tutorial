#Private Class Variables

class Tamil:
    __esh="esh loves tamil"
    def __init__(self):
        Tamil.__esh="esh loves tamil So much"

    @staticmethod
    def get_lovests():
        return Tamil.__esh


print(Tamil.get_lovests())

tam=Tamil()
print(tam.get_lovests())
