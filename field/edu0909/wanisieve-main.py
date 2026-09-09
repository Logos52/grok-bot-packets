from fugashi import Tagger
import requests
import json
import sys
import time
from jisho_api.kanji import Kanji
from jisho_api.word import Word
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate an Anki deck from parsed Japanese text, filtered by WaniKani level"
    )
    parser.add_argument(
        "-k", "--api-key",
        required=True,
        help="Your WaniKani personal access token"
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Path to the .txt file containing the chapter text"
    )
    parser.add_argument(
        "-d", "--deck",
        required=True,
        help="Name of the Anki deck to create/add to"
    )
    return parser.parse_args()

arg = parse_args()

API_TOKEN = arg.api_key
BASE_URL = "https://api.wanikani.com/v2"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Wanikani-Revision": "20170710"
}


ANKI_CONNECT_URL = "http://localhost:8765"

def invoke(action, **params):
    payload = {
        "action": action,
        "version": 6,
        "params": params
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload).json()
    
    if len(response) != 2:
        raise Exception("Unexpected response from AnkiConnect")
    if response.get("error") is not None:
        raise Exception(response["error"])
    
    return response["result"]

def get_burned_vocab():
    """Fetches all assignment records that are marked as burned."""
    burned_items = []
    url = f"{BASE_URL}/subjects/?burned=true&types=vocabulary"
    
    while url:
        response = requests.get(url, headers=HEADERS)
        
        # Respect rate limits if pushing too hard
        if response.status_code == 429:
            time.sleep(10)
            continue
            
        if response.status_code != 200:
            raise Exception(f"API Error {response.status_code}: {response.text}")
            
        data = response.json()
        #burned_items.extend(data["data"])
        for item in data["data"]:
            char = item["data"].get("characters")
            burned_items.append(char)
        
        # Move to the next page of results if it exists (500 items max per page)
        url = data["pages"]["next_url"]

        
    return burned_items

def select_new_vocab(words, comp):
    new_words = []
    for i in words:
        if i not in comp:
            new_words.append(i)
    print(new_words)
    return new_words


def create_notes(words, deckName):
    notes = []
    for i in words:
        if Word.request(i):
            x = (Word.request(i).data[0].senses[0].english_definitions)
            notes.append({
            "deckName": f"{deckName}",
            "modelName": "Basic",
            "fields": {"Front": f"{i}", "Back": f"{", ".join(x)}"},
            "options": {"allowDuplicate": False},
            "tags": ["vn-mined"]
        })
    return notes

def create_deck(deckName, notes):
    invoke("createDeck", deck=deckName)
    invoke("addNotes", notes=notes)



f = open(arg.input)
f = f.read()
tagger = Tagger("-Owakati")
words = [word.surface for word in tagger(f)]
burned = get_burned_vocab()
words2 = select_new_vocab(words, burned)
x = create_notes(words2, arg.deck)
create_deck(arg.deck,x)





