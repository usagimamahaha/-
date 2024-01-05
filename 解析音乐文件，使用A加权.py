import soundfile as sf;
import numpy as np;

def extract_audio_segment(flac_file_path, output_txt_file_path, start_time, end_time):
    print(f"Extracting audio data from {flac_file_path} between {start_time} and {end_time} seconds...")

    data, samplerate = sf.read(flac_file_path)

    start_sample = int(start_time * samplerate)
    end_sample = int(end_time * samplerate)

    segment = data[start_sample:end_sample]

    timestamps = [start_time + (i / samplerate) for i in range(len(segment))]

    with open(output_txt_file_path, 'w') as file:
        for time, amplitude in zip(timestamps, segment):
            if isinstance(amplitude, (list, tuple, np.ndarray)):
                amplitude = sum(amplitude) / len(amplitude)
            file.write(f"{time}, {amplitude}\n")

    print(f"Data extracted and saved to {output_txt_file_path}")

flac_path = "/home/zyf/桌面/NO, Thank You!.flac"
txt_path = "/home/zyf/桌面/audio_data_output1.txt"
extract_audio_segment(flac_path, txt_path, 30, 60)
