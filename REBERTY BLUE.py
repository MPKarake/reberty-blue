import discord
from discord.ext import commands
from discord import DMChannel
import asyncio
import random
from discord.utils import get

import game as game


client = discord.Client()

링크 = 739134516517666957
공지 = 735848968105492514
카피페 = 736295129937215579
관계 = 735848943870672937

attack = ["공격 실패", "공격 성공"]
drink = ["당신은 취했습니다.", "당신은 안 취했습니다."]
evasion = ["회피 실패", "회피 성공"]
prison = ["포로 취득 성공", "포로 취득 실패"]
save = ["포로 구출 성공", "포로 구출 실패"]
fish1 = ["장화", "데비 존스의 라커 문짝", "모자", "빈병", "스펀지", "전기뱀장어", "개복치"]
fish2 = ["정어리", "새우", "엔초비", "게", "오징어", "불가사리", "해초", "복어", "고등어", "농어", "넙치", "말미잘", "날치", "멸치",
         "해삼", "낙지", "명태", "물에 불은 책"]
fish3 = ["연어", "갈치", "해파리", "돔", "가오리", "돌돔", "병어", "삼치", "문어", "바다포도", "랍스터", "쏨뱅이", "무언가의 부품",
         "망한 데이트 편지"]
fish4 = ["철갑상어", "거북이", "참치", "장어", "상어"]
fish5 = ["크라켄(생후 3일)", "금화 주머니"]
fish6 = ["크라켄(생후 3일)"]
hint_letter = ["```18xx x월 xx일\n라 부세의 지도를 손에 넣었다. 여기까진 모든 일이 잘 풀렸고, 신이 우리를 인도한다고 생각했다."
               " 그 빌어먹을 난류만 아니었으면 말이다. 우리 배는 순식간에 난파되었고, "
               "선원들은 흩어졌다. 보물에 접근하려면 정보가 더 필요하다.```",
               "```17xx x월 xx일\n해도를 손에 넣어서 섬에 정박했을 때만 해도 우리는 희망에 부풀어 있었다. 설마 섬에서 조난을 당할 줄이야. "
               "다들 어디 가버렸는지조차 모르겠다. 탐사가 가능한 수준의 지형이 아니었다.```"]
no_hint_letter = ["```누가 그 문장을 곧이 곧대로 해석해? 머저리가 틀림없지.```",
                  "```사랑하는 나의 앤 메리, 이 전쟁이 끝나면 고국으로 돌아갈 거야. 어머니도 동생들도 나를 반기겠지. 당신이 너무 그리워...```",
                  "```누가 이걸 본다면 제 소원을 이루어주세요! 새 이빨이 곱게 났으면 좋겠어요.```",
                  "```소원을 담은 편지를 바다에 흘려보내면 이루어진다는데, 당신이 내게 돌아왔으면 좋겠어.```",
                  "```무인도에 표류한지 11일 째다. 나는 내 망할 오크통에 얼굴을 그려놓고 말을 붙이고 있다...```",
                  "```바다에 쓰레기 좀 버리지 마라. 이 인간 쓰레기들아.```"]
w = ["맑음", "바람많음", "비", "번개", "흐림", "폭우", "태풍"]
nene = ["그 미치광이 이야기를 지금 해야겠어?", "**그 남자가 영국의 적이라고 생각해?**", "영어를 할 줄 아는 모양이던데."
        , "여자는 왜 자꾸 데려오는 거야?", "돈, 권력, 그리고 여자!", "누구도 침범할 수 없는 자유", "네 인생은 온전히 너의 것"
        , "너, 이런 삶에 만족해?", "**이제 네 삶은 온전히 네 거야. 축하해.**", "너희 전부 내 거야. 내 보물이야. 내가 찾은."
        , "PLVS VLTRA. 저 너머, 더 멀리.", "손에 쥔 것은 적의 무기", "\"선장. 커피를 좋아하시네요.\""
        , "세상에 가진 놈 아니면 뺏기는 놈 뿐이야.", "**내 거니까 내가 보호하지. 뭐가 잘못됐어?**"
        , "인생? 즐겁지. 그야 이렇게 살 수 있는 것도 한 번 뿐이잖아.", "그 고양이, 내가 데려온 건데! 내 말은 듣질 않는다고."
        , "살아가는데 수치심이 필요해?", "*뭔가 가지고 싶은데.*", "***For The Queen***", "정은 붙이는 쪽이 손해지. 안 그래?"
        , "고향을 모르는 자", "영국에서 커피는 선원들이나 마시는거라고.", "**처음**으로 마주한 바다는 숨막히도록 아름답고, 슬펐다."
        , "가끔은 어머니가 여전히 바닷속에 남아 있을 거란 생각을 해.", "난 어디로든 갈 수 있어. 어디든.", "이대로 버티면 새벽이 온다."
        , "익숙한 것이 나아. 아니야, 싫어. 아니야. 좋아.", "**손해봤네. 그치.**"]
