import os
import requests

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


# config 
CLIENT_ID = os.getenv("CLIENT_ID") 
CLIENT_SECRET = os.getenv("CLIENT_SECRET") 
CLIENT_URL = os.getenv("CLIENT_URL") 
AS_URL = os.getenv("AS_URL", "https://sso.trade.gov.uk")
PORT = os.getenv("PORT", "5000")

@app.route('/', methods=['GET', 'POST'])
def login():
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        url = '{url}?scope={scope}&state={state}&redirect_uri={redirect_uri}&response_type={response_type}&client_id={client_id}'.format(
            url=f'{AS_URL}/o/authorize/',
            scope='read write',
            state='kalle',
            redirect_uri=f'{CLIENT_URL}{url_for("authorised")}',
            response_type='code',
            client_id=CLIENT_ID
        )
        return redirect(url)
    return render_template('login.html')


@app.route('/authorised', methods=['GET'])
def authorised():
    code = request.args.get('code')
    # state = request.args.get('state')  # TODO check

    response = requests.post(
        f'{AS_URL}/o/token/',
        data={
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': f'{CLIENT_URL}{url_for("authorised")}',
        }
    )

    token = response.json()['access_token']
    profile = requests.get(f'{AS_URL}/api/v1/user/me/',
                 headers={
                     'Authorization': f'Bearer {token}'
                 })

    data = {}
    data.update(response.json())
    data.update(profile.json())

    assert response.status_code == 200
    return render_template('access_token.html', **data)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
