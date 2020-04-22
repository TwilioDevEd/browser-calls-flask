from .base import BaseTest
from browser_calls_flask.models import SupportTicket
import json

# Import Mock if we're running on Python 2
import six

if six.PY3:  # pragma: no cover
    from unittest.mock import patch, MagicMock
else:  # pragma: no cover
    from mock import patch, MagicMock


class SupportTicketViewsTests(BaseTest):

    def test_save_valid_ticket(self):
        # When we post valid data
        response = self.post_ticket(name='Neo', phone_number='+15551239483',
                                    description='Issue while destroying the Matrix')

        # Then nothing is persisted
        new_ticket = SupportTicket.query.filter_by(name='Neo').first()
        self.assertNotEquals(None, new_ticket)
        self.assertIn("Your ticket was submitted! An agent will call you soon.", str(response.data))

    def test_checks_for_invalid_phone_numbers_before_saving(self):
        # When we post an invalid number
        response = self.post_ticket(name='James', phone_number='92',
                                    description="I don't know how to use...")

        # Then a message appears and data doesnt get persisted
        self.assertIn("Invalid phone number", str(response.data))
        new_ticket = SupportTicket.query.filter_by(name='James').first()
        self.assertEquals(None, new_ticket)

    def test_dashboard_shows_tickets(self):
        # Given we have a ticket
        ticket1 = SupportTicket(name="John", phone_number="+15551239483",
                                description="Got an issue while...")
        self.db.session.add(ticket1)
        self.db.session.commit()

        # When we GET the dashboard
        response = self.client.get('/dashboard')

        # Then John's ticket is there
        self.assertIn("John", str(response.data))
        self.assertIn("+1 555-123-9483", str(response.data))

    def post_ticket(self, name, phone_number, description):
        data = dict(name=name, phone_number=phone_number, description=description)
        return self.client.post('/tickets', data=data, follow_redirects=True)


class TwilioTokenTests(BaseTest):

    def test_get_token_for_customer_by_default(self):
        # Given
        mock_capability = MagicMock()
        mock_capability.to_jwt.return_value = b'abc123'

        # When
        with patch('browser_calls_flask.views.ClientCapabilityToken', return_value=mock_capability) as mock:
            response = self.client.get('/support/token', query_string={'forPage': '/'})

        # Then
        # Make sure our mock_capability object was called with the right
        # arguments and that the view returned the correct response
        self.assertTrue(mock_capability.allow_client_outgoing.called)
        mock_capability.allow_client_incoming.assert_called_once_with('customer')
        self.assertTrue(mock_capability.to_jwt.called)
        self.assertEqual({"token": "abc123"}, json.loads(response.data.decode("utf-8")))

    def test_get_token_for_agent_if_referrer_is_dashboard(self):
        # Given
        mock_capability = MagicMock()
        mock_capability.to_jwt.return_value = b'abc123'

        # When
        with patch('browser_calls_flask.views.ClientCapabilityToken', return_value=mock_capability) as mock:
            response = self.client.get('/support/token', query_string={'forPage': '/dashboard'})

        # Then
        self.assertTrue(mock_capability.allow_client_outgoing.called)
        mock_capability.allow_client_incoming.assert_called_once_with('support_agent')
        self.assertTrue(mock_capability.to_jwt.called)
        self.assertEqual({"token": "abc123"}, json.loads(response.data.decode("utf-8")))


class CallTest(BaseTest):

    def test_call_phone_number(self):
        # When we post with a phoneNumber parameter
        response = self.client.post('/support/call', data={'phoneNumber': '+15555555555'})

        # Then we get it on the TwiML response
        self.assertIn('<Number>+15555555555</Number>', str(response.data))

    def test_call_support(self):
        # When
        response = self.client.post('/support/call')

        # Then
        self.assertIn('<Client>support_agent</Client>', str(response.data))
