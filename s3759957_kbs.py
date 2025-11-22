import csv
import re
import difflib
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import os
import json


treatment_fact = {
  "hyperhidrosis": "Treating hyperhidrosis may start with treating the condition causing it. If a cause isn't found, treatment focuses on controlling heavy sweating. If new self-care habits don't improve your symptoms, your health care provider may suggest one or more of the following treatments. Even if your sweating improves after treatment, it may recur.",
  "bartholin_s_cyst": "Often a Bartholin's cyst requires no treatments especially if the cyst causes no signs or symptoms. When needed, treatment depends on the size of the cyst, your discomfort level and whether it's infected, which can result in an abscess.\n\nTreatment options your doctor may recommend include:\n\nSurgical drainage.You may need surgery to drain a cyst that's infected or very large. Drainage of a cyst can be done using local anesthesia or sedation.\n\nFor the procedure, your doctor makes a small incision in the cyst, allows it to drain, and then places a small rubber tube (catheter) in the incision. The catheter stays in place for up to six weeks to keep the incision open and allow complete drainage.\n\nRarely, for persistent cysts that aren't effectively treated by the above procedures, your doctor may recommend surgery to remove the Bartholin's gland. Surgical removal is usually done in a hospital under general anesthesia. Surgical removal of the gland carries a greater risk of bleeding or complications after the procedure.",
  "infant_reflux": "For most babies, making some changes to feeding eases infant reflux until it gets better on its own.",
  "hidradenitis_suppurativa": "Treatment with medicines, surgery or both can help control symptoms and prevent complications of hidradenitis suppurativa. Talk with your health care provider about the risks and benefits of the treatment options and how to develop an approach that's right for you.\nExpect to have regular follow-up visits with your dermatologist. Some people might need the comprehensive care provided by a health care team with members from multiple medical specialties.",
  "acute_myelogenous_leukemia": "Many types of treatment exist for acute myelogenous leukemia, also called AML. Treatment depends on several factors, including the subtype of the disease, your age, your overall health, your prognosis and your preferences.\nTreatment usually has two phases:\nRemission induction therapy.This first phase aims to kill the leukemia cells in your blood and bone marrow. But it doesn't usually destroy all the leukemia cells. You will need further treatment to keep the disease from coming back.\nConsolidation therapy.This phase also is called post-remission therapy or maintenance therapy. It aims to kill the remaining leukemia cells. Consolidation therapy is crucial to helping lower the risk of relapse.\nTreatments include:\nChemotherapy.Chemotherapy treats cancer with strong medicines. Most chemotherapy medicines are given through a vein. Some come in pill form. Chemotherapy is the main type of remission induction therapy. It also may be used for consolidation therapy.\nPeople with AML usually stay in the hospital during chemotherapy treatments because the medicines kill many healthy blood cells while destroying leukemia cells. If the first chemotherapy cycle doesn't cause remission, it can be repeated.\nSide effects of chemotherapy depend on the medicines you're given. Common side effects are nausea and hair loss. Serious, long-term complications may include heart disease, lung damage, fertility problems and other cancers.\nTargeted therapy.Targeted therapy for cancer is a treatment that uses medicines that attack specific chemicals in the cancer cells. By blocking these chemicals, targeted treatments can cause cancer cells to die. Your leukemia cells will be tested to see if targeted therapy may be helpful for you. Targeted therapy may be used alone or in combination with chemotherapy during induction therapy.\nBone marrow transplant.A bone marrow transplant, also called a bone marrow stem cell transplant, involves putting healthy bone marrow stem cells into the body. These cells replace cells hurt by chemotherapy and other treatments. A bone marrow stem cell transplant may be used for both remission induction and consolidation therapy.\nBefore a bone marrow transplant, you receive very high doses of chemotherapy or radiation therapy to destroy your leukemia-producing bone marrow. Then you receive infusions of stem cells from a compatible donor. This is called an allogeneic transplant.\nThere is an increased risk of infection after a transplant.\nClinical trials.Some people with leukemia choose to enroll in clinical trials to try experimental treatments or new combinations of known therapies.",
  "guillain_barre_syndrome": "There's no cure for Guillain-Barre syndrome. But two types of treatments can speed recovery and reduce symptoms:\nPlasma exchange, also known as plasmapheresis.Plasma is the liquid portion of part of your blood. In a plasma exchange, plasma is removed and separated from your blood cells. The blood cells are then put back into your body, which makes more plasma to replace what was removed. Plasmapheresis may work by ridding plasma of certain antibodies that contribute to the immune system's attack on the peripheral nerves.\nImmunoglobulin therapy.Immunoglobulin containing healthy antibodies from blood donors is given through a vein. High doses of immunoglobulin can block the damaging antibodies that may contribute to Guillain-Barre syndrome.\nThese treatments are equally effective. Mixing them or using one after the other is no more effective than using either method alone.\nYou are also likely to be given medicine to:\nRelieve pain, which can be severe.\nPrevent blood clots, which can develop if you're not mobile.\nPeople with Guillain-Barre syndrome need physical help and therapy before and during recovery. Your care may include:\nMovement of your arms and legs by caregivers before recovery, to help keep your muscles flexible and strong.\nPhysical therapy during recovery to help you cope with fatigue and regain strength and proper movement.\nTraining with adaptive devices, such as a wheelchair or braces, to give you mobility and self-care skills.",
  "acute_kidney_injury": "Treatment for acute kidney injury most often means a hospital stay. Most people with acute kidney injury are already in the hospital. How long you'll stay in the hospital depends on the reason for your acute kidney injury and how quickly your kidneys recover.",
  "acute_lymphocytic_leukemia": "In general, treatment for acute lymphocytic leukemia falls into separate phases:\nInduction therapy.The purpose of the first phase of treatment is to kill most of the leukemia cells in the blood and bone marrow and to restore normal blood cell production.\nConsolidation therapy.Also called post-remission therapy, this phase of treatment is aimed at destroying any remaining leukemia in the body.\nMaintenance therapy.The third phase of treatment prevents leukemia cells from regrowing. The treatments used in this stage are usually given at much lower doses over a long period of time, often years.\nPreventive treatment to the spinal cord.During each phase of therapy, people with acute lymphocytic leukemia may receive additional treatment to kill leukemia cells located in the central nervous system. In this type of treatment, chemotherapy drugs are often injected directly into the fluid that covers the spinal cord.\nDepending on your situation, the phases of treatment for acute lymphocytic leukemia can span two to three years.\nTreatments may include:\nChemotherapy.Chemotherapy, which uses drugs to kill cancer cells, is typically used as an induction therapy for children and adults with acute lymphocytic leukemia. Chemotherapy drugs can also be used in the consolidation and maintenance phases.\nTargeted therapy.Targeted drug treatments focus on specific abnormalities present within cancer cells. By blocking these abnormalities, targeted drug treatments can cause cancer cells to die. Your leukemia cells will be tested to see if targeted therapy may be helpful for you. Targeted therapy can be used alone or in combination with chemotherapy for induction therapy, consolidation therapy or maintenance therapy.\nRadiation therapy.Radiation therapy uses high-powered beams, such as X-rays or protons, to kill cancer cells. If the cancer cells have spread to the central nervous system, your doctor may recommend radiation therapy.\nBone marrow transplant.A bone marrow transplant, also known as a stem cell transplant, may be used as consolidation therapy or for treating relapse if it occurs. This procedure allows someone with leukemia to reestablish healthy bone marrow by replacing leukemic bone marrow with leukemia-free marrow from a healthy person.A bone marrow transplant begins with high doses of chemotherapy or radiation to destroy any leukemia-producing bone marrow. The marrow is then replaced by bone marrow from a compatible donor (allogeneic transplant).\nEngineering immune cells to fight leukemia.A specialized treatment called chimeric antigen receptor (CAR)-T cell therapy takes your body's germ-fighting T cells, engineers them to fight cancer and infuses them back into your body.CAR-T cell therapy might be an option for children and young adults. It might be used for consolidation therapy or for treating relapse.\nClinical trials.Clinical trials are experiments to test new cancer treatments and new ways of using existing treatments. While clinical trials give you or your child a chance to try the latest cancer treatment, the benefits and risks of the treatment may be uncertain. Discuss the benefits and risks of clinical trials with your doctor.",
  "radiation_sickness": "The treatment goals for radiation sickness are to prevent further radioactive contamination; treat life-threatening injuries, such as from burns and trauma; reduce symptoms; and manage pain.",
  "acute_sinusitis": "Most cases of acute sinusitis get better on their own. Self-care is usually all that's needed to ease symptoms."
}

