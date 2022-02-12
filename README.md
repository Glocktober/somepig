# Somepig

Somepig is a simple Flask app useful in debugging web configurations and integrations.

I don't want to oversell this - it's a simple application that might be useful to others.

### What it does for you
* Confirm HTML headers passed to the wsgi app
* Confirm the environment variables passed to the wsgi app
* Check for bearer token JWT (the token is decoded but not verified) (This is optional and is used only if the `pyjwt` module is installed.)

### Where this is useful
* Test installation of wsgi server (e.g. mod_wsgi configuration)
* Verifying enviroment variables (including REMOTE_USER) passed to the app from the web server
* Examine the impact of proxy servers on your app
* Debugging mod_auth_mellon (SAML) or mod_auth_oidc integrations
* These are Apache examples but the same is true for other web servers

### API routes
| URL route | format|description |
|-------|--------|-------|
|/hdr   | json|dump HTML headersp|
|/env|json|dump (most) wsgi environment variables|
|/whoami|html|print value of `REMOTE_USER`|
|/bearer|json|print **JWT** bearer token (optional)|
### Installation
* install from github
* integrate with your web server as you would any other Python Flask application