do_not_know_home = ["태어난 거? 어디더라. 아무튼 바다 한복판이었다는 건 들었네.", "**스페인에 충성하냐고? 내가 왜?**"
                    , "안달루시아, 멋진 곳이지!", "아버진 바보 같은 짓을 했어. 덕분에 살았지만."
                    , "***투항하지 않는 자는 전부 죽이고, 나머지는 부하로 삼겠다!***", "하나는 아버지 이름. 하나는 어머니의 이름. 아마도?"
                    , "이 배가 내 집이야. 그걸로 충분해."]
favorita = ["왕의 총애를 받는 이", "이방인들의 집", "떠나려면 떠나. 잡아두긴 싫으니까."]
Nell = ["풍요로운 봄, 밝게 빛나는 황금향.", "나는 여기서 책을 덮는다."]
free = ["너희에게 주고 싶은 것. 경험하게 하고 싶은 것. 내가 경험한, 가장 아름다운 일."
        , "누구든 이 배에 오를 수 있고, 또한 누구든 떠날 수 있으리라.", "선택은 너희들이 해. 그리고 책임을 져."]
david = ["HMS 마르스의 함장", "눈도 없고, 팔도 없는데 능력만 있는 놈이지.", "TRIA JUNCTA IN UNO. 힘을 모은다면 안될 거는 없지."
         , "Dlieu et mon droit. 우리의 권리를 위해.", "영국의 방패, 여왕폐하의 방패", "***Long Live the Queen Diana.***"
         , "***God Save The Queen.***", "너희는 무엇을 위해서 싸우는 거지?", "`\'오랜 친우들이여. 부디 그곳에서는 편안하게...\'`"
         , "```\"어떤걸 지키고 싶다면 먼저 살아남아야 돼. 살아남지 못하면 너가 지킬려는 것도 지킬 수 없게 되니깐.\"```-???"
         , "```\"ㄸ-- ㄱ- HMS 마르스의 함장에 임명한다. 1816년. 다이애나 여왕폐하 대신 읽음\"```-한 궁전 관료"
         , "우리의 희생이 당연한거냐고? 글쎄. 그건 나도 모르지. 나도 아직 그 답을 찾지 못했거든."
         , "\"나는 매번 무기를 들때마다 기도를 해.. 부디 내가 내 나라를 지킬 수 있는 방패가 될 수 있게 해달라고 말이야.\""
         , "```\"난 이해가 안돼! 어떻게 평민인 주제에 나보다 먼저 진급할 수 있냐고!!\"```-진급 심사에서 떨어진 장교"]
Mars = ["새 시대를 여는 첫걸음", "과연 관용과 포용이 통할까?", "스파이 손님을 태우는건 여간 힘든일이 아니야."
        , "전쟁의 신 마르스시여. 부디 저희를 지키시며 바른길로 나아갈 수 있게 인도해주소서."
        , "```\"함장이 된 것을 축하하네. 아니 슬퍼해야 할까? 하지만 좋게 생각해주게. 그만큼 정부가 경에게 거는 기대가 크다는 말이니깐. 당장 "
          "비밀첩보부를 경에게 지원하지 않았나? 난 경이 그 스파이들을 잘 쓸거라고 믿네.\"```-한 관리"]
SPY = ["\"그래서 귀관의 이름이.. ㄹ-- 파ㅇ-라고? 아... -- -ㄷ.. 알았네. 앞으로도 우리 그레이트브리튼 왕국을 위해 일해주게\""
       , "ㄹ크 --.. 부디 조심하게.", "자네가 죽어 사라져도 우리 영국은 자네를 영원히 기억하겠네. 맹세할게."
       , "```이름 : 루크 매든\n본명 : 로버트 파이크\n\n국적 : 영국\n나이 : 32세\n특이사항 : 영국 비밀첩보국 소속 요원. 현재 3년째 파보리타"
         " 호에 잠입 중.```"]
