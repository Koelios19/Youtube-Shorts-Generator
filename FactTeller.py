import randfacts
from elevenlabs import generate, set_api_key, save

api_key = 'e132a5a85840348b1ae6ec404e274ce2'
# This is the Eleven Labs API key. If it ever expires grab one at https://elevenlabs.io/api
set_api_key(api_key)



def generate_fact():
    x = randfacts.get_fact()
    return x


def generate_facts():
    facts = "fun facts i bet you didn't even know "
    while True:
        fact = generate_fact()
        fact = remove_ponctuation_and_caps_of(fact)
        if theres_space_for_another(fact, facts):
            facts += fact
        else:
            break
    print("Step 2: Generating Audio...")
    return facts


def generate_audio():
    audio = generate(
        text=generate_facts(),
        voice="Adam",
        model="eleven_monolingual_v1"
    )
    save(audio, "facts.mp3")


def theres_space_for_another(fact, facts):
    return len(facts.split(" ")) + len(fact.split(" ")) < 270


def remove_ponctuation_and_caps_of(fact):
    fact.replace(",", "").replace(".", "").replace("!", "").replace(":", "").replace("?", "").lower()
    return fact
