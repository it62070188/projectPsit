"""test manu"""
import webbrowser
import random
def find(must):
    ans = must[random.randint(0,2)]
    return ans

def main():
    """find body"""
    tall = float(input("Tall..."))
    weight = float(input("weight..."))
    lis1 = ["nudle", "strong", "small"]
    lis2 = ["snoppy", "jelly", "firsh"]
    lis3 = ["1111", "22222", "33333"]
    lis4 = ["987654", "8765", "23456"]
    body = weight / (tall/100)**2
    if body <= 20:
        print("Don't good")
        url(str("Don't good"))
    elif 20 < body <= 22:
        print(find(lis1))
        url(str(find(lis1)))
    elif 22 < body <= 24:
        print(find(lis2))
        url(str(find(lis2)))
    elif 24 < body <= 26:
        print(find(lis3))
        url(str(find(lis3)))
    elif 26 < body <= 28:
        print(find(lis4))
        url(str(find(lis4)))
    else:
        print("Fat")
    def url(para):
        """call url"""
        webbrowser.open("https://projectpsit2019.web.app/lunch.html"+"nember="para)
main()
