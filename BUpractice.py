def HoursToMinutes(x):
    x = x * 60
    return x

def hTOt_OR_tTOh(x, y):
    if x == 'h':
        y = y * 60
    elif x == 'm':
        y = y / 60
    else:
        return 'Please type h or m.'
    return y

print(HoursToMinutes(3))
print(hTOt_OR_tTOh('m', 120))

class person:
    apple = 1
    def _init_(self, name, age):
        self.name = name
        self.age = age

def myfunc(self):
    print("Hi my name is " + self.name)

p1 = person("Jphn", 36)
p1.myfunc() 
