class Progression:
    def __init__(self, a, d, n):
        self.a = a  # first element
        self.d = d  # difference
        self.n = n  # amount of elements

    def i_element(self, j):
        aj = self.a + (j - 1) * self.d
        return aj

    def summa(self, k):
        if k<=0:
            raise ValueError
        s = (k * (2 * self.a + self.d * (k - 1))) / 2
        return s
        # except TypeError:
        #     return False

    def range_(self, b1, b2):
        list_ = []
        i = 2
        while i <= self.n:
            ai = self.a + (i - 1) * self.d
            list_ = list_ + [ai]
            i += 1
        if len(list_) >= b2:
            return list_[b1-2:b2]
        else:
            while i <= b2:
                ai = self.a + (i - 1) * self.d
                list_ = list_ + [ai]
                i += 1
        return list_[b1-2:b2]

    def check_element(self, x):
        list_ = []
        i = 2
        while i <= self.n:
            ai = self.a + (i - 1) * self.d
            list_ = list_ + [ai]
            i += 1
        if x in list_:
            return True
        else:
            return False

def main():
    progression = Progression(1,3,10) #create progression where first element=1, difference=3,amount of elements=10
    print('The seventh element is ',progression.i_element(7))
    print('Sum of ten elements equal ',progression.summa('k'))
    print('Range between 3rd and 9th position: ',progression.range_(3,9))
    print('Check if it`s "13" in progression:',progression.check_element(13))
    print('Check if it`s "14" in progression:', progression.check_element(14))

if __name__ == '__main__':
    main()

