import os
import shutil
import tempfile
import argparse
import urllib.request

from io import StringIO
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter

from easynmt import EasyNMT
from tqdm import tqdm

def main(args):

	with urllib.request.urlopen(args.fileurl) as response:
		print("file name: ", args.fileurl)
		with tempfile.NamedTemporaryFile(delete = False) as tmp_file:
			shutil.copyfileobj(response, tmp_file)

		with open(tmp_file.name, 'rb') as fp:
			print("file open")
			outfp = StringIO()
			rmgr = PDFResourceManager()
			lprms = LAParams()
			device = TextConverter(rmgr, outfp, laparams = lprms) 
			iprtr = PDFPageInterpreter(rmgr, device)

			# 1ページずつ解析
			for page in PDFPage.get_pages(fp):
				iprtr.process_page(page)

			text = outfp.getvalue()

			outfp.close()
			device.close()

		# 改行コードで分割
		lines = text.splitlines()

		# モデル読み込み
		if args.gpu:
			model = EasyNMT('mbart50_m2m', device='cuda')
		else:
			model = EasyNMT('mbart50_m2m')

		# 英語から日本語へ変換
		jplines = ''
		for line in tqdm(lines):
			if len(line) <= 1:
				continue
			line = model.translate(line, target_lang = 'ja')

			jplines += line + '\n'

		print(jplines)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'PDFファイルを英語から日本語に変換')
	parser.add_argument('--fileurl', default = 'https://arxiv.org/pdf/2006.11693v2.pdf', help = 'PDFファイルURL')
	parser.add_argument('--gpu', action='store_false', help='CPU or GPU')
	args = parser.parse_args()

	try:
		if not os.path.splitext(args.fileurl)[-1] == '.pdf':
			raise Exception('Error!')
	except Exception:
		print("This file is not PDF")
		exit(1)

	main(args)