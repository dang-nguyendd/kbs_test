#__________ Requirements.txt __________
# annotated-types==0.7.0
# blis==1.3.3
# catalogue==2.0.10
# certifi==2025.11.12
# charset-normalizer==3.4.4
# click==8.3.1
# cloudpathlib==0.23.0
# colorama==0.4.6
# confection==0.1.5
# cymem==2.0.13
# en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl#sha256=1932429db727d4bff3deed6b34cfc05df17794f4a52eeb26cf8928f7c1a0fb85
# idna==3.11
# Jinja2==3.1.6
# MarkupSafe==3.0.3
# murmurhash==1.0.15
# numpy==2.3.5
# packaging==25.0
# preshed==3.0.12
# pydantic==2.12.4
# pydantic_core==2.41.5
# requests==2.32.5
# setuptools==80.9.0
# smart_open==7.5.0
# spacy==3.8.11
# spacy-legacy==3.0.12
# spacy-loggers==1.0.5
# srsly==2.5.2
# thinc==8.3.10
# tqdm==4.67.1
# typer-slim==0.20.0
# typing-inspection==0.4.2
# typing_extensions==4.15.0
# urllib3==2.5.0
# wasabi==1.1.3
# weasel==0.4.3
# wrapt==2.0.1

import spacy

symptom_fact_json = {
  "excessive_sweating": "Excessive sweating is perspiration that is much heavier than normal and unrelated to heat or exercise.",
  "clammy_skin": "Clammy skin means the skin feels cool and moist, often due to sweating.",
  "skin_irritation": "Skin irritation refers to redness, itching, or discomfort caused by inflammation of the skin.",
  "body_odor": "Body odor is the unpleasant smell produced when sweat mixes with bacteria on the skin.",
  "social_discomfort": "Social discomfort means feeling embarrassed or anxious around others because of symptoms.",

  "vaginal_lump": "A vaginal lump is a noticeable swelling or mass near the vaginal opening.",
  "pain_while_walking_or_sitting": "Pain while walking or sitting means discomfort that worsens with movement or pressure.",
  "discomfort_during_intercourse": "Discomfort during intercourse refers to pain or irritation felt during sexual activity.",
  "swelling": "Swelling is an abnormal enlargement of an area of the body due to fluid buildup or inflammation.",
  "redness_if_infected": "Redness if infected indicates that the area turns red when inflammation or infection is present.",

  "spitting_up": "Spitting up is when a baby brings milk or food back up shortly after feeding.",
  "irritability_after_feeding": "Irritability after feeding means a baby becomes fussy or uncomfortable following meals.",
  "coughing": "Coughing is a forceful release of air from the lungs to clear the airway.",
  "poor_feeding": "Poor feeding means a baby is not eating well or has difficulty taking in adequate nutrition.",
  "arching_of_back": "Arching of the back refers to a baby bending backward, often showing discomfort.",

  "painful_lumps": "Painful lumps are tender swellings under the skin that cause discomfort.",
  "skin_abscesses": "Skin abscesses are pockets of pus that form due to infection.",
  "blackheads": "Blackheads are small dark bumps caused by clogged hair follicles.",
  "draining_tunnels": "Draining tunnels are tracts under the skin that leak fluid or pus.",
  "scarring": "Scarring is the formation of thickened or discolored skin after injury or inflammation.",

  "fatigue": "Fatigue is a persistent feeling of tiredness or lack of energy.",
  "frequent_infections": "Frequent infections mean getting illnesses more often than usual due to a weakened immune system.",
  "bruising": "Bruising is discoloration of the skin caused by bleeding under the surface.",
  "nosebleeds": "Nosebleeds involve bleeding from the inside of the nose.",
  "bone_pain": "Bone pain is aching or tenderness felt deep inside the bones.",
  "pale_skin": "Pale skin means the skin appears lighter than usual due to reduced blood flow or anemia.",

  "weakness_in_legs": "Weakness in the legs means reduced strength or difficulty moving the lower limbs.",
  "tingling": "Tingling is a pins-and-needles sensation often caused by nerve irritation.",
  "paralysis": "Paralysis is the loss of the ability to move part of the body.",
  "difficulty_breathing": "Difficulty breathing means feeling short of breath or unable to inhale normally.",
  "loss_of_reflexes": "Loss of reflexes refers to reduced or absent automatic muscle responses.",

  "decreased_urine_output": "Decreased urine output means producing much less urine than normal.",
  "confusion": "Confusion is difficulty thinking clearly, remembering, or making decisions.",
  "nausea": "Nausea is the sensation of wanting to vomit.",

  "fever": "Fever is a higher-than-normal body temperature, usually due to infection.",
  "swollen_lymph_nodes": "Swollen lymph nodes are enlarged glands caused by infection or inflammation.",

  "vomiting": "Vomiting is forcefully expelling stomach contents through the mouth.",
  "diarrhea": "Diarrhea is having loose, watery stools more often than usual.",
  "skin_burns": "Skin burns are injuries to the skin caused by heat, chemicals, or radiation.",
  "hair_loss": "Hair loss refers to unusual or excessive shedding of hair.",

  "recurrent_seizures": "Recurrent seizures are repeated episodes of abnormal brain activity causing convulsions or altered awareness.",
  "memory_issues": "Memory issues involve difficulty remembering information or events.",
  "behavioral_changes": "Behavioral changes are noticeable differences in mood, personality, or actions.",
  "confusion": "Confusion is difficulty thinking clearly or understanding the environment."
}


