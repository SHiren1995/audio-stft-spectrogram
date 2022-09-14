import os
import glob
import librosa
import librosa.display
import matplotlib.pyplot as plt


def audio_stft_spectrogram():
    # グラフ・縦軸、横軸の範囲設定
    plt.xlim(0,60)
    plt.ylim(0,1200)

    # オーディオデータのパス取得
    files:list = glob.glob("./input_data/*")

    # オーディオデータ → スペクトログラム
    for file in files:

        #オーディオファイル名・取得
        basename_without_ext = os.path.splitext(os.path.basename(file))[0]

        try:
            #サンプリング周波数 22.05kHzで読み込み
            y,sr = librosa.load(file) 

            # 短時間フーリエ変換（STFT）
            D = librosa.stft(y)

            # 複素数を強度と位相へ変換
            S, phase = librosa.magphase(D)

            # 強度をdb単位へ変換
            Sdb = librosa.amplitude_to_db(S)

            #スペクトログラムを書き込み
            librosa.display.specshow(Sdb, sr=sr, x_axis='time', y_axis='log')

            #スペクトログラム画像・生成
            plt.savefig("./output_data/" + basename_without_ext + '.png')
            print(f'ファイル名：{basename_without_ext}.png スペクトログラム生成・完了')

        except:
            print('スペクトログラム生成に失敗しました。')

if __name__ == "__main__":
    audio_stft_spectrogram()