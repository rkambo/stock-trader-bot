## Context

This application is made to send a weekly report, outlining the state of different financial industries. I made this in order to study the [Golden Cross vs Death Cross](https://www.investopedia.com/ask/answers/121114/what-difference-between-golden-cross-and-death-cross-pattern.asp) method of investing, where an investor takes the Simple Mean Average of a short window (typically 50 days) and compares it against the Simple Mean Average of a longer window (typically 200 days). A golden cross forms when the short term SMA crosses above the long term SMA, and can signify a market with increasing prices (a bull market), and the opposite being a death cross, signifying a market with decreasing prices (a bear market).

## Requirements

## Env file

Make a .env file with the following variable (the email to send the report to):
`EMAIL=your-email-address`

## Automation

It is recommended that a cron job be set up to execute `main.py` to execute at the beginning of each week.

### Gmail API

This requires a valid [Gmail API](https://developers.google.com/gmail/api/guides) setup, through creating a Google Cloud Platform project.

You will need to create a credentials.json file as this application will use the Gmail API to send emails.

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
