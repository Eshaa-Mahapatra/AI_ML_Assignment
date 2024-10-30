from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Expanded content for each mood
content_database = {
    "happy": [
        {"title": "10 Ways to Boost Your Happiness", "link": "https://example.com/happy1"},
        {"title": "The Science of Happiness", "link": "https://example.com/happy2"},
    ],
    "sad": [
        {"title": "How to Cope with Sadness", "link": "https://example.com/sad1"},
        {"title": "Finding Joy After Loss", "link": "https://example.com/sad2"},
    ],
    "angry": [
        {"title": "Managing Anger Effectively", "link": "https://example.com/angry1"},
        {"title": "Understanding Anger Issues", "link": "https://example.com/angry2"},
    ],
    "loved": [
        {"title": "The Power of Love", "link": "https://example.com/loved1"},
        {"title": "Building Healthy Relationships", "link": "https://example.com/loved2"},
    ],
    "emotional": [
        {"title": "Dealing with Emotional Turmoil", "link": "https://example.com/emotional1"},
        {"title": "Finding Balance in Emotions", "link": "https://example.com/emotional2"},
    ],
    "excited": [
        {"title": "Ways to Channel Your Excitement", "link": "https://example.com/excited1"},
        {"title": "How Excitement Affects Us", "link": "https://example.com/excited2"},
    ],
    "anxious": [
        {"title": "Managing Anxiety in Daily Life", "link": "https://example.com/anxious1"},
        {"title": "Techniques to Reduce Anxiety", "link": "https://example.com/anxious2"},
    ],
    "frustrated": [
        {"title": "Overcoming Frustration", "link": "https://example.com/frustrated1"},
        {"title": "Turning Frustration into Motivation", "link": "https://example.com/frustrated2"},
    ],
    "lonely": [
        {"title": "Coping with Loneliness", "link": "https://example.com/lonely1"},
        {"title": "Building Connections", "link": "https://example.com/lonely2"},
    ],
    "grateful": [
        {"title": "The Power of Gratitude", "link": "https://example.com/grateful1"},
        {"title": "Practicing Gratitude Daily", "link": "https://example.com/grateful2"},
    ],
    "relaxed": [
        {"title": "How to Maintain Relaxation", "link": "https://example.com/relaxed1"},
        {"title": "Techniques for Deep Relaxation", "link": "https://example.com/relaxed2"},
    ],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_mood = request.json.get('mood')
    recommendations = content_database.get(user_mood, [])
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
