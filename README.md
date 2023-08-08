## Required to run

You will need a credentials.json file as this application will use the Gmail API to send emails.

credentials.json:

```javascript
{
    "installed":
    {
        "client_id":[your-client-id],
        "project_id":[your-project-name],
        "auth_uri":"https://accounts.google.com/o/oauth2/auth",
        "token_uri":"https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
        "client_secret":[your-client-secret],
        "redirect_uris":["http://localhost"]
    }
}
```
