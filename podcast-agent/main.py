
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_shorts():
    data = request.get_json()
    podcast_link = data.get("podcast_link")

    print(f"Received podcast link: {podcast_link}")

    # Simulate generating 10 short videos
    shorts = []
    for i in range(1, 11):
        shorts.append({
            "short_url": f"https://example.com/short_{i}.mp4",
            "instagram_caption": f"🔥 Clip {i} from the podcast! 🎧 #PodcastShorts",
            "youtube_title": f"Short Clip {i} - Best Moments",
            "youtube_description": f"This is short clip {i} from the podcast.",
            "facebook_description": f"Watch short {i} from the podcast. Don't miss out!"
        })

    return jsonify({
        "status": "success",
        "shorts": shorts
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
