from flask import Flask, request, jsonify
from routes.video_process import process_video

app = Flask(__name__)

@app.route('/process_video', methods=['POST'])
def process_video_route():
    data = request.get_json()
    youtube_url = data.get('youtube_url')

    if not youtube_url:
        return jsonify({'error': 'No YouTube URL provided'}), 400
    
    # Process the video
    result = process_video(youtube_url)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

