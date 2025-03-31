from flask import Flask, jsonify, request
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/heroes', methods=['GET', 'POST'])
def heroes():
    if request.method == 'GET':
        heroes = Hero.query.all()
        return jsonify([{'id': h.id, 'name': h.name, 'super_name': h.super_name} for h in heroes])
    if request.method == 'POST':
        data = request.json
        hero = Hero(name=data['name'], super_name=data['super_name'])
        db.session.add(hero)
        db.session.commit()
        return jsonify({'id': hero.id, 'name': hero.name, 'super_name': hero.super_name})

@app.route('/heroes/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def hero(id):
    hero = Hero.query.get(id)
    if request.method == 'GET':
        return jsonify({'id': hero.id, 'name': hero.name, 'super_name': hero.super_name})
    if request.method == 'PATCH':
        data = request.json
        if 'name' in data: hero.name = data['name']
        if 'super_name' in data: hero.super_name = data['super_name']
        db.session.commit()
        return jsonify({'id': hero.id, 'name': hero.name, 'super_name': hero.super_name})
    if request.method == 'DELETE':
        db.session.delete(hero)
        db.session.commit()
        return jsonify({'message': 'Hero deleted'})

@app.route('/powers', methods=['GET', 'POST'])
def powers():
    if request.method == 'GET':
        powers = Power.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'description': p.description} for p in powers])
    if request.method == 'POST':
        data = request.json
        power = Power(name=data['name'], description=data['description'])
        db.session.add(power)
        db.session.commit()
        return jsonify({'id': power.id, 'name': power.name, 'description': power.description})

@app.route('/powers/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def power(id):
    power = Power.query.get(id)
    if request.method == 'GET':
        return jsonify({'id': power.id, 'name': power.name, 'description': power.description})
    if request.method == 'PATCH':
        data = request.json
        if 'name' in data: power.name = data['name']
        if 'description' in data: power.description = data['description']
        db.session.commit()
        return jsonify({'id': power.id, 'name': power.name, 'description': power.description})
    if request.method == 'DELETE':
        db.session.delete(power)
        db.session.commit()
        return jsonify({'message': 'Power deleted'})

@app.route('/hero_powers', methods=['POST'])
def hero_powers():
    data = request.json
    hero_power = HeroPower(
        strength=data['strength'],
        hero_id=data['hero_id'],
        power_id=data['power_id']
    )


@app.route('/heroes/<int:id>', methods=['PATCH'])
def update_hero(id):
    hero = Hero.query.get(id)
    data = request.json
    if 'name' in data: 
        hero.name = data['name']
    if 'super_name' in data:
        hero.super_name = data['super_name']
    db.session.commit()
    return jsonify({'id': hero.id, 'name': hero.name, 'super_name': hero.super_name})

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    data = request.json
    if 'name' in data:
        power.name = data['name']
    if 'description' in data:
        power.description = data['description']
    db.session.commit()
    return jsonify({'id': power.id, 'name': power.name, 'description': power.description})
    db.session.add(hero_power)
    db.session.commit()
    return jsonify({'id': hero_power.id, 'hero_id': hero_power.hero_id, 'power_id': hero_power.power_id, 'strength': hero_power.strength})

if __name__ == '__main__':
    app.run(port=5555)