class Calcu:
    def __init__(self, a, b):
        self.fnum = a
        self.snum = b
    def plus(self):
        result = self.fnum + self.snum
        return result
    
    def minus(self):
        result = self.fnum - self.snum
        return result
    
    def mult(self):
        result = self.fnum * self.snum
        return result
    
    def division(self):
        result = self.fnum / self.snum
        return result
    
    def c_division(self):
        result = self.fnum // self.snum
        residual = self.fnum % self.snum
        return result, residual

    def p(self):
        result = self.fnum ** self.snum
        return result
            

def check_opration(ope, obj_n):
    if ope == "+": return Calcu.plus(obj_n)
    if ope == "-": return Calcu.minus(obj_n)
    if ope == "*": return Calcu.mult(obj_n)
    if ope == "/": return Calcu.division(obj_n)
    if ope == "//": return Calcu.c_division(obj_n)
    if ope == "**": return Calcu.p(obj_n)






if __name__ == "__main__":
    status = True
    while status:
        try:
            txt = "formul (example -> 2 * 5 | q q q -> Exit):"
            a, b, c = input(txt).split()
            if a == 'q' and b == 'q' and c == 'q':
                break
            a = int(a)
            c = int(c)
            answer = Calcu(a, c)
            result = check_opration(b, answer)

            print("The answer is %s" % str(result))

        except TypeError:
            print("\nPleas enter a correct data for example 1 * 2 or q q q (\"for exit\") or 9 + 6\n")
        except ValueError:
            print("\nPleas enter a correct Value for example 1 * 2 or q q q (\"for exit\") or 9 + 6\n")
        except ZeroDivisionError:
            print("don't type 0")
        finally:
            print("\nDebugging was successful\n")

