from flask import Flask, render_template, request
import random
app = Flask(__name__)

body = 0
bodys = ''

@app.route('/')
def main():
    return render_template('first.html')

@app.route('/templates/lunch.html')
def lunch():
    return render_template('lunch.html')

@app.route('/templates/breakfast.html')
def breakfast():
    return render_template('breakfast.html')


@app.route('/templates/dinner.html')
def dinner():
    return render_template('dinner.html')

@app.route('/input1', methods=['POST', 'GET'])
def input1():
    if request.method == 'POST':
        w = int(request.form['weight'])
        t = int(request.form['Height'])
        body = w / (t/100)**2
        lis = ['Noodle', 'Pizza', 'Fried Rice', 'Roasted Pork', 'Spaghetti', 'Grilled Chicken', 'Sushi', 'Burger', 'Sandwich', 'Tomyum Kung']
        lis_forfat = ['Chicken and Red Plum Salad', 'Grilled Ratatouille Linguine', 'Grilled Steak Tortilla Salad', 'Creamy Lemon Chicken Pasta', 'Beet, Mushroom, and Avocado Salad', 'Roasted Mushroom Parmesan Sandwich', 'Fried Avocado Tacos', 'Bacon and Apple Farro Salad', 'Spicy Tuna Sandwiches', 'Veggie Wraps with Goat Cheese']
        if body <= 20:
            bodys = lis[random.randint(0, 9)]
        else:
            bodys = lis_forfat[random.randint(0, 9)]
        return render_template('lunch.html', body_ssa=bodys)


@app.route('/input2', methods=['POST', 'GET'])
def input2():
    if request.method == 'POST':
        w = int(request.form['weight'])
        t = int(request.form['Height'])
        body = w / (t/100)**2
        lis = ['Beef steak', 'pork steak', 'Salmon Salad', 'padthai', 'spakette', 'eeee', 'eeeeeeee', 'dokkkkk', '555555', 'eieieiei']
        lis_forfat = ['Salad Greens', 'Lean Protein', 'Whole Grains', '6666666', '8888888', '4444444', '777777777', '1121212112', '444444545', '10101010101']
        if body <= 20:
            bodys = lis[random.randint(0, 9)]
        else:
            bodys = lis_forfat[random.randint(0, 9)]
        return render_template('breakfast.html', body_ssa=bodys)


@app.route('/input3', methods=['POST', 'GET'])
def input3():
    if request.method == 'POST':
        w = int(request.form['weight'])
        t = int(request.form['Height'])
        body = w / (t/100)**2
        lis = ['Beef Steak', 'Pork Steak', 'Salmon Salad', 'PadThai', 'Spaghetti', 'Fish Steak', 'Noodle', 'Ramen', 'Hot Curry', 'Fried Chicken']
        lis_forfat = ['Striped Bass With Radish Salsa Verde', 'Grilled Steak Tortilla Salad', 'Vegan Black Bean Soup', 'Speedy Eggplant Parmesan', 'Roasted Tomato & Chive Pizza', 'Grilled Ratatouille Linguine', 'Roasted Shrimp & Poblano Salad', 'Grilled Chicken With Herbed Corn Salsa', 'Soba Salad With Grilled Tofu', 'Salmon Burgers With Cabbage-Apple Slaw']
        if body <= 20:
            bodys = lis[random.randint(0, 9)]
        else:
            bodys = lis_forfat[random.randint(0, 9)]
        return render_template('dinner.html', body_ssa=bodys)



if __name__ == '__main__':
    app.debug = True
    app.run()
