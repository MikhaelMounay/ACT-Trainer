import pypdfium2 as pdfium
import re

pdf = pdfium.PdfDocument("./April 2021 (D05).pdf")
# print(len(pdf))

page = pdf[2]
width, height = page.get_size()
textpage = page.get_textpage()
text_all = textpage.get_text_range()
text_part = textpage.get_text_bounded(left=40, bottom=70, right=width-300, top=height-20)
text_part2 = textpage.get_text_bounded(left=300, bottom=70, right=width-40, top=height-20)
searcher = textpage.search("staccato", match_case=False, match_whole_word=False)

# print(searcher.get_next())
text_part = text_part.replace("\r\n", " ")
text_part = re.sub(' +', ' ', text_part)
# print(repr(text_part))
print(text_part)
# print(text_part2)