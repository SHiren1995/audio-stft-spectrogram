import os
import glob
import librosa
import librosa.display
import matplotlib.pyplot as plt


def audio_stft_spectrogram(input_data_path: str, output_data_path: str):
    # グラフ・縦軸、横軸の範囲設定
    plt.xlim(0, 60)
    plt.ylim(0, 1200)

    # 入力オーディオデータのパス取得
    input_files: list = glob.glob(input_data_path + '*')
    input_files_basename_without_ext :list = [ os.path.splitext(os.path.basename(file))[0] for file in input_files]

    # 出力スペクトログラムのパス取得
    output_files: list = glob.glob(output_data_path + '*')
    output_files_basename_without_ext :list = [ os.path.splitext(os.path.basename(file))[0] for file in output_files]

    # 入力ファイルと出力ファイルの差分取得
    diff_files = set(input_files_basename_without_ext) - set(output_files_basename_without_ext)
    input_file_path_list = [input_data_path + file for file in diff_files]

    # オーディオデータ → スペクトログラム
    if len(input_file_path_list):
        for file in input_file_path_list:

            # オーディオファイル名・取得
            basename_without_ext = os.path.splitext(os.path.basename(file))[0]

            try:
                # サンプリング周波数 22.05kHzで読み込み
                y, sr = librosa.load(file)

                # 短時間フーリエ変換（STFT）
                D = librosa.stft(y)

                # 複素数を強度と位相へ変換
                S, phase = librosa.magphase(D)

                # 強度をdb単位へ変換
                Sdb = librosa.amplitude_to_db(S)

                # スペクトログラムを書き込み
                librosa.display.specshow(Sdb, sr=sr, x_axis='time', y_axis='log')

                # スペクトログラム画像・生成
                plt.savefig(output_data_path + basename_without_ext + '.png')
                print(f'ファイル名：{basename_without_ext}.png スペクトログラム生成・完了')

            except:
                print('スペクトログラム生成に失敗しました。')
    else:
        print('出力可能な音声データが存在しません。')


if __name__ == "__main__":
    input_data_path = r"G:/マイドライブ/audiodata/"
    output_data_path = r"G:/マイドライブ/output_data/"
    audio_stft_spectrogram(input_data_path=input_data_path,
                           output_data_path=output_data_path)