advice_fact = {
  "hyperhidrosis": "You may start by seeing your primary care provider. You may then be referred to a specialist in diagnosing and treating conditions of the hair and skin (dermatologist). If your condition is not responding to treatment, you may be referred to a specialist in the nervous system (neurologist) or a surgeon.\nHere's some information to help you get ready for your appointment.",
  "bartholin_s_cyst": "Your first appointment will likely be with either your primary care provider or a doctor who specializes in conditions that affect women (gynecologist).",
  "infant_reflux": "You may start by seeing your baby's primary healthcare team. Or you may be referred to a specialist in children's digestive diseases, called a pediatric gastroenterologist.",
  "hidradenitis_suppurativa": "You'll likely first see your primary care provider. You might then be referred to a health care provider who specializes in diagnosing and treating skin diseases, also known as a dermatologist. Depending on the severity of your condition, your care also might involve specialists in colorectal surgery, plastic surgery or gastroenterology.\nHere's some information to help you get ready for your appointment.",
  "acute_myelogenous_leukemia": "Make an appointment with your healthcare professional if you have symptoms that worry you. You may be referred to a doctor who specializes in blood cell diseases. This type of doctor is called a hematologist.\nAppointments can be brief, and there's a lot of information to discuss. It's a good idea to be prepared. Here's some information to help you get ready:",
  "guillain_barre_syndrome": "You may be referred to a doctor who specializes in disorders of the brain and nervous system, known as a neurologist.",
  "acute_kidney_injury": "Most people are in a hospital when they get acute kidney injury. If you aren't in the hospital and have symptoms of kidney failure, make an appointment with your family healthcare professional right away. You may be referred to a specialist in kidney disease, called a nephrologist.\nBefore your appointment, write down questions. Consider asking:\nWhat's the most likely cause of my symptoms?\nHave my kidneys stopped working? What could have caused my kidney failure?\nWhat tests do I need?\nWhat are my treatment choices, and what are the risks?\nDo I need to go to the hospital?\nWill my kidneys recover or will I need dialysis?\nI have other health conditions. How can I best manage these conditions together?\nDo I need to eat a special diet? If so, can you refer me to a dietitian to help me plan what to eat?\nDo you have printed materials about acute kidney injury that I can have? What websites do you suggest?",
  "acute_lymphocytic_leukemia": "Make an appointment with your family doctor if you or your child has signs and symptoms that worry you. If your doctor suspects acute lymphocytic leukemia, you'll likely be referred to a doctor who specializes in treating diseases and conditions of the blood and bone marrow (hematologist).\nBecause appointments can be brief, and because there's often a lot of information to discuss, it's a good idea to be prepared. Here's some information to help you get ready, and what to expect from the doctor.",
  "radiation_sickness": "If your symptoms are serious, you might need emergency medical care. \nIf your symptoms are less serious, you may start by seeing your healthcare professional. Or you may be referred right away to a doctor who specializes in nervous system conditions, known as a neurologist.",
  "acute_sinusitis": "If your symptoms are serious, you might need emergency medical care. \nIf your symptoms are less serious, you may start by seeing your healthcare professional. Or you may be referred right away to a doctor who specializes in nervous system conditions, known as a neurologist."
}

