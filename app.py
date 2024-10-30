from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Expanded content for each mood with multiple real links
content_database = {
    "happy": [
        {"title": "10 Ways to Boost Your Happiness", "link": "https://www.verywellmind.com/ways-to-boost-your-happiness-2795037"},
        {"title": "The Science of Happiness", "link": "https://www.psychologytoday.com/us/basics/happiness"},
        {"title": "Finding Joy in Everyday Life", "link": "https://www.psychologytoday.com/us/articles/finding-joy-in-everyday-life"},
        {"title": "The Happiness Project", "link": "https://www.gretchenrubin.com/books/the-happiness-project/about-the-book/"},
    ],
    "sad": [
        {"title": "How to Cope with Sadness", "link": "https://www.helpguide.org/articles/mental-health/coping-with-sadness.htm"},
        {"title": "Finding Joy After Loss", "link": "https://www.psychologytoday.com/us/blog/the-optimistic-parent/201805/finding-joy-after-loss"},
        {"title": "Dealing with Sadness and Grief", "link": "https://www.verywellmind.com/dealing-with-grief-2794777"},
        {"title": "Overcoming Sadness", "link": "https://www.psychologytoday.com/us/basics/grief/overcoming-sadness"},
    ],
    "angry": [
        {"title": "Managing Anger Effectively", "link": "https://www.apa.org/topics/anger"},
        {"title": "Understanding Anger Issues", "link": "https://www.mayoclinic.org/diseases-conditions/anger-management/symptoms-causes/syc-20360438"},
        {"title": "Ways to Control Anger", "link": "https://www.verywellmind.com/how-to-control-anger-2795243"},
        {"title": "Anger Management Techniques", "link": "https://www.psychologytoday.com/us/basics/anger/anger-management-techniques"},
    ],
    "loved": [
        {"title": "The Power of Love", "link": "https://www.psychologytoday.com/us/basics/love"},
        {"title": "Building Healthy Relationships", "link": "https://www.mayoclinic.org/healthy-lifestyle/relationships-and-safety/in-depth/building-healthy-relationships/art-20045681"},
        {"title": "The Science of Love", "link": "https://www.psychologytoday.com/us/basics/love/the-science-love"},
        {"title": "Love and Relationships", "link": "https://www.verywellmind.com/the-importance-of-love-in-our-lives-2795560"},
    ],
    "emotional": [
        {"title": "Dealing with Emotional Turmoil", "link": "https://www.verywellmind.com/what-is-emotional-turmoil-2795910"},
        {"title": "Finding Balance in Emotions", "link": "https://www.psychologytoday.com/us/basics/emotional-regulation"},
        {"title": "Understanding Your Emotions", "link": "https://www.healthline.com/health/emotional-regulation"},
        {"title": "The Role of Emotions in Life", "link": "https://www.psychologytoday.com/us/basics/emotions"},
    ],
    "excited": [
        {"title": "Ways to Channel Your Excitement", "link": "https://www.verywellmind.com/how-to-channel-your-excitement-2796043"},
        {"title": "How Excitement Affects Us", "link": "https://www.psychologytoday.com/us/blog/feelings-figured-out/201802/the-excitement-puzzle"},
        {"title": "Excitement and Motivation", "link": "https://www.psychologytoday.com/us/basics/excitement"},
        {"title": "The Positive Effects of Excitement", "link": "https://www.verywellmind.com/excitement-as-a-motivator-2795883"},
    ],
    "anxious": [
        {"title": "Managing Anxiety in Daily Life", "link": "https://www.anxiety.org/managing-anxiety"},
        {"title": "Techniques to Reduce Anxiety", "link": "https://www.healthline.com/health/anxiety-reduction-techniques"},
        {"title": "Coping with Anxiety", "link": "https://www.verywellmind.com/understanding-anxiety-2795374"},
        {"title": "Anxiety Management Tips", "link": "https://www.psychologytoday.com/us/basics/anxiety/anxiety-management-tips"},
    ],
    "frustrated": [
        {"title": "Overcoming Frustration", "link": "https://www.psychologytoday.com/us/blog/overcoming-frustration"},
        {"title": "Turning Frustration into Motivation", "link": "https://www.verywellmind.com/how-to-turn-frustration-into-motivation-2795078"},
        {"title": "Coping with Frustration", "link": "https://www.healthline.com/health/coping-with-frustration"},
        {"title": "Managing Frustration in Life", "link": "https://www.psychologytoday.com/us/basics/frustration"},
    ],
    "lonely": [
        {"title": "Coping with Loneliness", "link": "https://www.verywellmind.com/ways-to-cope-with-loneliness-2794868"},
        {"title": "Building Connections", "link": "https://www.mindtools.com/pages/article/newTCS_01.htm"},
        {"title": "Understanding Loneliness", "link": "https://www.psychologytoday.com/us/basics/loneliness"},
        {"title": "Finding Joy in Solitude", "link": "https://www.verywellmind.com/finding-joy-in-solitude-2795643"},
    ],
    "grateful": [
        {"title": "The Power of Gratitude", "link": "https://greatergood.berkeley.edu/article/item/the_power_of_gratitude"},
        {"title": "Practicing Gratitude Daily", "link": "https://www.psychologytoday.com/us/blog/the-moment-youth/202011/the-power-gratitude"},
        {"title": "How Gratitude Affects Us", "link": "https://www.healthline.com/health/benefits-of-gratitude"},
        {"title": "The Science of Gratitude", "link": "https://www.verywellmind.com/the-science-of-gratitude-2795897"},
    ],
    "relaxed": [
        {"title": "How to Maintain Relaxation", "link": "https://www.healthline.com/health/ways-to-relax"},
        {"title": "Techniques for Deep Relaxation", "link": "https://www.mindful.org/how-to-practice-relaxation/"},
        {"title": "Relaxation Strategies", "link": "https://www.psychologytoday.com/us/basics/relaxation"},
        {"title": "The Benefits of Relaxation", "link": "https://www.verywellmind.com/the-benefits-of-relaxation-2794876"},
    ],
}

@app.route('/')
def index():
    return render_template('index.html')

# New route to display recommendations on a separate page
@app.route('/recommendations', methods=['POST'])
def recommendations():
    user_mood = request.form.get('mood')  # Get mood from form submission
    recommendations = content_database.get(user_mood.lower(), [])
    
    # Shuffle recommendations to ensure variety
    random.shuffle(recommendations)

    return render_template('recommendations.html', mood=user_mood, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
