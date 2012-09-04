import sys
import urllib
sys.path.append("mashape")

from mashape.http.http_client import HttpClient
from mashape.http.content_type import ContentType
from mashape.auth.mashape_auth import MashapeAuth
from mashape.auth.basic_auth import BasicAuth
from mashape.auth.query_auth import QueryAuth
from mashape.auth.custom_header_auth import CustomHeaderAuth


class SentimentAnalysisFree:

    auth_handlers = []
    PUBLIC_DNS = "chatterbox-analytics-sentiment-analysis-free.p.mashape.com"

    def __init__(self, public_key, private_key):
        self.auth_handlers.append(MashapeAuth(public_key, private_key))

    def classifytext(self, lang, text, exclude=None, mashape_callback=None):
        parameters = {
                "lang": lang,
                "text": text,
                "exclude": exclude}

        mashape_client = HttpClient()
        response = mashape_client.do_call(
                "POST",
                "https://" + self.PUBLIC_DNS + "/sentiment/current/classify_text/",
                parameters,
                self.auth_handlers,
                ContentType.FORM,
                mashape_callback,
                True)
        return response

