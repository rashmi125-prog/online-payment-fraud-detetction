from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="yourdb", user="youruser", password="yourpass", host="localhost", port="5432")
cur = conn.cursor()

@app.route('/register', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        cur.execute("INSERT INTO Registration (name, email, date_of_birth) VALUES (%s, %s, %s)",
                    (data['name'], data['email'], data['dob']))
        conn.commit()
        return jsonify({"message": "User registered"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users', methods=['GET'])
def read_users():
    cur.execute("SELECT * FROM Registration")
    users = cur.fetchall()
    return jsonify(users)

@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    try:
        cur.execute("UPDATE Registration SET name=%s, email=%s, date_of_birth=%s WHERE id=%s",
                    (data['name'], data['email'], data['dob'], id))
        conn.commit()
        return jsonify({"message": "User updated"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        cur.execute("DELETE FROM Registration WHERE id=%s", (id,))
        conn.commit()
        return jsonify({"message": "User deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
