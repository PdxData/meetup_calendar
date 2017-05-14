"""

Create a `local.py` file next to this `default.py` file to put your custom
settings.  An example `local.py` file is:

    # Get the api key associated with your Meetup account by logging in and
    # navigating to https://secure.meetup.com/meetup_api/key/ .
    # Never share your actual api key with anyone.

    meetup_api_key = '111111111111111111111111111'

"""

meetup_api_key = ''

# -----------  Anything above this line will be overwritten by what's in
# `local.py` due to the following try/except import  -------------------------
try:
    from local import *  # noqa: F401, F403
except ImportError:
    pass
