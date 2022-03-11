<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Browser Calls for Python - Flask

![Flask](https://github.com/TwilioDevEd/browser-calls-flask/workflows/Flask/badge.svg)

Learn how to use [Twilio Client](https://www.twilio.com/client) to make
browser-to-phone and browser-to-browser calls with ease. The unsatisfied
customers of the Birchwood Bicycle Polo Co. need your help!

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/browser-calls/python/flask)!

## Quickstart

### Create a TwiML App

This project is configured to use a **TwiML App**, which allows us to easily set
the voice URLs for all Twilio phone numbers we purchase in this app.

Create a new TwiML app [here](https://console.twilio.com/us1/develop/voice/manage/twiml-apps?frameUrl=%2Fconsole%2Fvoice%2Ftwiml%2Fapps%3Fx-target-region%3Dus1) and
use its `SID` as the `TWIML_APPLICATION_SID` environment variable wherever you
run this app.


[Learn more about creating a TwiML app here](https://support.twilio.com/hc/en-us/articles/223180928-How-Do-I-Create-a-TwiML-App-)

Once you have created your TwiML app, configure your Twilio phone number to use
it ([instructions here](https://support.twilio.com/hc/en-us/articles/223180928-How-Do-I-Create-a-TwiML-App-)).
If you don't have a Twilio phone number yet, you can purchase a new number in
your [Twilio Account Dashboard](https://console.twilio.com/us1/develop/phone-numbers/manage/search?frameUrl=%2Fconsole%2Fphone-numbers%2Fsearch%3Fx-target-region%3Dus1&currentFrameUrl=%2Fconsole%2Fphone-numbers%2Fsearch%3FisoCountry%3DUS%26searchTerm%3D%26searchFilter%3Dleft%26searchType%3Dnumber%26x-target-region%3Dus1%26__override_layout__%3Dembed%26bifrost%3Dtrue).

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