rules = [
  {
    "id": "hyperhidrosis",
    "conditions": [
      {"attribute": "excessive_sweating", "op": "eq", "value": True},
      {"attribute": "clammy_skin", "op": "eq", "value": True},
      {"attribute": "skin_irritation", "op": "eq", "value": True},
      {"attribute": "body_odor", "op": "eq", "value": True},
      {"attribute": "social_discomfort", "op": "eq", "value": True}
    ],
    "conclusion": "Hyperhidrosis causes excessive sweating unrelated to heat or exercise. It can disrupt daily life and cause social anxiety. Treatments include antiperspirants, medications, therapies, and in severe cases surgery. Sometimes an underlying condition may be involved."
  },
  {
    "id": "bartholin_cyst",
    "conditions": [
      {"attribute": "vaginal_lump", "op": "eq", "value": True},
      {"attribute": "pain_while_walking_or_sitting", "op": "eq", "value": True},
      {"attribute": "discomfort_during_intercourse", "op": "eq", "value": True},
      {"attribute": "swelling", "op": "eq", "value": True},
      {"attribute": "redness_if_infected", "op": "eq", "value": True}
    ],
    "conclusion": "A Bartholin's cyst forms when the duct of the Bartholin gland becomes blocked, leading to swelling. If infected, it can form an abscess. Treatment ranges from home care to surgical drainage and antibiotics."
  },
  {
    "id": "infant_reflux",
    "conditions": [
      {"attribute": "spitting_up", "op": "eq", "value": True},
      {"attribute": "irritability_after_feeding", "op": "eq", "value": True},
      {"attribute": "coughing", "op": "eq", "value": True},
      {"attribute": "poor_feeding", "op": "eq", "value": True},
      {"attribute": "arching_of_back", "op": "eq", "value": True}
    ],
    "conclusion": "Infant reflux occurs when stomach contents flow back into the esophagus. It's common and usually harmless if growth is normal. Persistent or severe cases may indicate GERD, allergies, or digestive blockage."
  },
  {
    "id": "hidradenitis_suppurativa",
    "conditions": [
      {"attribute": "painful_lumps", "op": "eq", "value": True},
      {"attribute": "skin_abscesses", "op": "eq", "value": True},
      {"attribute": "blackheads", "op": "eq", "value": True},
      {"attribute": "draining_tunnels", "op": "eq", "value": True},
      {"attribute": "scarring", "op": "eq", "value": True}
    ],
    "conclusion": "Hidradenitis suppurativa causes painful lumps in areas where skin rubs together. It is chronic, recurrent, and may worsen over time. Combined medical and surgical therapy can help manage symptoms and prevent complications."
  },
  {
    "id": "acute_myelogenous_leukemia",
    "conditions": [
      {"attribute": "fatigue", "op": "eq", "value": True},
      {"attribute": "frequent_infections", "op": "eq", "value": True},
      {"attribute": "bruising", "op": "eq", "value": True},
      {"attribute": "nosebleeds", "op": "eq", "value": True},
      {"attribute": "bone_pain", "op": "eq", "value": True},
      {"attribute": "pale_skin", "op": "eq", "value": True}
    ],
    "conclusion": "Acute myelogenous leukemia is a rapidly progressing cancer of the blood and bone marrow that affects myeloid cells. It is the most common acute leukemia in adults and requires urgent treatment."
  },
  {
    "id": "guillain_barre_syndrome",
    "conditions": [
      {"attribute": "weakness_in_legs", "op": "eq", "value": True},
      {"attribute": "tingling", "op": "eq", "value": True},
      {"attribute": "paralysis", "op": "eq", "value": True},
      {"attribute": "difficulty_breathing", "op": "eq", "value": True},
      {"attribute": "loss_of_reflexes", "op": "eq", "value": True}
    ],
    "conclusion": "Guillain-Barre syndrome occurs when the immune system attacks the nerves, causing progressive weakness that can lead to paralysis. It is a medical emergency requiring hospital treatment. Most people recover, though recovery may take months to years."
  },
  {
    "id": "acute_kidney_injury",
    "conditions": [
      {"attribute": "decreased_urine_output", "op": "eq", "value": True},
      {"attribute": "swelling", "op": "eq", "value": True},
      {"attribute": "fatigue", "op": "eq", "value": True},
      {"attribute": "confusion", "op": "eq", "value": True},
      {"attribute": "nausea", "op": "eq", "value": True}
    ],
    "conclusion": "Acute kidney injury occurs when the kidneys suddenly fail to filter waste from the blood. Severity ranges from mild to life-threatening, but the condition can be reversible with prompt treatment."
  },
  {
    "id": "acute_lymphocytic_leukemia",
    "conditions": [
      {"attribute": "fever", "op": "eq", "value": True},
      {"attribute": "bone_pain", "op": "eq", "value": True},
      {"attribute": "bruising", "op": "eq", "value": True},
      {"attribute": "swollen_lymph_nodes", "op": "eq", "value": True},
      {"attribute": "fatigue", "op": "eq", "value": True},
      {"attribute": "frequent_infections", "op": "eq", "value": True}
    ],
    "conclusion": "Acute lymphocytic leukemia is a fast-progressing cancer of lymphocyte-producing bone marrow cells. It is the most common cancer in children and highly treatable, though adult outcomes are less favorable."
  },
  {
    "id": "radiation_sickness",
    "conditions": [
      {"attribute": "nausea", "op": "eq", "value": True},
      {"attribute": "vomiting", "op": "eq", "value": True},
      {"attribute": "diarrhea", "op": "eq", "value": True},
      {"attribute": "skin_burns", "op": "eq", "value": True},
      {"attribute": "fatigue", "op": "eq", "value": True},
      {"attribute": "hair_loss", "op": "eq", "value": True}
    ],
    "conclusion": "Radiation sickness is caused by high-dose radiation exposure over a short time. Severity depends on absorbed dose. It is rare and often fatal, usually associated with nuclear accidents."
  },
  {
    "id": "autoimmune_epilepsy",
    "conditions": [
      {"attribute": "recurrent_seizures", "op": "eq", "value": True},
      {"attribute": "memory_issues", "op": "eq", "value": True},
      {"attribute": "behavioral_changes", "op": "eq", "value": True},
      {"attribute": "confusion", "op": "eq", "value": True}
    ],
    "conclusion": "Autoimmune epilepsy occurs when antibodies mistakenly attack the brain, causing seizures that often do not respond to typical antiseizure medications. Early immunotherapy can reduce inflammation and improve outcomes."
  }
]




class KnowledgeBase:
    """
    A class that holds a dictionary of facts and a list of rule dictionaries.
    """

    def __init__(self, facts=None, rules=None):
        self.facts = facts if facts is not None else {}
        self.rules = rules if rules is not None else []


    def load_csv_kbs(self, filepath, limit=14):
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
            # Disease, Treatment, Overview, Symptoms, Preparing_for_your_appointment

            disease = row.get("Disease", "")
            keywords = row.get("Symptoms", "")

            key = f"{disease}, {keywords}".strip()

            # ----- FACTS -----
            facts[key] = row.get("Overview", "")

            # ----- RULES -----
            rule = {
                "Disease": key,
                "Value": True,
                "Symptoms": row.get("Symptoms", ""),
                "Treatment": row.get("Treatment", ""),
                "Preparing for your appointment": row.get("Preparing for your appointment", ""),
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

        if best_key is None or score <= 20:
            return {
                "match": None,
                "score": 0,
                "rules": [],
                "message": "No relevant information found."
            }

        # Get matching rules
        matched_rules = [
            rule for rule in self.kb.rules 
            if rule.get("Disease") == best_key
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
            if rule.get("Disease") == fact_key
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