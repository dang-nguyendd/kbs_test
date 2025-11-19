import csv
import re
import difflib
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import os
import json


class KnowledgeBase:
    """
    A class that holds a dictionary of facts and a list of rule dictionaries.
    """

    def __init__(self, facts=None, rules=None):
        self.facts = facts if facts is not None else {}
        self.rules = rules if rules is not None else []

# ----- GETTERS -----

    def get_all(self):
        return self.facts, self.rules

    def get_fact(self, key):
        return self.facts.get(key)

    def get_rule_by_key(self, key, value):
        return [rule for rule in self.rules if rule.get(key) == value]

# ----- SETTERS -----

    def set_fact(self, key, value):
        self.facts[key] = value

    def add_rule(self, rule_dict):
        if isinstance(rule_dict, dict):
            self.rules.append(rule_dict)
        else:
            raise TypeError("rule_dict must be a dictionary")

    def load_csv_kbs(self, filepath, limit=10):
        """
        Load up to `limit` rows from a CSV file,
        trim whitespace from each cell,
        and return a list of dictionaries.
        """
        data = []
        with open(filepath, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader):
                if i >= limit:
                    break
                clean_row = {k.strip(): v.strip() for k, v in row.items() if v is not None}
                data.append(clean_row)
        return data

    def load_healthcare_csv(self, filepath):
        records = self.load_csv_kbs(filepath)

        facts = {}
        rules = []

        for row in records:
            # Expecting CSV columns:
            # Disease, Keywords, Overview, Symptoms, Causes, Prevention,
            # Diagnosis, Treatment, Preparing_for_your_appointment

            disease = row.get("Disease", "")
            keywords = row.get("Keywords", "")

            key = f"{disease}, {keywords}".strip()

            # ----- FACTS -----
            facts[key] = row.get("Overview", "")

            # ----- RULES -----
            rule = {
                "disease": key,
                "value": True,
                "Symptoms": row.get("Symptoms", ""),
                "Causes": row.get("Causes", ""),
                "Prevention": row.get("Prevention", ""),
                "Diagnosis": row.get("Diagnosis", ""),
                "Treatment": row.get("Treatment", ""),
                "Preparing_for_your_appointment": row.get("Preparing_for_your_appointment", ""),
            }

            rules.append(rule)

        self.facts = facts
        self.rules = rules

class InferenceEngine:
    """
    Inference Engine that:
    1. Takes user input,
    2. Performs full-text search across KnowledgeBase facts' keys,
    3. Selects the highest match,
    4. Retrieves the rules related to that fact key.
    """

    def __init__(self, knowledge_base):
        """
        Initialize with a KnowledgeBase object.
        """
        self.kb = knowledge_base

# ----- Compute match score between user input & key -----
    def compute_score(self, user_text, fact_key):
        """
        Compute fuzzy similarity (0–100).
        Uses SequenceMatcher to estimate typo-tolerant similarity.
        """
        return int(difflib.SequenceMatcher(None, user_text.lower(), fact_key.lower()).ratio() * 100)

# ----- Find best fact match -----
    def find_best_fact_key(self, user_input):
        best_key = None
        best_score = 0

        for key in self.kb.facts.keys():
            score = self.compute_score(user_input, key)
            if score > best_score:
                best_score = score
                best_key = key

        return best_key, best_score

# ----- Get rules for best-matched fact -----
    def infer(self, user_input):
        """
        Perform inference:
        - Find best-matching fact key
        - Retrieve rules related to that key
        - Return results in dictionary form
        """

        best_key, score = self.find_best_fact_key(user_input)

        if best_key is None or score == 0:
            return {
                "match": None,
                "score": 0,
                "rules": [],
                "message": "No relevant information found."
            }

        # Get matching rules
        matched_rules = [
            rule for rule in self.kb.rules 
            if rule.get("disease") == best_key
        ]

        return {
            "match": best_key,
            "score": score,
            "rules": matched_rules,
            "overview": self.kb.facts.get(best_key, ""),
            "message": "Match found."
        }

class NLPProcessor:
    """
    Processes user input text to extract cleaned main keywords:
    - lowercase
    - trim
    - remove punctuation
    - remove stopwords
    - stemming
    """

    def __init__(self):
        self.stemmer = PorterStemmer()
        try:
            self.stop_words = set(stopwords.words("english"))
        except:
            import nltk
            nltk.download("stopwords")
            self.stop_words = set(stopwords.words("english"))

