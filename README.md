# convertPDF-ENJP
PDFファイルの文章を英語から日本語に変換

## 概要
PDFMinerライブラリとEasyNMTライブラリを組み合わせて作成した簡易的なコード。
PDFファイルを入力, 出力は日本語文。
文書によっては処理が比較的長いですのでご注意を。

## EasyNMTライブラリ
英語から複数の言語に翻訳可能なライブラリ。OpenAIのAPIを用いて翻訳も可能ですが有料ですので、お試しに作る際にはこのライブラリが有効かと思います。

## 仮想環境構築

1. venvを用いて構築<br>
「convertpdf」という仮想環境を作成。
     ``` bash
     python -m venv convertpdf
     ```

2. 環境を有効化

     ``` bash
     // Windows
     .\convertpdf\Scripts\activate

     // Linux
     source convertpdf/bin/activate
     ```

3. ライブラリをインストール
     ``` bash
     pip install -r requirements.txt
     ```

4. 実行
     ``` bash
     // サンプル
     python main.py --fileurl https://arxiv.org/pdf/2006.11693v2.pdf
     ```

## 参考サイト
- https://tech.excite.co.jp/entry/2022/08/19/191151
- https://www.shibutan-bloomers.com/python_library_pdfminer-six/2124/
- https://docs.python.org/ja/3/howto/urllib2.html


