import pyaudio
import wave
import requests
import openai
import re
import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Set the duration of the recording in seconds
RECORD_SECONDS = 10

# Set the sampling rate and the sample size in bytes
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "audio_file.wav"

# Initialize the PyAudio object and the stream
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

# Start recording
print("Recording...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Stop recording and close the stream
print("Finished recording.")
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio as a WAV file
wavefile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wavefile.setnchannels(CHANNELS)
wavefile.setsampwidth(audio.get_sample_size(FORMAT))
wavefile.setframerate(RATE)
wavefile.writeframes(b''.join(frames))
wavefile.close()

# set up API endpoint URL

url = "https://experimental.willow.vectara.io/v1/audio/transcriptions"

payload={'model': 'whisper-1'}
files=[
  ('file',('audio_file.wav',open('audio_file.wav','rb'),'audio/wav'))
]
headers = {
  'customer-id': '2982778228',
  'x-api-key': 'zqt_scmVdMBNwvDQnbUx7n-acMbDRg8-VkjNW2FeFw'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

# process API response
if response.status_code == 200:
    response_data = response.json()
    text2 = response_data["text"]

    print("Recognized text:", text2)
else:
    print("API request failed with status code:", response.status_code)

def clean_text(text):
    """Clean text by removing special characters, extra spaces, and converting to lowercase."""
    text = re.sub(r'[^\w\s]', '', text)  # remove special characters
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = text.lower()  # convert to lowercase
    return text.strip()

file = open("D:\hackathon\sample.txt", "r")
text1 = file.read()
file.close()


text1 = clean_text(text1)
text2 = clean_text(text2)

url = "https://experimental.willow.vectara.io/v1/chat/completions"

payload = json.dumps({
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": f"compare '{text1}' and '{text2}' based on context, and only calculate the similarity ratio and if the similarity ratio is not 100% show us the reasons in a list"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'customer-id': '2982778228',
  'x-api-key': 'zqt_scmVdMBNwvDQnbUx7n-acMbDRg8-VkjNW2FeFw'
}

response = requests.request("POST", url, headers=headers, data=payload)
xyz = json.loads(response.content)
context1 = xyz["choices"][0]["message"]["content"]
print(context1)



url = "https://experimental.willow.vectara.io/v1/chat/completions"

payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": f"generate ten questions about '{text1}'"
        }
    ]
    })
headers = {
    'Content-Type': 'application/json',
    'customer-id': '2982778228',
    'x-api-key': 'zqt_scmVdMBNwvDQnbUx7n-acMbDRg8-VkjNW2FeFw'
    }

response = requests.request("POST", url, headers=headers, data=payload)

xyz = json.loads(response.content)
context2 = xyz["choices"][0]["message"]["content"]
print(context2)