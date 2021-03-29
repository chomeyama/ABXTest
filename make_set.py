import os
import shutil

wav_root = '../wav/'
METHOD = ['world', 'nsf', 'qppwg', 'usfgan']
SPK = ['bdl', 'clb', 'rms', 'slt']
N_SET = 10
N_DATA_PER_SET = 5

data_number = [474, 487, 500, 513]

for n_set in range(N_SET):
    files = [[] for i in range(len(METHOD))]
    for i in range(N_DATA_PER_SET):
        spk_index = (n_set + i) % len(SPK)
        for j, method in enumerate(METHOD):
            os.makedirs(f'wav/set{n_set + 1}/{method}', exist_ok=True)
            for scale in [2.00, 0.50]:
                file_path = f'{method}/{SPK[spk_index]}_arctic_b{data_number[spk_index]:0>4}_f{scale:.2f}.wav'
                new_file_path = shutil.copyfile(wav_root + file_path, f'wav/set{n_set + 1}/' + file_path)
                files[j] += [new_file_path]
        data_number[spk_index] += 1
    for j, method in enumerate(METHOD):
        with open(f'wav/set{n_set + 1}/{method}.list', mode='w') as f:
            for file_path in sorted(files[j]):
                f.write(file_path + '\n')