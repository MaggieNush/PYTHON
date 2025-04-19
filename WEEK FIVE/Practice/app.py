from flask import Flask, request, render_template_string

app = Flask(__name__)

style = """
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #fffaf0;
            color: #333;
            padding: 30px;
            max-width: 600px;
            margin: auto;
        }
        h1, h2 {
            color: #d2691e;
        }
        form {
            background: #fff;
            padding: 20px;
            border: 2px dashed #ffa500;
            border-radius: 10px;
        }
        input, select {
            padding: 8px;
            margin: 5px 0 15px 0;
            width: 100%;
            box-sizing: border-box;
        }
        input[type="submit"] {
            background: #ffa500;
            border: none;
            color: white;
            cursor: pointer;
            font-weight: bold;
        }
        input[type="submit"]:hover {
            background: #ff8c00;
        }
        a {
            text-decoration: none;
            color: #d2691e;
        }
    </style>
"""

@app.route('/')
def home():
    return style + '''
        <h1>Welcome to Maggie's Juice Bar 🍹</h1>
        <p><a href="/customize">🍍 Customize your juice</a></p>
    '''

@app.route('/customize', methods=['GET', 'POST'])
def customize():
    if request.method == 'POST':
        name = request.form['name']
        size = request.form['size']
        ingredients = request.form.getlist('ingredients')
        return render_template_string(style + '''
            <h2>Your Juice Order 🍓</h2>
            <p><strong>Name:</strong> {{ name }}</p>
            <p><strong>Size:</strong> {{ size }}</p>
            <p><strong>Ingredients:</strong> {{ ingredients | join(', ') }}</p>
            <p><a href="/customize">🍊 Make another one</a></p>
        ''', name=name, size=size, ingredients=ingredients)

    return style + '''
        <h2>Customize Your Juice 🍍</h2>
        <form method="POST">
            <label>Name:</label>
            <input type="text" name="name" required><br>
            <label>Size:</label>
            <select name="size">
                <option value="250ml">250ml</option>
                <option value="500ml">500ml</option>
                <option value="1L">1L</option>
            </select><br>
            <label>Ingredients (choose at least one):</label><br>
            <input type="checkbox" name="ingredients" value="Mango"> Mango<br>
            <input type="checkbox" name="ingredients" value="Pineapple"> Pineapple<br>
            <input type="checkbox" name="ingredients" value="Ginger"> Ginger<br>
            <input type="checkbox" name="ingredients" value="Mint"> Mint<br>
            <input type="submit" value="🍹 Make My Juice">
        </form>
        <p><a href="/">🏠 Back to home</a></p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
