import wikipedia
import time
import re

def get_description(food_name, retries=3, delay=1, max_delay=5, attempt=0):
    """
    ~ Shamar
    Fetches a brief description of the food from Wikipedia with retries and automatic synonym handling.
    """
    error_messages = [
        "Request timed out. Please try again later.",
        "Redirect error encountered.",
        "No description available for this food.",
        "An error occurred. Please try again."
    ]

    try:
        summary = wikipedia.summary(food_name, sentences=1)
        return summary

    except wikipedia.exceptions.DisambiguationError as e:
        options = ", ".join(e.options[:5])
        return f"Multiple results found: {options}"

    except wikipedia.exceptions.HTTPTimeoutError:
        if attempt < retries:
            time.sleep(delay)
            delay = min(delay * 2, max_delay)
            return get_description(food_name, retries, delay, max_delay, attempt + 1)
        else:
            return error_messages[0]

    except wikipedia.exceptions.RedirectError:
        return error_messages[1]

    except wikipedia.exceptions.PageError:
        if attempt < retries:
            variations = generate_name_variations(food_name)
            for variation in variations:
                try:
                    summary = wikipedia.summary(variation, sentences=1)
                    return f"Using variation '{variation}': {summary}"
                except wikipedia.exceptions.PageError:
                    continue
            return get_description(food_name, retries, delay, max_delay, attempt + 1)
        else:
            return error_messages[2]

    except Exception as e:
        if attempt < retries:
            time.sleep(delay)
            delay = min(delay * 2, max_delay)
            return get_description(food_name, retries, delay, max_delay, attempt + 1)
        else:
            return f"{error_messages[3]} Error: {str(e)}"


def generate_name_variations(food_name):
    """
    ~ Aaron
    Generates common variations of the food name.
    """
    variations = [food_name, food_name.lower(), food_name.title()]
    plural_food_name = re.sub(r"(\w+)$", r"\1s", food_name)
    variations.append(plural_food_name)

    food_name_parts = food_name.split("&")
    if len(food_name_parts) == 2:
        variations.append(food_name_parts[0].strip() + " and " + food_name_parts[1].strip())

    random_variations = [
        food_name.replace(" ", "_"),
        food_name.replace("&", "and")
    ]

    variations.extend(random_variations)
    return variations
