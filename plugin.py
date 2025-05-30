import requests
import logging
import json

# implements custom screen data API as per https://docs.usetrmnl.com/go/private-plugins/create-a-screen
class plugin():
    
    BASE_URL = "https://usetrmnl.com/api/custom_plugins/{}"
    
    def __init__ (self, id):
        self.url = self.BASE_URL.format(id)

    def post(self, data, deep_merge=False, stream_limit=None):
        data_dict = {'merge_variables' : data}
        if deep_merge and stream_limit:
            logging.error("Cannot use deep merge strategy with stream limit")
            return
        elif deep_merge:
            data_dict.update({"merge_strategy": "deep_merge"})
        elif stream_limit:
            data_dict.update({"merge_strategy": "stream"})
            data_dict.update({"stream_limit": stream_limit})

        logging.debug("Posting data: {} to: {}".format(data_dict, self.url))

        return requests.post(
            self.url,
            data=json.dumps(data_dict),
            headers={'content-type': 'application/json'})
