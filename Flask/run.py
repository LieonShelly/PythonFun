from Blog import create_app
import requests

app = create_app()

if __name__ == '__main__':
    print('-----Runing----------')
    app.run(host='0.0.0.0', port=80)
    req = requests.get('http://127.0.0.1:4000')
    print(req.text)
    print(req.status_code)
