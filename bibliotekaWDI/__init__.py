def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nww(a, b):
    return (a * b) // nwd(a, b)


def is_prime(number):
    if number < 4:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(number ** 0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def rebase(number, base):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    if base > 10:
        res = ""
        while number != 0:
            res = str(digits[number % base]) + res
            number //= base
        return res
    else:
        res = 0
        power = 0
        while number != 0:
            res += digits[number % base] * (10 ** power)
            number //= base
            power += 1
        return res


def number_count(number, base, i):
    T = [0] * base
    while number != 0:
        T[number % base] += 1
        number //= base
    return T[i]


def reverse_number(number):
    res = 0
    while number != 0:
        res *= 10
        res += number % 10
        number //= 10
    return res


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        self.head = None

    def add(self, val):
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    def add_list(self, T):
        p = self
        while p.next is not None:
            p = p.next
        for value in T:
            p.next = Node(value)
            p = p.next

    def remove(self, val):
        p = self
        if p.val == val:
            p = Node(p.next.val, p.next.next)
        while p.next.val != val and p.next is not None:
            p = p.next
        if p.next.val == val:
            p.next = p.next.next

    def reverse_list(self):
        p = self

        def reverse_interior(curr, last=None):
            if curr is None:
                return last
            next = curr.next
            curr.next = last
            return reverse_interior(next, curr)

        return reverse_interior(p)

    def is_present(self, val):
        q = self
        while q is not None:
            if q.val == val:
                return True
            q = q.next
        return False

    def print_list(self):
        q = self
        while q is not None:
            print(q.val)
            q = q.next