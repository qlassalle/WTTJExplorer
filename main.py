import requester
import json

jobs = requester.process_request()

jobs.sort(key=lambda j: j.published_at, reverse=True)
# print(len(jobs))
for job in jobs:
    print(json.dumps(job.__dict__, indent=4, separators=(',', ': '), ensure_ascii=False))

# print(json.dumps(json_response['hits'][0], indent= 4, separators=(',', ': ')))