england = ["누군가는 부수고 싶어하는 땅. **하지만 나에게는 내가 지켜야만 하는 땅이야.**", "***현재 내가 복무하는 유일한 이유***"
           , "사람이 돌아오게 할려면 그들이 살 집을 지켜줘야하지 않을까?", "난 내 친구들과 가족이 사랑했던 영국을 지킬 뿐이야."]


@client.event
async def on_ready():
    print(client.user.id)
    print("reday")
    game = discord.Game("RE:berty Blue")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    id = client.get_guild(715419524140236842)

    if message.content.startswith(">Liberty Blue"):
        await message.channel.send("***누구에게도 지배 당하지 않는, 자유로운 바다.***")

    if message.content.startswith(">넬 네르하 엘도라도"):
        await message.channel.send(random.choice(nene))

    if message.content.startswith(">고향을 모르는 자"):
        await message.channel.send(random.choice(do_not_know_home))

    if message.content.startswith(">파보리타"):
        await message.channel.send(random.choice(favorita))

    if message.content.startswith(">오리올 네르하"):
        await message.channel.send("안달루시아 출신의 남자. 아내와 아들을 끔찍히 사랑했다지. 그 목이 잘리는 순간엔...")

    if message.content.startswith(">네레이다 엘도라도"):
        await message.channel.send("아이가 태어나자 서약을 깨고 바다에 던져졌다. 그의 아들은 요람에서 그 이야기를 자장가 대신 들었다.")

    if message.content.startswith(">Nell Nerja El Dorado"):
        await message.channel.send(random.choice(Nell))

    if message.content.startswith(">자유"):
        await message.channel.send(random.choice(free))

    if message.content.startswith(">여왕의 노예"):
        await message.channel.send("Nell Nerja El Dorado.")

    if message.content.startswith(">데이비드 젤리코"):
        await message.channel.send(random.choice(david))

    if message.content.startswith(">HMS 마르스"):
        await message.channel.send(random.choice(Mars))

    if message.content.startswith(">스파이"):
        await message.channel.send(random.choice(SPY))

    if message.content.startswith(">영국"):
        await message.channel.send(random.choice(england))

    if message.content.startswith(">여왕의 방패"):
        await message.channel.send("David Jellico")

    if message.content.startswith(">주사위는 던져졌다"):
        await message.channel.send(random.randint(1, 100))

    if message.content.startswith(">다이스"):
        msg = message.content[5:]
        msg1 = msg.split()
        min = int(msg1[0])
        max = int(msg1[1])
        await message.channel.send(random.randint(min, max))

    if message.content.startswith(">낚시"):
        success = random.randint(1, 5)
        if success == 1:
            await message.channel.send("{0.author.mention}은(는) 무언가를 놓쳤다...".format(message))
        else:
            fish = random.randint(1, 100)
            if fish >= 1 and fish <= 16:
                f_result1 = random.choice(fish1)
                if str(f_result1) == "전기뱀장어":
                    fish_result1 = "{0.author.mention}은(는) **".format(message) + str(f_result1) + "**을(를) 낚았다!"
                    size1 = random.randint(200, 250)
                    size2 = random.randint(0, 9)
                    fish_result1_1 = "**" + str(f_result1) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                         "\'** cm다."
                    await message.channel.send(str(fish_result1) + "\n" + str(fish_result1_1))
                elif str(f_result1) == "개복치":
                    fish_result1 = "{0.author.mention}은(는) **".format(message) + str(f_result1) + "**을(를) 낚았다!"
                    size1 = random.randint(175, 185)
                    size2 = random.randint(0, 9)
                    fish_result1_2 = "**" + str(f_result1) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result1) + "\n" + str(fish_result1_2))
                else:
                    fish_result1 = "{0.author.mention}은(는) **".format(message) + str(f_result1) + "**을(를) 낚았다!"
                    await message.channel.send(fish_result1)
            elif fish > 17 and fish <= 53:
                f_result2 = random.choice(fish2)
                if str(f_result2) == "정어리":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(5, 10)
                    size2 = random.randint(0, 9)
                    fish_result2_1 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                elif str(f_result2) == "새우":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(1, 2)
                    size2 = random.randint(0, 9)
                    fish_result2_2 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_2))
                elif str(f_result2) == "게":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(150, 180)
                    size2 = random.randint(0, 9)
                    fish_result2_3 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_3))
                elif str(f_result2) == "오징어":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(8, 18)
                    size2 = random.randint(0, 9)
                    fish_result2_4 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_4))
                elif str(f_result2) == "불가사리":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(25, 80)
                    size2 = random.randint(0, 9)
                    fish_result2_5 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_5))
                elif str(f_result2) == "복어":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(10, 20)
                    size2 = random.randint(0, 9)
                    fish_result2_6 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_6))
                elif str(f_result2) == "고등어":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(30, 40)
                    size2 = random.randint(0, 9)
                    fish_result2_7 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_7))
                elif str(f_result2) == "농어":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(100, 200)
                    size2 = random.randint(0, 9)
                    fish_result2_8 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_8))
                elif str(f_result2) == "넙치":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(15, 83)
                    size2 = random.randint(0, 9)
                    fish_result2_9 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_9))
                elif str(f_result2) == "날치":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(30, 40)
                    size2 = random.randint(0, 9)
                    fish_result2_10 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                      "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_10))
                elif str(f_result2) == "멸치":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(10, 20)
                    size2 = random.randint(0, 9)
                    fish_result2_11 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                      "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_11))
                elif str(f_result2) == "낙지":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(55, 65)
                    size2 = random.randint(0, 9)
                    fish_result2_12 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                      "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_12))
                elif str(f_result2) == "명태":
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    size1 = random.randint(30, 90)
                    size2 = random.randint(0, 9)
                    fish_result2_13 = "**" + str(f_result2) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                      "\'** cm다."
                    await message.channel.send(str(fish_result2) + "\n" + str(fish_result2_13))
                else:
                    fish_result2 = "{0.author.mention}은(는) **".format(message) + str(f_result2) + "**을(를) 낚았다!"
                    await message.channel.send(fish_result2)
            elif fish > 54 and fish <= 81:
                f_result3 = random.choice(fish3)
                if str(f_result3) == "망한 데이트 편지":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    await message.channel.send(str(fish_result3) + "\n", file=discord.File("letter1.png"))
                elif str(f_result3) == "연어":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(71, 76)
                    size2 = random.randint(0, 9)
                    fish_result3_1 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_1))
                elif str(f_result3) == "갈치":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(95, 105)
                    size2 = random.randint(0, 9)
                    fish_result3_2 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_2))
                elif str(f_result3) == "해파리":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(5, 150)
                    size2 = random.randint(0, 9)
                    fish_result3_3 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_3))
                elif str(f_result3) == "돔":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(15, 85)
                    size2 = random.randint(0, 9)
                    fish_result3_4 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_4))
                elif str(f_result3) == "가오리":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(180, 700)
                    size2 = random.randint(0, 9)
                    fish_result3_5 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_5))
                elif str(f_result3) == "돌돔":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(20, 40)
                    size2 = random.randint(0, 9)
                    fish_result3_6 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_6))
                elif str(f_result3) == "병어":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(20, 70)
                    size2 = random.randint(0, 9)
                    fish_result3_7 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_7))
                elif str(f_result3) == "삼치":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(95, 105)
                    size2 = random.randint(0, 9)
                    fish_result3_8 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_8))
                elif str(f_result3) == "문어":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(100, 300)
                    size2 = random.randint(0, 9)
                    fish_result3_9 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_9))
                elif str(f_result3) == "랍스터":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(25, 50)
                    size2 = random.randint(0, 9)
                    fish_result3_10 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                      "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_10))
                elif str(f_result3) == "쏨뱅이":
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    size1 = random.randint(15, 30)
                    size2 = random.randint(0, 9)
                    fish_result3_11 = "**" + str(f_result3) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                      "\'** cm다."
                    await message.channel.send(str(fish_result3) + "\n" + str(fish_result3_11))
                else:
                    fish_result3 = "{0.author.mention}은(는) **".format(message) + str(f_result3) + "**을(를) 낚았다!"
                    await message.channel.send(fish_result3)
            elif fish > 82 and fish <= 92:
                dice = random.randint(1, 5)
                if dice < 2:
                    letter_result = random.choice(hint_letter)
                    fish_result4 = "{0.author.mention}은(는) **누군가의 유리병 편지**을(를) 낚았다!\n".format(message) + \
                                   str(letter_result)
                    await message.channel.send(fish_result4)
                else:
                    letter_result = random.choice(no_hint_letter)
                    fish_result4 = "{0.author.mention}은(는) **누군가의 유리병 편지**을(를) 낚았다!\n".format(message) + \
                                   str(letter_result)
                    await message.channel.send(fish_result4)
            elif fish > 93 and fish < 99:
                f_result4 = random.choice(fish4)
                if str(f_result4) == "철갑상어":
                    fish_result4 = "{0.author.mention}은(는) **".format(message) + str(f_result4) + "**을(를) 낚았다!"
                    size1 = random.randint(76, 860)
                    size2 = random.randint(0, 9)
                    fish_result4_1 = "**" + str(f_result4) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result4) + "\n" + str(fish_result4_1))
                elif str(f_result4) == "거북이":
                    fish_result4 = "{0.author.mention}은(는) **".format(message) + str(f_result4) + "**을(를) 낚았다!"
                    size1 = random.randint(100, 220)
                    size2 = random.randint(0, 9)
                    fish_result4_2 = "**" + str(f_result4) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result4) + "\n" + str(fish_result4_2))
                elif str(f_result4) == "참치":
                    fish_result4 = "{0.author.mention}은(는) **".format(message) + str(f_result4) + "**을(를) 낚았다!"
                    size1 = random.randint(250, 450)
                    size2 = random.randint(0, 9)
                    fish_result4_3 = "**" + str(f_result4) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result4) + "\n" + str(fish_result4_3))
                elif str(f_result4) == "장어":
                    fish_result4 = "{0.author.mention}은(는) **".format(message) + str(f_result4) + "**을(를) 낚았다!"
                    size1 = random.randint(60, 80)
                    size2 = random.randint(0, 9)
                    fish_result4_4 = "**" + str(f_result4) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result4) + "\n" + str(fish_result4_4))
                elif str(f_result4) == "상어":
                    fish_result4 = "{0.author.mention}은(는) **".format(message) + str(f_result4) + "**을(를) 낚았다!"
                    size1 = random.randint(150, 500)
                    size2 = random.randint(0, 9)
                    fish_result4_5 = "**" + str(f_result4) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result4) + "\n" + str(fish_result4_5))
                else:
                    fish_result4 = "{0.author.mention}은(는) **".format(message) + str(f_result4) + "**을(를) 낚았다!"
                    await message.channel.send(fish_result4)
            elif fish == 100:
                f_result5 = random.choice(fish5)
                if str(f_result5) == "크라켄(생후 3일)":
                    size1 = random.randint(30, 50)
                    size2 = random.randint(0, 9)
                    fish_result5 = "<@&715422619779727410>\n" \
                                   "{0.author.mention}은(는) **".format(message) + str(f_result5) + "**을(를) 낚았다!"
                    fish_result5_1 = "**" + str(f_result5) + "**의 크기는 **\'" + str(size1) + "." + str(size2) + \
                                     "\'** cm다."
                    await message.channel.send(str(fish_result5) + "\n" + str(fish_result5_1))
                else:
                    gold = random.randint(3, 15)
                    fish_result5 = "{0.author.mention}은(는) **".format(message) + str(f_result5) + "**을(를) 낚았다!"
                    coin = "금화 주머니에는 금화 " + str(gold) + " 닢이 들어있다."
                    result = str(fish_result5) + "\n" + str(coin)
                    await message.channel.send(result)

    if message.content.startswith(">야바위"):
        gamble = random.randint(1, 3)
        msg1 = "{0.author.mention}은(는) 빠르게 컵을 섞기 시작한다.".format(message)
        msg2 = "슥"
        msg3 = "결과는?"
        await message.channel.send(msg1)
        await message.channel.send(msg2)
        await message.channel.send(msg2)
        await message.channel.send(msg2)
        if gamble == 1:
            msg = "구슬이 숨겨진 컵은 첫번째 컵입니다."
            await message.author.send(msg)
        elif gamble == 2:
            msg = "구슬이 숨겨진 컵은 두번째 컵입니다."
            await message.author.send(msg)
        else:
            msg = "구슬이 숨겨진 컵은 세번째 컵입니다."
            await message.author.send(msg)
        await message.channel.send(msg3)

    if message.content.startswith(">사기야바위"):
        msg1 = "{0.author.mention}은(는) 빠르게 컵을 섞기 시작한다.".format(message)
        msg2 = "슥"
        msg3 = "삭"
        msg4 = "결과는?"
        msg = "당신은 사기를 시전했습니다."
        await message.channel.send(msg1)
        await message.channel.send(msg2)
        await message.channel.send(msg2)
        await message.channel.send(msg3)
        await message.author.send(msg)
        await message.channel.send(msg4)

    if message.content.startswith(">술 약한"):
        msg1 = "{0.author.mention}은(는) 술을 마셨다.".format(message)
        msg2 = random.choice(drink)
        msg3 = "{0.author.mention}, ".format(message)
        await message.channel.send(str(msg1))
        await message.channel.send(str(msg3) + str(msg2))

    if message.content.startswith(">술 중간"):
        r = random.randint(1, 10)
        msg1 = "{0.author.mention}은(는) 술을 마셨다.".format(message)
        msg2 = "{0.author.mention}, ".format(message)
        msg3 = "당신은 취했습니다."
        msg4 = "당신은 안 취했습니다."
        if r >= 1 and r < 4:
            await message.channel.send(str(msg1))
            await message.channel.send(str(msg2) + str(msg3))
        else:
            await message.channel.send(str(msg1))
            await message.channel.send(str(msg2) + str(msg4))

    if message.content.startswith(">술 센"):
        r = random.randint(1, 10)
        msg1 = "{0.author.mention}은(는) 술을 마셨다.".format(message)
        msg2 = "{0.author.mention}, ".format(message)
        msg3 = "당신은 취했습니다."
        msg4 = "당신은 안 취했습니다."
        if r >= 1 and r < 3:
            await message.channel.send(str(msg1))
            await message.channel.send(str(msg2) + str(msg3))
        else:
            await message.channel.send(str(msg1))
            await message.channel.send(str(msg2) + str(msg4))

    if message.content.startswith(">공격"):
        member = message.mentions[0]
        As = random.choice(attack)
        content = "{0.author.mention}가 {1.mention}에게 공격을 시도합니다.\n".format(message, member) + str(As)
        await message.channel.send(content)

    if message.content.startswith(">회피"):
        member = message.mentions[0]
        Es = random.choice(evasion)
        content = "{0.author.mention}가 {1.mention}의 공격에 회피를 시도합니다.\n".format(message, member) + str(Es)
        await message.channel.send(content)

    if message.content.startswith(">포로취득"):
        member = message.mentions[0]
        Ps = random.choice(prison)
        content = "{0.author.mention}가 기절한 {1.mention}을 포로로 잡으려고 시도합니다.\n".format(message, member) + str(Ps)
        await message.channel.send(content)

    if message.content.startswith(">포로지원"):
        member = message.mentions[0]
        Ss = random.choice(save)
        content = "{0.author.mention}가 포로 {1.mention}의 구출을 시도합니다.\n".format(message, member) + str(Ss)
        await message.channel.send(content)

    if message.content.startswith(">투포환"):
        member = message.mentions[0]
        Damage = random.randint(90, 95)
        Dmsg = "{0.mention} 대미지 ".format(member) + str(Damage)
        colltime = "{0.author.mention}은 앞으로 3턴간 투포환 사용 불가. 보조무기로 교체해 주십시오.\n".format(message) + str(Dmsg)
        content = "{0.author.mention}가 {1.mention}에게 투포환을 던집니다.\n".format(message, member) + str(colltime)
        critical = "**공격이란 것이 폭발한다!**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Damage) == "95":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">머스킷"):
        member = message.mentions[0]
        Damage = random.randint(60, 70)
        Dmsg = "{0.mention} 대미지 ".format(member) + str(Damage)
        content = "{0.author.mention}가 {1.mention}에게 머스킷을 쏩니다.\n".format(message, member) + str(Dmsg)
        critical = "**석양이...집니다.**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Damage) == "70":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">롱보우"):
        member = message.mentions[0]
        Damage = random.randint(60, 70)
        Dmsg = "{0.mention} 대미지 ".format(member) + str(Damage)
        content = "{0.author.mention}가 {1.mention}에게 롱보우를 쏩니다.\n".format(message, member) + str(Dmsg)
        critical = "**당신이 유럽의 고주몽인 것입니까?**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Damage) == "70":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">검"):
        member = message.mentions[0]
        Damage = random.randint(50, 60)
        Dmsg = "{0.mention} 대미지 ".format(member) + str(Damage)
        content = "{0.author.mention}가 {1.mention}을 검으로 공격합니다.\n".format(message, member) + str(Dmsg)
        critical = "**엑스-칼리버-!!**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Damage) == "60":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">활"):
        member = message.mentions[0]
        Damage = random.randint(50, 60)
        Dmsg = "{0.mention} 대미지 ".format(member) + str(Damage)
        content = "{0.author.mention}가 {1.mention}에게 활을 쏩니다.\n".format(message, member) + str(Dmsg)
        critical = "**당신이 유럽의 고주몽인 것입니까?**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Damage) == "60":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">채찍"):
        member = message.mentions[0]
        Damage = random.randint(40, 50)
        Dmsg = "{0.mention} 대미지 ".format(member) + str(Damage)
        content = "{0.author.mention}가 {1.mention}에게 채찍을 휘두릅니다.\n".format(message, member) + str(Dmsg)
        critical = "**여왕님도 울고 갈 솜씨!**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Damage) == "50":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">둔기"):
        member = message.mentions[0]
        Damage = random.randint(30, 40)
        Dmsg = "{0.mention} 대미지 ".format(member) + str(Damage)
        content = "{0.author.mention}가 {1.mention}을 둔기로 공격합니다.\n".format(message, member) + str(Dmsg)
        critical = "**9회말 역전만루홈런!**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Damage) == "40":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">건틀릿"):
        member = message.mentions[0]
        Damage = random.randint(20, 30)
        Dmsg = "{0.mention} 대미지 ".format(member) + str(Damage)
        content = "{0.author.mention}가 {1.mention}을 건틀릿으로 공격합니다.\n".format(message, member) + str(Dmsg)
        critical = "**격투계를 뒤집어놓으셨다!**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Damage) == "30":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">너클"):
        member = message.mentions[0]
        Damage = random.randint(10, 20)
        Dmsg = "{0.mention} 대미지 ".format(member) + str(Damage)
        content = "{0.author.mention}가 {1.mention}을 너클로 공격합니다.\n".format(message, member) + str(Dmsg)
        critical = "**까불다 맞으면 아프다.**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Damage) == "20":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">주먹"):
        member = message.mentions[0]
        Damage = random.randint(1, 8)
        Dmsg = "{0.mention} 대미지 ".format(member) + str(Damage)
        content = "{0.author.mention}가 {1.mention}을 주먹으로 공격합니다.\n".format(message, member) + str(Dmsg)
        critical = "**살살 맞으면 안 아프지. 지금은 아닌 것 같지만.**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Damage) == "8":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">치료"):
        member = message.mentions[0]
        Heal = random.randint(10, 40)
        Hmsg = "{0.mention} 회복 ".format(member) + str(Heal)
        content = "{0.author.mention}가 {1.mention}을 치유합니다.\n".format(message, member) + str(Hmsg)
        critical = "**조상님도 살아날 오버힐!**"
        Cmsg = str(content) + "\n" + str(critical)
        if str(Heal) == "40":
            await message.channel.send(Cmsg)
        else:
            await message.channel.send(content)

    if message.content.startswith(">오늘의 날씨는 뭘까용~?"):
        weather = random.choice(w)
        await message.channel.send("오늘의 날씨는 " + str(weather) + "입니당!")

    if message.content.startswith(">삭제"):
        amount = int(message.content[4:])
        await message.channel.purge(limit=amount)

    if message.content.startswith(">링크"):
        await message.channel.purge(limit=1)
        msg = message.content[4:]
        await client.get_channel(링크).send(msg)

    if message.content.startswith(">공지"):
        await message.channel.purge(limit=1)
        msg = message.content[4:]
        await client.get_channel(공지).send(msg)

    if message.content.startswith(">관계"):
        await message.channel.purge(limit=1)
        msg = message.content[4:]
        await client.get_channel(관계).send(msg)

    if message.content.startswith(">카피페"):
        msg = message.content[5:]
        msg2 = "```" + str(msg) + "```"
        await client.get_channel(카피페).send(msg2)

    if message.content.startswith(">보내기"):
        await message.channel.purge(limit=1)
        msg = message.content[5:]
        await message.channel.send(msg)

    if message.content.startswith(">명령어"):
        embed = discord.Embed(title="명령어", description="> 기본\n`>명령어` 명령어 목록을 불러옵니다.\n\n"
                                                       "> 편의기능\n`>주사위는 던져졌다` 1에서 100까지의 랜덤한 숫자를 출력합니다."
                                                       "\n`>다이스 최솟값 최댓값` 최솟값과 최댓값 까지의 랜덤한 숫자를 출력합니다."
                                                       "\n`>낚시` 배의 후방발코니와 추후 공개되는 장소에서 낚시를 합니다. "
                                                       "무엇이 잡힐지 낚시대를 올리기 전까지는 아무도 모릅니다.."
                                                       "\n`>야바위` 컵 3개와 구슬을 이용해서 도박을 합니다. 여러분의 운을 믿습니다."
                                                       "\n`>사기야바위` 컵 3개와 구슬을 이용해서 사기를 칩니다."
                                                       "\n`>술 약한` 술 약한 사람이 술을 마십니다. 취했을까요?"
                                                       "\n`>술 중간` 술에 중간인 사람이 술을 마십니다. 취했을까요?"
                                                       "\n`>술 센` 술 센 사람이 술을 마십니다. 취했을까요?"
                                                       "\n`>관계 내용` 커뮤 내에서 형성된 관계를 정리합니다."
                                                       "\n\n"
                                                       "> 전투\n`>공격 @태그` 태그한 상대를 공격합니다.\n`>회피 @태그` 태그한 "
                                                       "상대의 공격을 회피합니다.\n\n> 무기\n`>투포환 @태그` 태그한 상대를 "
                                                       "투포환으로 공격합니다.\n`>머스킷 @태그` 태그한 상대를 머스킷으로 공격합니다."
                                                       "\n`>롱보우 @태그` 태그한 상대를 롱보우로 공격합니다.\n`>검 @태그` 태그한 "
                                                       "상대를 검으로 공격합니다.\n`>활 @태그` 태그한 상대를 활로 공격합니다.\n"
                                                       "`>채찍 @태그` 태그한 상대를 채찍으로 공격합니다.\n`>둔기 @태그` 태그한 "
                                                       "상대를 둔기로 공격합니다.\n`>건틀릿 @태그` 태그한 상대를 건틀릿으로 "
                                                       "공격합니다.\n`>너클 @태그` 태그한 상대를 너클로 공격합니다.\n"
                                                       "`>주먹 @태그` 태그한 상대를 주먹으로 공격합니다.\n\n> 선의 전용\n"
                                                       "`>치료 @태그` 태그한 상대를 치료합니다.\n\n> 포로\n`>포로취득 @태그` "
                                                       "태그한 상대를 포로로 취득하려고 시도합니다.\n`>포로지원 @태그` "
                                                       "태그한 상대의 구출을 시도합니다.", color=0x0067a2)
        embed.set_author(name="Liberty Blue", url=""
                         , icon_url=
                         "https://cdn.discordapp.com/attachments/735844523481104462/736763648680394862/aqd.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/735844523481104462/736763648680394862/aqd.png")
        await message.channel.send(embed=embed)

    if message.content.startswith(">스탭명령어"):
        embed = discord.Embed(title="명령어", description="> 기본\n>명령어\n>스탭명령어\n\n"
                                                       "> 편의기능\n>주사위는 던져졌다\n다이스 최솟값 최댓값\n>낚시"
                                                       "\n>야바위\n>사기야바위\n>술 약한\n>술 중간\n술 센\n\n"
                                                       "> 전투\n>공격 @태그\n>회피 @태그\n\n"
                                                       "> 무기\n>투포환 @태그\n>머스킷 @태그\n>롱보우 @태그\n>검 @태그\n"
                                                       ">활 @태그\n>채찍 @태그\n>둔기 @태그\n>건틀릿 @태그\n>너클 @태그\n"
                                                       ">주머 @태그\n\n> 선의 전용\n>치료 @태그\n\n"
                                                       "> 포로\n>포로취득 @태그\n>포로지원 @태그\n\n"
                                                       "> 스탭용\n>오늘의 날씨는 뭘까용~?\n>삭제 삭제 수\n>관계 전할내용"
                                                       "\n>링크 전할내용\n>공지 전할내용\n>보내기 전할내용(같은 채널)"
                                                       "\n\n> 비밀문구\n>Liberty Blue\n>넬 네르하 엘도라도\n>고향을 모르는 자"
                                                       "\n>파보리타\n>오리올 네르하\n>네레이다 엘도라도\n>Nell Nerja El Dorado"
                                                       "\n>여왕의 노예"
                                                       "\n>데이비드 젤리코\n>HMS 마르스\n>스파이\n>여왕의 방패", color=0x0067a2)
        embed.set_author(name="Liberty Blue", url=""
                         , icon_url=
                         "https://cdn.discordapp.com/attachments/735844523481104462/736763648680394862/aqd.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/735844523481104462/736763648680394862/aqd.png")
        await message.channel.send(embed=embed)


client.run("NzE2MDQyNTU0ODcyOTU0OTM1.XtGBRQ.iQwNM3tzXVgq5yS7N-jhe0BoKfI")