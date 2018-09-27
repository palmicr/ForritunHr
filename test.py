number = 0x6f73

question_mask = number & 0x0700

answer_mask = number & 0x0000


question_number = question_mask >> 7

answer = answer_mask >> 2

print(question_number, answer)
