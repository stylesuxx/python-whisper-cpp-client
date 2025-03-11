from whisper_cpp_client import WhisperCppClient
import json

client = WhisperCppClient('http://192.168.1.44', 3333)
client.set_params({
    'response_format': 'json'
})

try:
    response_content = client.transcribe('./examples/jfk.wav')
    data = json.loads(response_content)
    print(data)
except Exception as e:
    print(f"Error: {e}")
