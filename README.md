# easy_transcription

This is an aggregate of several other open transcription/diarization/google sheets tutorials into what I find to be the easiest way to transcribe>diarize>send to sheets. Using Whisper for transcription, PyAnnote for diarization, and App Engine APIs for sheets. 

1. python3 -m venv venv 
1. source venv/bin/activate 
1. python3 -m pip install -r requirements.txt
1. python3 -m jupyter notebook .

Drop in your mp3 files of interest in the same directory.
I initially made a simple GUI for this but you will likely need to tinker with the code for example if you have different audio formats or want to use a different size Whisper model, or if you run out of CUDA memory. Definitely open to PR's or ideas on how to make this more format agnostic and easier to use!

There are two notebooks, one is just to CSV, the other goes a bit further and pushes the csv straight to a sheets setup from a Google App Engine account -- if you're interested in that.  

Please raise issues if you run into them! A lot of the difficulty in this I've found is getting the requirements to work together as e.g. pyannote and whisper sometimes have conflicting requirements.
