# ABC Test Client

A test client for the DIT auth broker (ABC)

## Demonstration (Local SSO Provider)

Let's setup a virtual environment:

    virtualenv --python=python3 env
    
Activate it:
    
    . env/bin/activate    
    
And then install the required libs:

    pip install -r requirements.txt  
    
Before we run our test client, we need to boot a local staff-sso instance; just
follow [the instructions](https://github.com/uktrade/staff-sso); when it comes
to the redirect urls, make sure you put

    http://localhost:5000/authorised 
       
And, ensure that the `Default access allowed` is checked (otherwise, you'll get an `access denied` screen, later on)

Note both the `Client id` and the `Client secret` for use below

Finally, as documented in the above instructions, start the SAML IdP test server.       
                    
We now need to set some environment variables;
      
    export CLIENT_URL=http://localhost:5000 \
    export AS_URL=http://localhost:8000 \
    export PORT=5000

Note that `PORT` refers to this test application, note the port of the SSO provider which should be `8000`.
  
  
For the following values will come from your created application, above; these values are only samples.
        
    export CLIENT_ID=X87EOidtsWO34zVpvQ0V1EiqkJRRFwAszYh9UdaJ \
    export CLIENT_SECRET=hCeWoKkAqjefrG5rkTLWym4VFo0S2Xh3LsIyL4NXETLSsxYHIeTQ4b3sfMGiSHr31JGCWgObktr2Qg9qSSY1DBUnZZpQl9AAc995quqcuQOOXPqjt7rrls7TQL85aPu9
    
    
And finally, we can start the application:

    FLASK_APP=app.py flask run
          
Now, it's important that you open the following link in an *incognito* browser.   
          
    http://localhost:5000         

You should be redirected to a login screen; you can use `user1` and `user1pass` or `user2` and `user2pass`.

If all goes well, you should see something like the following info:

    Access token: 3YrOJgDmAmeOmTRjGDg3szynYDr5vj

    Refresh token: Idva2653E95Slx9COgD6ZFU1PtdtkX

    Expires in: 36000

    Token type: Bearer

    Scope: read write

    Email: user1@example.com

    First name:

    Last name:
    
## Demonstration (Any SSO Provider)        

If your application has been registered with another SSO Provider (perhaps [UAT Staff SSO](https://sso.trade.uat.uktrade.io/)),
you can simply alter the above environment variables, accordingly, specifically: `CLIENT_ID`,`CLIENT_SECRET` and `CLIENT_URL`; just ensure
that one of the redirect uris is `http://127.0.0.1:5000` (and not 127.0.0.1).

Then simply follow the above steps, starting with the application start.
