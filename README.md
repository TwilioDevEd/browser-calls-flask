<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Browser Calls for Python - Flask

> This repository is now archived and is no longer being maintained. 
> Check out the [JavaScript SDK Quickstarts](https://www.twilio.com/docs/voice/sdks/javascript/get-started) to get started with browser-based calling. 

## About

Learn how to use [Twilio's JavaScript SDK](https://www.twilio.com/docs/voice/sdks/javascript) to make browser-to-phone and browser-to-browser calls with ease. The unsatisfied customers of the Birchwood Bicycle Polo Co. need your help!

### Create a TwiML App

This project is configured to use a **TwiML App**, which allows us to easily set the voice URLs for all Twilio phone numbers we purchase in this app.

Create a new TwiML app at https://www.twilio.com/console/voice/twiml/apps and use its `Sid` as the `TWILIO_APPLICATION_SID` environment variable wherever you run this app.

Once you have created your TwiML app, configure your Twilio phone number to use it ([instructions here](https://www.twilio.com/help/faq/twilio-client/how-do-i-create-a-twiml-app)).

If you don't have a Twilio phone number yet, you can purchase a new number in your [Twilio Account Dashboard](https://www.twilio.com/user/account/phone-numbers/incoming).

## Local development

This project is built using the [Flask](http://flask.pocoo.org/) web framework. It runs on Python 2.7+ and Python 3.4+.

1. To run the app locally, first clone this repository and `cd` into it.

1. Create and activate a new python3 virtual environment.

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

1. Install the requirements using pip.

    ```bash
    pip install -r requirements.txt
    ```

1. Copy the `.env.example` file to `.env`, and edit it including your credentials
   for the Twilio API (found at https://www.twilio.com/user/account/settings). You
   will also need a [Twilio Number](https://www.twilio.com/user/account/phone-numbers/incoming) and TwiML App SID you made above. You will also need a [SECRET_KEY](https://flask.palletsprojects.com/en/2.0.x/config/#SECRET_KEY). 

1. Run `source .env` to apply the environment variables (or even better, use [autoenv](https://github.com/kennethreitz/autoenv))

1. Run the migrations.

    ```bash
    python manage.py db upgrade
    ```

1. Modify seed data.

   We have provided an example of name and phone number in the seed data. In order for
   the application to send SMS notifications, you must edit this seed data providing
   a real phone number where you want the SMS notifications to be received.

   In order to do this, you must modify
   [this file](https://github.com/TwilioDevEd/browser-calls-flask/blob/master/manage.py#L25)
   that is located at: `project_root/manage.py`

1. Seed the database.

   ```bash
   python manage.py dbseed
   ```

1. Start ngrok.

   To actually forward incoming calls, your development server will need to be publicly accessible.
   [We recommend using ngrok to solve this problem](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html).
   
   ```bash
   ngrok http 5000
   ```

   Once you have started ngrok, update your TwiML app's voice URL setting to use your ngrok hostname. It will look something like this:

   ```
   http://[your-domain].ngrok.io/support/call
   ```

1. Start the development server.

    ```bash
    python manage.py runserver
    ```

Once ngrok is running, open up your browser and go to your ngrok URL.

That's it!

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests.

    ```
    FLASK_ENV=testing manage.py test
    ```

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
