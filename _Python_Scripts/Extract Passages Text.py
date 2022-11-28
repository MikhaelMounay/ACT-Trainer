import pypdfium2 as pdfium
import re

pdf = pdfium.PdfDocument("./April 2021 (D05).pdf")
# print(len(pdf))

questions = {}
answers = {}

def getQuestionsFromPage(pagenumber):
  page = pdf[pagenumber - 1]
  width, height = page.get_size()
  textpage = page.get_textpage()
  text_all = textpage.get_text_range()
  text_part = textpage.get_text_bounded(
      left=40, bottom=70, right=width-300, top=height-20)
  text_part2 = textpage.get_text_bounded(
      left=300, bottom=70, right=width-40, top=height-20)

  # searcher = textpage.search("staccato", match_case=False, match_whole_word=False)
  # print(searcher.get_next())

  text_part = text_part.replace("\r\n", " ")
  text_part = re.sub(' +', ' ', text_part)

  text_part2 = text_part2.replace("\r\n", " ")
  text_part2 = re.sub(' +', ' ', text_part2)

  # print(repr(text_part))
  # print(text_part)
  print(text_part2)

  numberofquestions = 75
  # questions = {}
  # answers = {}

  for i in range(int(float(text_part2[0:2])), numberofquestions + 1):
    print(i)
    if f"{i}. " in text_part2:
      if i % 2 != 0:
        subtofind = re.findall(f"{i}\..*?A\.", text_part2)[0]
        questions[i] = text_part2[text_part2.find(subtofind) + len(f"{i}. ") : text_part2.find(subtofind) + len(subtofind) - 3]
        sub2tofind = re.findall(f"{i}\..*?A\. ", text_part2)[0]
        sub2tofind2 = re.findall(f"{i}\..*?B\. ", text_part2)[0]
        sub2tofind3 = re.findall(f"{i}\..*?C\. ", text_part2)[0]
        sub2tofind4 = re.findall(f"{i}\..*?D\. ", text_part2)[0]
        answers[i] = {}
        answers[i]["A"] = text_part2[text_part2.find(sub2tofind) + len(sub2tofind) : text_part2.find(sub2tofind2) + len(sub2tofind2) - 4]
        answers[i]["B"] = text_part2[text_part2.find(sub2tofind2) + len(sub2tofind2) : text_part2.find(sub2tofind3) + len(sub2tofind3) - 4]
        answers[i]["C"] = text_part2[text_part2.find(sub2tofind3) + len(sub2tofind3) : text_part2.find(sub2tofind4) + len(sub2tofind4) - 4]
        if f"{i+1}. " in text_part2:
          answers[i]["D"] = text_part2[text_part2.find(sub2tofind4) + len(sub2tofind4) : text_part2.find(re.findall(f"{i+1}\.", text_part2)[0]) + len(re.findall(f"{i+1}\.", text_part2)[0]) - 3]
        else:
          answers[i]["D"] = text_part2[text_part2.find(sub2tofind4) + len(sub2tofind4) :]
          break

      elif i % 2 == 0:
        subtofind = re.findall(f"{i}\..*?F\.", text_part2)[0]
        questions[i] = text_part2[text_part2.find(subtofind) + len(f"{i}. ") : text_part2.find(subtofind) + len(subtofind) - 3]
        sub2tofind = re.findall(f"{i}\..*?F\. ", text_part2)[0]
        sub2tofind2 = re.findall(f"{i}\..*?G\. ", text_part2)[0]
        sub2tofind3 = re.findall(f"{i}\..*?H\. ", text_part2)[0]
        sub2tofind4 = re.findall(f"{i}\..*?J\. ", text_part2)[0]
        answers[i] = {}
        answers[i]["A"] = text_part2[text_part2.find(sub2tofind) + len(sub2tofind) : text_part2.find(sub2tofind2) + len(sub2tofind2) - 4]
        answers[i]["B"] = text_part2[text_part2.find(sub2tofind2) + len(sub2tofind2) : text_part2.find(sub2tofind3) + len(sub2tofind3) - 4]
        answers[i]["C"] = text_part2[text_part2.find(sub2tofind3) + len(sub2tofind3) : text_part2.find(sub2tofind4) + len(sub2tofind4) - 4]
        if f"{i+1}. " in text_part2:
          answers[i]["D"] = text_part2[text_part2.find(sub2tofind4) + len(sub2tofind4) : text_part2.find(re.findall(f"{i+1}\.", text_part2)[0]) + len(re.findall(f"{i+1}\.", text_part2)[0]) - 3]
        else:
          answers[i]["D"] = text_part2[text_part2.find(sub2tofind4) + len(sub2tofind4) :]
          break

  # print(questions)
  # print("==============")
  # print(answers)

for i in range(4, 14):
  getQuestionsFromPage(i)

print("==================================================")
for i in answers:
  print(i, " :", answers[int(i)])