import math

def amplitude_to_db(amplitude):

    if amplitude > 0:
        return 20 * math.log10(amplitude)
    else:
        return -float('inf') 

def extract_top_intensities_db(input_txt_file_path, output_txt_file_path, top_n=10000):
    with open(input_txt_file_path, 'r') as file:
        lines = file.readlines()

    time_db_pairs = []
    for line in lines:
        t, i = line.strip().split(',')
        db_intensity = amplitude_to_db(float(i))
        time_db_pairs.append((float(t), db_intensity))


    average_db_intensity = sum(db for t, db in time_db_pairs if db != -float('inf')) / len(time_db_pairs)


    top_db_intensities = sorted(time_db_pairs, key=lambda pair: pair[1], reverse=True)[:top_n]


    with open(output_txt_file_path, 'w') as file:
        file.write(f"Average dB intensity: {average_db_intensity}\n")
        for time, db_intensity in top_db_intensities:
            file.write(f"Time: {time}, dB Intensity: {db_intensity}\n")

    print(f"Data processed and saved to {output_txt_file_path}")


input_path = 'audio_data_output1.txt'
output_path = 'processed_audio_data_db.txt'
extract_top_intensities_db(input_path, output_path)

