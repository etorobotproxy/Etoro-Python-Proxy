from flask import Flask, jsonify
import cloudscraper

app = Flask(__name__)
scraper = cloudscraper.create_scraper()

@app.route('/trades/<username>')
def trades(username):
    json = scraper.get(f'https://www.etoro.com/api/streams/v2/streams/user-trades/{username}').json()
    return jsonify(json)

@app.route('/ping')
def ping():
    return jsonify({'message': 'PONG!'})

@app.route('/user/<username>')
def user(username):
    try:
        data = scraper.get(f'https://www.etoro.com/api/logininfo/v1.1/users/{username}').json()
        if data['optOut']: 
            return jsonify({'private': True})
        else:
            return jsonify({'exists': True})
    except:
        return jsonify({'exists':False})

# @app.route('/general')
# def general():
#     json = scraper.get('https://www.etoro.com/api/streams/v2/streams/user-trades/theryall').json()
#     return jsonify(json)

if __name__ == '__main__':
    app.run(debug=True)