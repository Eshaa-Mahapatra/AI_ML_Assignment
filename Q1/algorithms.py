import random
import math

# A* Algorithm for Goal-Oriented Recommendations
def a_star_recommendation(current_mood, goal_mood, content_options):
    path = []
    for content in content_options:
        if content["effect"] == goal_mood:
            path.append(content)
    return path[:3]  # Return top 3 recommendations towards goal

# Hill Climbing for Immediate Recommendation
def hill_climbing_recommendation(current_mood, content_options):
    best_content = None
    for content in content_options:
        if not best_content or abs(content["mood_score"] - current_mood) < abs(best_content["mood_score"] - current_mood):
            best_content = content
    return best_content

# Simulated Annealing for Exploration-Based Recommendation
def simulated_annealing_recommendation(current_mood, content_options, temperature=1.0, cooling_rate=0.01):
    current_content = random.choice(content_options)
    for _ in range(100):
        new_content = random.choice(content_options)
        change_in_mood = abs(new_content["mood_score"] - current_mood) - abs(current_content["mood_score"] - current_mood)
        if change_in_mood < 0 or math.exp(-change_in_mood / temperature) > random.random():
            current_content = new_content
        temperature *= (1 - cooling_rate)
    return current_content

# Constraint Satisfaction for User Preferences
def constraint_satisfaction_recommendation(user_preferences, content_options):
    filtered_content = []
    for content in content_options:
        if all(content.get(pref) == user_preferences.get(pref) for pref in user_preferences):
            filtered_content.append(content)
    return filtered_content[:3]  # Top 3 that meet preferences


# Updated content database with mood associations
content_options = [
    {"title": "Meditation for Calm", "effect": "calm", "link": "https://www.youtube.com/watch?v=66GgM5H7B2I"},
    {"title": "Stress Relief Music", "effect": "relaxed", "link": "https://www.youtube.com/watch?v=ZQfG-0pU9rA"},
    {"title": "Positive Affirmations", "effect": "motivated", "link": "https://www.verywellmind.com/positive-affirmations-2795625"},
    {"title": "Guided Breathing", "effect": "calm", "link": "https://www.youtube.com/watch?v=KJ0y4i4F5bo"},
    {"title": "Self-Compassion Exercise", "effect": "positive", "link": "https://self-compassion.org/exercise.html"},
    {"title": "Understanding Anxiety", "effect": "informed", "link": "https://www.nami.org/Your-Journey/Individuals-with-Mental-Illness/Understanding-Anxiety"},
    {"title": "Journaling Prompts for Reflection", "effect": "calm", "link": "https://journaltherapy.com/journaling-prompts/"},
    {"title": "Inspirational Talks", "effect": "motivated", "link": "https://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action"},
    {"title": "Yoga for Beginners", "effect": "relaxed", "link": "https://www.youtube.com/watch?v=Z2X3qT_V8V0"},
    {"title": "Mindfulness Exercise", "effect": "calm", "link": "https://www.mindful.org/mindfulness-practice/"},
    {"title": "Uplifting Podcast", "effect": "motivated", "link": "https://www.podcastwebsite.com/uplifting"},
    {"title": "Comforting Book Recommendations", "effect": "positive", "link": "https://www.goodreads.com/shelf/show/comfy"},
    {"title": "Inspirational Quotes", "effect": "motivated", "link": "https://www.brainyquote.com/topics/inspirational-quotes"},
    {"title": "Healthy Recipes for Emotional Eating", "effect": "calm", "link": "https://www.eatingwell.com/recipes/20130/mealtimes/quick-healthy/"},
    {"title": "Therapeutic Coloring Pages", "effect": "relaxed", "link": "https://www.coloringpagesforkids.com/"},
]

def recommend_content(mood):
    recommendations = []
    
    # Define mood mapping to content
    mood_to_effect = {
        "sad": ["calm", "positive"],
        "angry": ["relaxed"],
        "happy": ["motivated"],
        "emotional": ["informed", "self-compassion"],
        "loved": ["positive"],
        "excited": ["motivated"],
        "anxious": ["calm"],
        "frustrated": ["relaxed"],
        "lonely": ["connected"],
        "grateful": ["positive", "motivated"],
        "relaxed": ["calm"],
    }

    # Get effects based on mood
    effects = mood_to_effect.get(mood.lower(), [])
    
    # Find recommendations based on effects
    for effect in effects:
        for content in content_options:
            if content['effect'] == effect:
                recommendations.append(content)
    
    # Shuffle the recommendations
    random.shuffle(recommendations)

    # Return up to 3 unique recommendations, ensuring they change each time
    return recommendations[:3] if len(recommendations) >= 3 else recommendations
