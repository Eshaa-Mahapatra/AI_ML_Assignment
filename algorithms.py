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
    {"title": "Meditation for Calm", "effect": "calm", "mood_score": 1, "type": "video", "link": "https://example.com/meditation", "description": "A guided meditation to help you find calmness and peace."},
    {"title": "Stress Relief Music", "effect": "relaxed", "mood_score": 2, "type": "audio", "link": "https://example.com/music", "description": "Soothing music to relieve stress and anxiety."},
    {"title": "Positive Affirmations", "effect": "motivated", "mood_score": 3, "type": "text", "link": "https://example.com/affirmations", "description": "Daily affirmations to boost your self-esteem and motivation."},
    {"title": "Guided Breathing", "effect": "calm", "mood_score": 1, "type": "video", "link": "https://example.com/breathing", "description": "Learn breathing techniques to calm your mind."},
    {"title": "Self-Compassion Exercise", "effect": "positive", "mood_score": 4, "type": "text", "link": "https://example.com/self-compassion", "description": "An exercise to foster self-kindness and compassion."},
    {"title": "Understanding Anxiety", "effect": "informed", "mood_score": 3, "type": "article", "link": "https://example.com/anxiety", "description": "Read about anxiety to better understand your feelings."},
    {"title": "Journaling Prompts for Reflection", "effect": "calm", "mood_score": 2, "type": "text", "link": "https://example.com/journaling-prompts", "description": "Prompts to help you reflect and process your emotions."},
    {"title": "Inspirational Talks", "effect": "motivated", "mood_score": 5, "type": "video", "link": "https://example.com/inspirational-talks", "description": "Watch talks that inspire you to take action."},
    {"title": "Yoga for Beginners", "effect": "relaxed", "mood_score": 2, "type": "video", "link": "https://example.com/yoga", "description": "A beginner's guide to yoga for relaxation and mindfulness."},
]


def recommend_content(mood):
    recommendations = []
    
    # Define mood mapping to content
    mood_to_effect = {
        "sad": ["calm", "positive"],
        "angry": ["relaxed"],
        "happy": ["motivated"],
        "emotional": ["informed", "self-compassion"],
        "loving": ["positive"],
    }

    # Get effects based on mood
    effects = mood_to_effect.get(mood.lower(), [])
    
    # Find recommendations based on effects
    for effect in effects:
        for content in content_options:
            if content['effect'] == effect:
                recommendations.append(content)

    return recommendations