treatment_fact_json = {
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

advice_fact_json = {
  "hyperhidrosis": "You may start by seeing your primary care provider. You may then be referred to a specialist in diagnosing and treating conditions of the hair and skin (dermatologist). If your condition is not responding to treatment, you may be referred to a specialist in the nervous system (neurologist) or a surgeon.",
  "bartholin_s_cyst": "Your first appointment will likely be with either your primary care provider or a doctor who specializes in conditions that affect women (gynecologist).",
  "infant_reflux": "You may start by seeing your baby's primary healthcare team. Or you may be referred to a specialist in children's digestive diseases, called a pediatric gastroenterologist.",
  "hidradenitis_suppurativa": "You'll likely first see your primary care provider. You might then be referred to a health care provider who specializes in diagnosing and treating skin diseases, also known as a dermatologist. Depending on the severity of your condition, your care also might involve specialists in colorectal surgery, plastic surgery or gastroenterology.",
  "acute_myelogenous_leukemia": "Make an appointment with your healthcare professional if you have symptoms that worry you. You may be referred to a doctor who specializes in blood cell diseases. This type of doctor is called a hematologist.\nAppointments can be brief, and there's a lot of information to discuss. It's a good idea to be prepared. Here's some information to help you get ready:",
  "guillain_barre_syndrome": "You may be referred to a doctor who specializes in disorders of the brain and nervous system, known as a neurologist.",
  "acute_kidney_injury": "Most people are in a hospital when they get acute kidney injury. If you aren't in the hospital and have symptoms of kidney failure, make an appointment with your family healthcare professional right away. You may be referred to a specialist in kidney disease, called a nephrologist.\nBefore your appointment, write down questions. Consider asking:\nWhat's the most likely cause of my symptoms?\nHave my kidneys stopped working? What could have caused my kidney failure?\nWhat tests do I need?\nWhat are my treatment choices, and what are the risks?\nDo I need to go to the hospital?\nWill my kidneys recover or will I need dialysis?\nI have other health conditions. How can I best manage these conditions together?\nDo I need to eat a special diet? If so, can you refer me to a dietitian to help me plan what to eat?\nDo you have printed materials about acute kidney injury that I can have? What websites do you suggest?",
  "acute_lymphocytic_leukemia": "Make an appointment with your family doctor if you or your child has signs and symptoms that worry you. If your doctor suspects acute lymphocytic leukemia, you'll likely be referred to a doctor who specializes in treating diseases and conditions of the blood and bone marrow (hematologist).\nBecause appointments can be brief, and because there's often a lot of information to discuss, it's a good idea to be prepared. Here's some information to help you get ready, and what to expect from the doctor.",
  "radiation_sickness": "If your symptoms are serious, you might need emergency medical care. \nIf your symptoms are less serious, you may start by seeing your healthcare professional. Or you may be referred right away to a doctor who specializes in nervous system conditions, known as a neurologist.",
  "acute_sinusitis": "If your symptoms are serious, you might need emergency medical care. \nIf your symptoms are less serious, you may start by seeing your healthcare professional. Or you may be referred right away to a doctor who specializes in nervous system conditions, known as a neurologist."
}

rules_json = [
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




#__________ KNOWLEDGE BASE __________

class KnowledgeBase:
    def __init__(self):
        self.domain_knowledge = {}     # treatments, advice, descriptions
        self.inference_rules = []      # symptom → condition rules

    def load_domain_knowledge(self, knowledge):
        self.domain_knowledge.update(knowledge)

    def load_inference_rules(self, rules):
        self.inference_rules.extend(rules)


#__________ INFERENCE ENGINE __________

class InferenceEngine:
    def __init__(self, kb):
        self.kb = kb

    def infer(self, user_entities: dict):
        diagnoses = []
        for rule in self.kb.inference_rules:
            if self.apply_rule(rule, user_entities):
                diagnoses.append(rule["id"])
        return diagnoses

    def apply_rule(self, rule, user_entities, threshold=0.5):
        conditions = rule["conditions"]
        matches = 0

        for cond in conditions:
            if self.check_condition(cond, user_entities):
                matches += 1

        match_ratio = matches / len(conditions)
        return match_ratio >= threshold


    def check_condition(self, condition, user_entities):
        key = condition["attribute"]
        expected = condition["value"]
        if key not in user_entities:
            return False
        return user_entities[key] == expected


#__________ NLP PROCESSOR __________

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.has_ner = True

        # map wording → symptom key
        self.symptom_map = {
            "sweat": "excessive_sweating",
            "clammy": "clammy_skin",
            "odor": "body_odor",
            "irritation": "skin_irritation",
            "social": "social_discomfort",

            "vaginal lump": "vaginal_lump",
            "intercourse": "discomfort_during_intercourse",
            "walk": "pain_while_walking_or_sitting",
            "sit": "pain_while_walking_or_sitting",
            "swell": "swelling",
            "redness": "redness_if_infected",

            "spit": "spitting_up",
            "vomit": "vomiting",
            "irritable": "irritability_after_feeding",
            "cough": "coughing",
            "feed": "poor_feeding",
            "arch": "arching_of_back",

            "lump": "painful_lumps",
            "blackhead": "blackheads",
            "abscess": "skin_abscesses",
            "tunnel": "draining_tunnels",
            "scar": "scarring",

            "fatigue": "fatigue",
            "infection": "frequent_infections",
            "bruise": "bruising",
            "nosebleed": "nosebleeds",
            "bone pain": "bone_pain",
            "pale": "pale_skin",

            "tingle": "tingling",
            "weak": "weakness_in_legs",
            "paralysis": "paralysis",
            "breath": "difficulty_breathing",
            "reflex": "loss_of_reflexes",

            "urine": "decreased_urine_output",
            "confuse": "confusion",
            "nausea": "nausea",

            "fever": "fever",
            "lymph": "swollen_lymph_nodes",

            "diarrhea": "diarrhea",
            "burn": "skin_burns",
            "hair loss": "hair_loss",

            "seizure": "recurrent_seizures",
            "memory": "memory_issues",
            "behavior": "behavioral_changes",
        }

    def process_query(self, text):

        text = text.lower()
        doc = self.nlp(text)

        entities = {}

        for token in doc:
            lemma = token.lemma_
            if lemma in self.symptom_map:
                key = self.symptom_map[lemma]
                entities[key] = True

        intent = "symptoms"
        return {"intent": intent, "entities": entities}


#__________ KNOWLEDGE BASE QUERY __________

class KnowledgeBaseQuery:
    """Return domain symptom when no rule fires."""
    def __init__(self, symptom_dict):
        self.symptom = symptom_dict

    def lookup(self, entities: dict):
        hits = []
        for key in entities:
          # Find any symptom key that contains the rule ID
          for condition in self.symptom:
              if condition.startswith(key.split("_")[0]): 
                  hits.append(self.symptom[condition])

        if not hits:
            hits.append("No diagnosis matched. Please provide more symptoms.")

        return hits


#__________ MAIN INTERFACE __________
class HealthcareQAProgram:
    """
    Class for main Program Interface 
    """
    def __init__(self):
        self.kb = KnowledgeBase()
        self.nlp = NLPProcessor()

    def build_kb(self, treatment_fact, advice_fact, symptom_fact, rules):
        self.kb = KnowledgeBase()

        # Merge treatments + advice facts
        merged = {}
        for cond, text in treatment_fact.items():
            merged[f"{cond}_treatment"] = text
        for cond, text in advice_fact.items():
            merged[f"{cond}_advice"] = text
        for cond, text in symptom_fact.items():
            merged[f"{cond}_symptom"] = text

        self.kb.load_domain_knowledge(merged)
        self.kb.load_inference_rules(rules)

        return self.kb

    def handle_user_input(self, text):
        structured = self.nlp.process_query(text)

        diagnoses = InferenceEngine(self.kb).infer(structured["entities"])

        if diagnoses:
          diagnosis = diagnoses[0]

          treatment = self.kb.domain_knowledge.get(f"{diagnosis}_treatment", "No treatment info.")
          advice = self.kb.domain_knowledge.get(f"{diagnosis}_advice", "No advice info.")

          print("\n--- RESULT ---")
          print("Structured input:", structured)
          print("Diagnosis:", diagnosis)
          print("Treatment:", treatment)
          print("Advice:", advice)
          print()
        else:
            # Fallback
            fallback = KnowledgeBaseQuery(self.kb.domain_knowledge).lookup(structured["entities"])

            print("\n--- RESULT ---")
            print("Structured input:", structured)
            print("Diagnosis: None found")
            print("Symptom Explanation:")
            for a in fallback:
                print(" -", a)
            print()


    # Main program 
    def run(self):
        treatment_fact = treatment_fact_json
        advice_fact = advice_fact_json
        symptom_fact = symptom_fact_json
        rules = rules_json

        self.build_kb(treatment_fact, advice_fact, symptom_fact, rules)

        print("Medical Diagnosis Knowledge-Based System")
        print("Describe your symptoms (type 'quit' to exit).")

        while True:
            user = input("> ").strip()
            if user in ("quit", "exit"):
                break
            self.handle_user_input(user)


if __name__ == "__main__":
    program = HealthcareQAProgram()
    program.run()


