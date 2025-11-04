import csv

def load_csv_sample(filepath, limit=10):
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


# Example usage
if __name__ == "__main__":
    filepath = "healthcare_disease_dataset.csv"  # 👈 replace with your actual CSV file path
    records = load_csv_sample(filepath)

    print(f"Loaded {len(records)} records.")
    # Print first few records for inspection
    for i, rec in enumerate(records[:3], start=1):
        print(f"{i}: {rec}")



class KnowledgeBase:
    """
    A class that holds a dictionary of facts and a list of rule dictionaries.
    """

    def __init__(self, facts=None, rules=None):
        """
        Initialize the class with a dictionary and a list of dictionaries.

        :param facts: A dictionary (default: empty dict)
        :param rules: A list of dictionaries (default: empty list)
        """
        self.facts = facts if facts is not None else {}
        self.rules = rules if rules is not None else []

    # --------------------------
    # Basic getter methods
    # --------------------------

    def get_all(self):
        """
        Get all facts and rules.
        :return: A tuple (facts, rules)
        """
        return self.facts, self.rules

    def get_fact(self, key):
        """
        Get a fact by its key.
        :param key: The key to look up in the facts dictionary.
        :return: The value if key exists, else None.
        """
        return self.facts.get(key)

    def get_rule_by_key(self, key, value):
        """
        Find rules (dicts) in the rules list where a given key matches a value.
        :param key: Key to search in each rule dictionary.
        :param value: Value to match.
        :return: List of matching rule dictionaries.
        """
        return [rule for rule in self.rules if rule.get(key) == value]

    # --------------------------
    # Setter / Updater methods
    # --------------------------

    def set_fact(self, key, value):
        """
        Add or update a fact in the facts dictionary.
        """
        self.facts[key] = value

    def add_rule(self, rule_dict):
        """
        Add a new rule (dictionary) to the rules list.
        :param rule_dict: A dictionary representing a rule.
        """
        if isinstance(rule_dict, dict):
            self.rules.append(rule_dict)
        else:
            raise TypeError("rule_dict must be a dictionary")

    # --------------------------
    # Display utility
    # --------------------------

    def display(self):
        """
        Print the contents of facts and rules in a readable format.
        """
        print("Facts:")
        for key, value in self.facts.items():
            print(f"  {key}: {value}")

        print("\nRules:")
        for i, rule in enumerate(self.rules, 1):
            print(f"  {i}: {rule}")


class InferenceEngine:
    """
    A simple example class.
    Describe what this class does here.
    """

    def __init__(self, name, value):
        """
        Initialize the class with attributes.
        :param name: A string representing the name.
        :param value: A value to store.
        """
        self.name = name
        self.value = value

    def display_info(self):
        """
        Display the class information.
        """
        print(f"Name: {self.name}, Value: {self.value}")

    def update_value(self, new_value):
        """
        Update the stored value.
        :param new_value: The new value to assign.
        """
        self.value = new_value
        print(f"Value updated to: {self.value}")

class NLPProcessor:
    """
    A simple example class.
    Describe what this class does here.
    """

    def __init__(self, name, value):
        """
        Initialize the class with attributes.
        :param name: A string representing the name.
        :param value: A value to store.
        """
        self.name = name
        self.value = value

    def display_info(self):
        """
        Display the class information.
        """
        print(f"Name: {self.name}, Value: {self.value}")

    def update_value(self, new_value):
        """
        Update the stored value.
        :param new_value: The new value to assign.
        """
        self.value = new_value
        print(f"Value updated to: {self.value}")

class KnowledgeBaseQuery:
    """
    A simple example class.
    Describe what this class does here.
    """

    def __init__(self, name, value):
        """
        Initialize the class with attributes.
        :param name: A string representing the name.
        :param value: A value to store.
        """
        self.name = name
        self.value = value

    def display_info(self):
        """
        Display the class information.
        """
        print(f"Name: {self.name}, Value: {self.value}")

    def update_value(self, new_value):
        """
        Update the stored value.
        :param new_value: The new value to assign.
        """
        self.value = new_value
        print(f"Value updated to: {self.value}")

class UserInput:
    """
    A simple example class.
    Describe what this class does here.
    """

    def __init__(self, name, value):
        """
        Initialize the class with attributes.
        :param name: A string representing the name.
        :param value: A value to store.
        """
        self.name = name
        self.value = value

    def handle_user_input(self):
        """
        Display the class information.
        """
        print(f"Name: {self.name}, Value: {self.value}")

    def update_value(self, new_value):
        """
        Update the stored value.
        :param new_value: The new value to assign.
        """
        self.value = new_value
        print(f"Value updated to: {self.value}")
