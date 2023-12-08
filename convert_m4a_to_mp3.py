import subprocess
import sys

def convert_m4a_to_mp3(input_file):
    output_file = input_file.rsplit('.', 1)[0] + '.mp3'
    command = ['ffmpeg', '-i', input_file, '-acodec', 'libmp3lame', '-y', output_file]
    subprocess.run(command)
    print(f"Converted '{input_file}' to '{output_file}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_m4a_to_mp3.py <filename>")
    else:
        input_m4a = sys.argv[1]
        convert_m4a_to_mp3(input_m4a)

