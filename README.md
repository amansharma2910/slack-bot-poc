# Slack Bot POC
---

This slack bot can be integrated in your application via the "Add to Slack" button. Your platform's users can then install this application inside their workspace to get platform event notifications delivered straight to their designated channels.


## Requirements
---

### 1. Create Slack App
You can follow this guide to setup a basic Slack app: https://api.slack.com/authentication/basics

### 2. Add following scopes
For the app to work, you would require the following scopes to be enabled for your app:
1. `incoming-webhook` : To send messages to the channels where users install the app in their workspace.
2. `users:read` : To read user data.
3. `users:read.email` : To fetch user email.

### 3. Enable Public Distribution for app
Head over to the `Manage Distribution` section in your app's `Settings`. Enable public distribution from there.

### 4. Add .env to the source code
Here is the sample `.env` file to be added to the root of your source code.
```
SLACK_CLIENT_ID=<app_client_ID>
SLACK_CLIENT_SECRET=<app_client_secret>
```


## Running the application:
---

To run the server, simply run the following commands:

#### With Docker:
```bash
docker-compose up
```

__OR__

#### Without Docker (Development Mode)
```bash
uvicorn src.main:app --reload
```

Feel free to use this tutorial code to develop your own Slack bots! Check out the usage [license](LICENSE).