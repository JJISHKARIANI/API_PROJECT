import json
from models import Joke

class Storage:
    FILENAME = "jokes_history.json"
# aq yvela metodi agwerilia class methodad radgan gamodzaxeba shemedzlos pirdapir da ara storage obj ebis sheqmna
    @classmethod
    def load_joke(cls):
        try:
            with open(cls. FILENAME, "r", encoding='utf-8') as file:
                data = json.load(file)
                return [Joke.from_dict(i) for i in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
# deserealization xdeba compehenstionit da abrunebs cariel files tu faili ar iqneba
    @classmethod
    def save_joke(cls, jokes_list):
        try:
            with open(cls.FILENAME, "w", encoding='utf-8') as file:
                data = [i.to_dict() for i in jokes_list]
                json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"[error]: {e}")
# aq xdeba serializacia  jokes lists gadavcemt datas.
# agwerilia exception nebismieri erroris dasacherad
    @classmethod
    def add_joke(cls, joke: Joke):
        jokes = cls.load_joke()
        jokes.append(joke)
        cls.save_joke(jokes)
# jokes desearilzda daemata axali joke da serializda tavidan

    @classmethod
    def delete_joke(cls, index: int):
        jokes = cls.load_joke()
        if 0 <= index < len(jokes):
            jokes.pop(index)
            cls.save_joke(jokes)
            return True
        return False
#  desearilzda shemowmda index pop s gadavcemt sasurvek index da ukve axal informacias serializacias vuketebt
# brundeba True tu index sworia  false tu index arasworia out of bounds