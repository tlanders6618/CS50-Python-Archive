class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity;
        self.size=0;

    @property #property means getter
    def capacity(self):
        return self._capacity;

    @capacity.setter
    def capacity(self, num):
        if (num>=0):
            self._capacity=num;
        else:
            raise ValueError("Jar's capacity cannot be negative.");

    @property #property means getter
    def size(self):
        return self._size;

    @size.setter
    def size(self, num):
        if (num>=0):
            self._size=num;
        else:
            raise ValueError("Jar's size cannot be negative.");

    def deposit(self, cookies):
        if (cookies<0 or self.size+cookies>self.capacity):
            raise ValueError("Not enough space in this jar for that many cookies.");
        else:
            self.size+=cookies;

    def withdraw(self, cookies):
        if (cookies<0 or self.size-cookies<0):
            raise ValueError("Not enough cookies in this jar for that many space.");
        else:
            print("Nom nom"); self.size-=cookies;

    def __str__(self):
        list="";
        for _ in range(self.size):
            list+="🍪";
        return list;