# ----- Basic cleaning -----
    def clean_text(self, text):
        if not isinstance(text, str):
            return ""

        text = text.lower().strip()                       # lowercase + trim
        text = re.sub(r"[^\w\s]", " ", text)              # remove punctuation
        text = re.sub(r"\d+", " ", text)                  # remove numbers
        text = re.sub(r"\s+", " ", text)                  # normalize whitespace

        return text

# ----- Tokenization + stopword removal -----
    def tokenize(self, text):
        tokens = text.split()
        filtered = [w for w in tokens if w not in self.stop_words]
        return filtered

# ----- Stemming -----
    def stem_tokens(self, tokens):
        return [self.stemmer.stem(t) for t in tokens]

    def extract_keywords(self, user_input):
        cleaned = self.clean_text(user_input)
        tokens = self.tokenize(cleaned)
        stems = self.stem_tokens(tokens)

        # remove duplicates but preserve original order
        seen = set()
        keywords = []
        for word in stems:
            if word not in seen:
                seen.add(word)
                keywords.append(word)

        return " ".join(keywords) 


class KnowledgeBaseQuery(InferenceEngine):

    def list_conditions(self):
        """
        Display all fact keys (diseases) with index numbers.
        """
        self.index_map = {}   # number -> fact_key

        print("\nAvailable Conditions:\n")
        print(f"[0] Quit")
        for i, key in enumerate(self.kb.facts.keys(), start=1):
            print(f"[{i}] {key}")
            self.index_map[str(i)] = key   # store mapping for later

    def infer(self):
        """
        Ask user to choose a disease number.
        Validate the number.
        Return rules for selected fact key.
        """

        # Ask user
        user_input = input("\nEnter option number: ").strip()   
        
        # Prompt to quit 
        if user_input == '0':
            return None

        # Validate input
        if user_input not in self.index_map:
            print("Invalid option. Please enter a valid number.")
            return None

        # Fetch fact key
        fact_key = self.index_map[user_input]

        # Retrieve rules associated with that fact key
        matched_rules = [
            rule for rule in self.kb.rules
            if rule.get("disease") == fact_key
        ]

        # Prepare response
        result = {
            "option": fact_key,
            "rules": matched_rules,
            "overview": self.kb.facts.get(fact_key, ""),
            "message": "Match found."
        }

        # Clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        return result


class HealthcareQAProgram:
    """
    Class for main Program Interface 
    """

    def __init__(self):
        # KnowledgeBase class
        filepath = "healthcare_disease_dataset.csv"
        self.kb = KnowledgeBase()
        self.kb.load_healthcare_csv(filepath)

        # InferenceEngine class
        self.ie = InferenceEngine(knowledge_base=self.kb)

        # KnowledgeBaseQuery class
        self.kbq = KnowledgeBaseQuery(knowledge_base=self.kb)

        # NLPProcessor class
        self.processor = NLPProcessor()

    def handle_user_input(self):
        """
        Display the class information.
        """
        user_input = input("\nInput: ").strip()

        if user_input.lower().strip() == "quit":
            # Clear terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Goodbye!")
            return 0
        if user_input.lower().strip() == "manual":
            self.kbq.list_conditions()
            answer = self.kbq.infer()
            if answer:
                print(json.dumps(answer, indent=4, ensure_ascii=False))
            return 1

        answer = self.processor.extract_keywords(user_input.lower().strip())
        answer = self.ie.infer(answer)
        if answer['match'] == None:
            print("No conditions found by Inference Engine. Please search manually.")
            self.kbq.list_conditions()
            answer = self.kbq.infer()
            if answer:
                print(json.dumps(answer, indent=4, ensure_ascii=False))
            return 1
        else: 
            print(json.dumps(answer, indent=4, ensure_ascii=False))
            return 1
    # Main program 
    def run(self):
        while True:
            print("\nEnter your symptoms or questions (type 'quit' to exit or 'manual' to search manually):")
            query = self.handle_user_input()
            if not query:
                break 

program = HealthcareQAProgram()
program.run()