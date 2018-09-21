import json
import requests

class FoodGroup(object):
    name = ""
    impact = ""
    suggestion = ""

    def __init__(self, name, impact, suggestion):
        self.name = name
        self.impact = impact
        self.suggestion = suggestion

def parseJson(jsonObj):
    textarray = []
    json_object = jsonObj
    json_body = json_object[0]['lines']
    body_length = len(json_body)
    for line_num in range(0,body_length):
        words = json_body[line_num]
        words_length = len(words)
        word_list = words['words']
        word_list_length =len(word_list)
        for word in range(0,word_list_length):         
            textarray.insert(word, word_list[word]['text'])
            
    return textarray

def fillDictionary(dict):
    beef = FoodGroup("BEEF", "", "")
    beef.impact = "Livestock farming produces from 20% to 50% of all man-made greenhouse gas emissions."
    beef.suggestion = "Some other forms of protein are just as good! Such as lentils, tofu, and hummus!"
    dict[beef.name] = beef

    milk = FoodGroup("MILK", "", "")
    milk.impact = "Dairy operations can consume large volumes of water to grow feed, water cows, manage manure and process products. Additionally, manure and fertilizer runoff from dairy farms can pollute water resources. "
    milk.suggestion = "Dietitians tend to favor soy milk as an alternative to cow’s milk because its protein content is close to that of cow’s milk, and most brands are fortified with calcium and vitamins."
    dict[milk.name] = milk

    chicken = FoodGroup("CHICKEN", "", "")
    chicken.impact = "Chicken production has devastating consequences on water quality, contributes to global climate change and harms natural habitat"
    chicken.suggestion = "Replace chicken in traditional dishes by trying chicken-free veggie pot pies, fajitas, alfredo pasta, pad thai and burritos."
    dict[chicken.name] = chicken

    straws = FoodGroup("STRAWS", "", "")
    straws.impact = "It takes up to 200 years for a plastic straw to decompose and they cant be recycled in most places!"
    straws.suggestion = "Use metal straws!"
    dict[straws.name] = straws

    cheese = FoodGroup("CHEESE", "", "")
    cheese.impact = "It turns out that cheese may do as much harm to the environment as some kinds of meat."
    cheese.suggestion = "Vegan cheese is just as good and doesn't harm the environment!"
    dict[cheese.name] = cheese


def filterResults(temparray, dict):
    data = {}
    for item in temparray:
        newItem = item.upper()
        if newItem in dict:
            data[(dict.get(item)).name] = dict.get(item).impact
    return data

def connect_to_azure(url):
        subscription_key = <azure_subscription_key>
        vision_base_url = <azure_base_url>
        ocr_url = vision_base_url + "ocr"

        image_url = url

        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        params  = {'language': 'unk', 'detectOrientation': 'true'}
        data    = {'url': image_url}
        response = requests.post(ocr_url, headers=headers, params=params, json=data)
        parsed_response = requests.post(ocr_url, headers=headers, json=data)
        response.raise_for_status()
        analysis = response.json()
       
        return analysis['regions']    

def main(url):

    results = connect_to_azure(url)
    temparray = parseJson(results)
    dict = {}
    fillDictionary(dict)
    keywords = filterResults(temparray, dict)
    json_data = json.dumps(keywords)

    #json_data contains final result of high impact items found in receipt 

if __name__ == "__main__":
    main()
