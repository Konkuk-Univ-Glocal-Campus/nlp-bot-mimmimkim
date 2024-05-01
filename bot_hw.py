import random

random_responses = ["재밌다 더 말해줘.",
                    "아 알겠어.",
                    "왜 그런말을 하니?",
                    "이상한 날씨야, 그렇지 않니?",
                    "주제를 바꿔보자.",
                    "지난 밤에 게임 깼어?"]

print("안녕 난 Marvin이야, 간단한 로봇이야.")
print("너가 '잘가'라고 입력하면 대화를 끝낼 수 있어.")
print("답을 입력한 뒤에 엔터를 눌러.")
print("오늘 뭐했어?")

while True:
    user_input = input("> ")
    if user_input.lower() == "잘가":
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("좋은 대화였어, 잘가!")
