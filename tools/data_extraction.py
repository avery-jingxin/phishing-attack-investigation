from email import policy
from email.parser import BytesParser

data = {
    "from": [],
    "to": [],
    "date":[],
    "subject":[],
    "body":[],
}

# Extract information
def get_email_info(fp):
    msg = BytesParser(policy=policy.default).parse(fp, headersonly=False)
    header = msg.get_header(preferencelist=('plain')).get_content()
    body = msg.get_body(preferencelist=('plain')).get_content()

    data["from"].append(header['from'])
    data["to"].append(header['to'])
    data["date"].append(header['date'])
    data["subject"].append(header['subject'])
    data["body"].append(body.strip())
  