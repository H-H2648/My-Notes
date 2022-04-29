# Python Unit Tests:

## Mock
In python unittest, unittest.mock allows us to define a "mock" object with "mock" features.

For instance, if I call r = request.get('http://facebook.com'), by defining request = mock() and redefining the attributes of the mock object request, it allows us to do unit testing without access to the internet (we don't want the test to fail because of external failures)

More powerful feature with patch(?)