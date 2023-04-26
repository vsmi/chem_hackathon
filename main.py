import requests

# response = requests.get("https://toxric.bioinforai.tech/jk/search/getToxicityBigCategory")
# print(response.status_code)
# print(response.text)

# resp_pubchem = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/240/JSON/")
# print(resp_pubchem.text)

# Construct the API request URL
cid = '2244'
url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/property/MolecularWeight/JSON'

# Send the API request and parse the JSON response
response = requests.get(url)
data = response.json()
print(data)
# Extract the fingerprint bit string and convert to binary format
# fingerprint_hex = data['PropertyTable']['Properties'][0]['Value']['StringWithMarkup'][0]['String']
# fingerprint_bin = bin(int(fingerprint_hex, 16))[2:].zfill(881)