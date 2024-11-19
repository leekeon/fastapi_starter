import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3 needed to disable SSL verification
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Monkey patch the requests library to disable SSL verification
_original_request = requests.Session.request

def _patched_request(self, *args, **kwargs):
    kwargs['verify'] = False
    return _original_request(self, *args, **kwargs)

# Call the patch function to apply it immediately upon importing the module
requests.Session.request = _patched_request
