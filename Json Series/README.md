# How to use Json in Python

By default this are the tranlations decoding json files in python:

|JSON           |Python    |
|---------------|:--------:|
|object         |dict      |
|array          |list      |
|string         |str       |
|number (int)   |int       |
|number (real)  |float     |
|true           |True      |
|false          |False     |
|null           |None      |

```python
import json

# Parse the json file data into python.
data = json.loads(json_file)

# In case you modified the information and you want to save it in a json file run you need the dump function.
new_json_file = json.dumps(data, indent=2)
```

An important detail of the previous code is using **indent** so you can let some read the file in an easier way. Also you can **sort** the information using the *sort_keys* argument.

To save the data from the json file in a python project, when the data is outside the python script, you can use the following commands:

```python
import json

# Open the json file in the same directory as the python script and save it in the python object.
with open('states.json')as f:
    data = json.load(f)
```

Once done that you can move through the data in the python object, in this case, it will be per **state** in the json file and if you are interested print it with the state abbreviation.

```python
for state in data['states']:
    print(state['name'], state['abbreviation'])
```

We have checked how to access the information in the states list, but if you were curious and checked the json file you may have noticed that inside every state there is a list of the area codes. Here is a tree diagram to explain how the json file has been built:

```bash
States JSON.
├───States
│   ├───Name
│   ├───Abbreviation
│   ├───Area Codes
│   │   ├───Area Code 1
│   └───────Area Code 2
└───Json Series
```

So to be able to check the area codes, we will use the code from above and use a second for to iterate through the area codes of each state.

```python
# Checking the area codes list of every state
for item in data['states']:
    name = item['name']
    abbreviation = item['abbreviation']
    print(name,abbreviation,':')
    for area in item['area_codes']:
        print(area)
```

Nowwe will parse from a python object to a json file and save it.

```python
# Open the file and then doing a dump with the data and the file name in which you want to write the data. In this case, the file name is new states.
with open('new_states.json','w') as f:
    json.dump(data,f, indent=2)
```

Now we are going to extract the information from an API returning a json file. For this case I used the API from [World Trading Data][API] in this API it is only needed to create an account and will give you a token for **250 free calls** to their API per day.

To start this second demo I am going to call the API and store the data in the data python object.

```python
import json
from urllib.request import urlopen

# Using the World Trading Data API to import data of stock of Microsoft
with urlopen("https://api.worldtradingdata.com/api/v1/stock?symbol=MSFT&api_token="Your_Token") as response:
    source = response.read()

# Information parsed into python
data = json.loads(source)
```

Most of this notes were taken from the [Tutorial] of Corey Schafer, follow his tutorials and hope being helpful in your search for knowledge.

[Tutorial]: https://www.youtube.com/watch?v=9N6a-VLBa2I
[API]: https://www.worldtradingdata.com