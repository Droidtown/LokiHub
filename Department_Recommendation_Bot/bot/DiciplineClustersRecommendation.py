import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint
import asyncio

from interest.interest import execLoki
from the18DisciplineClusters.the18DisciplineClusters import getLokiTextSim
from DisciplineClusters_AgricultureGroup.Classifier import getLokiTextSim as ClassifierAgriculture
from DisciplineClusters_ArchitectureAndDesignGroup.Classifier import getLokiTextSim as ClassifierArchitectureAndDesign
from DisciplineClusters_ArtGroup.Classifier import getLokiTextSim as ClassifierArt
from DisciplineClusters_EarthAndEnvironmentalScienceGroup.Classifier import getLokiTextSim as ClassifierEarthAndEnvironmentalScience
from DisciplineClusters_EducationGroup.Classifier import getLokiTextSim as ClassifierEducation
from DisciplineClusters_EngineeringGroup.Classifier import getLokiTextSim as ClassifierEngineering
from DisciplineClusters_FinanceAndEconomicsGroup.Classifier import getLokiTextSim as ClassifierFinanceAndEconomics
from DisciplineClusters_ForeignLanguageGroup.Classifier import getLokiTextSim as ClassifierForeignLanguage
from DisciplineClusters_InformationGroup.Classifier import getLokiTextSim as ClassifierInformation
from DisciplineClusters_LawAndPoliticsGroup.Classifier import getLokiTextSim as ClassifierLawAndPolitics
from DisciplineClusters_LeisureAndPhysicalGroup.Classifier import getLokiTextSim as ClassifierLeisureAndPhysical
from DisciplineClusters_LifeSciencesGroup.Classifier import getLokiTextSim as ClassifierLifeSciences
from DisciplineClusters_LiteratureHistoryAndPhilosophyGroup.Classifier import getLokiTextSim as ClassifierLiteratureHistoryAndPhilosophy
from DisciplineClusters_ManagementGroup.Classifier import getLokiTextSim as ClassifierManagement
from DisciplineClusters_MassCommunicationGroup.Classifier import getLokiTextSim as ClassifierMassCommunication
from DisciplineClusters_MathematicsPhysicsAndChemistryGroup.Classifier import getLokiTextSim as ClassifierMathematicsPhysicsAndChemistry
from DisciplineClusters_MedicalHealthGroup.Classifier import getLokiTextSim as ClassifierMedicalHealth
from DisciplineClusters_SocialAndPsychologicalGroup.Classifier import getLokiTextSim as ClassifierSocialAndPsychological

logging.basicConfig(level=logging.DEBUG)

async def getLokiResult(inputSTR, filterLIST=[]):
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    refDICT = {}
    resultDICT = await execLoki(inputSTR, filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

async def getDisciplineCluster(inputSTR):
    disciplineClusterResult = await getLokiTextSim(inputSTR, [], featureLIST=["noun", "verb"], count=1)
    return disciplineClusterResult["results"][0]["lexicon"]

async def getDepartment(inputSTR, msgSTR):
    if inputSTR == "資訊學群":
        departmentResult = await ClassifierInformation(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "工程學群":
        departmentResult = await ClassifierEngineering(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "數理化學群":
        departmentResult = await ClassifierMathematicsPhysicsAndChemistry(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "醫藥衛生學群":
        departmentResult = await ClassifierMedicalHealth(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "生命科學學群":
        departmentResult = await ClassifierLifeSciences(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "生物資源學群":
        departmentResult = await ClassifierAgriculture(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "管理學群":
        departmentResult = await ClassifierManagement(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "財經學群":
        departmentResult = await ClassifierFinanceAndEconomics(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "法政學群":
        departmentResult = await ClassifierLawAndPolitics(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "社會心理學群":
        departmentResult = await ClassifierSocialAndPsychological(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "外語學群":
        departmentResult = await ClassifierForeignLanguage(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "文史哲學群":
        departmentResult = await ClassifierLiteratureHistoryAndPhilosophy(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "建築設計學群":
        departmentResult = await ClassifierArchitectureAndDesign(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "藝術學群":
        departmentResult = await ClassifierArt(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "教育學群":
        departmentResult = await ClassifierEducation(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "大眾傳播學群":
        departmentResult = await ClassifierMassCommunication(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "遊憩運動學群":
        departmentResult = await ClassifierLeisureAndPhysical(msgSTR, [], featureLIST=["noun","verb"], count=3)
    elif inputSTR == "地球環境學群":
        departmentResult = await ClassifierEarthAndEnvironmentalScience(msgSTR, [], featureLIST=["noun","verb"], count=3)
    return departmentResult

async def Introduction(inputSTR):
    if inputSTR == "資訊學群":
        IntroContent = "資訊學群主要學習電腦的軟硬體結構、各種電腦作業系統的原理，進而瞭解各種電腦程式設計的方法、找出電腦程式的錯誤並加以修正。課程中更包括學習資訊系統的統整規畫與管理，電腦保密方法及電腦病毒防治。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E8%B3%87%E8%A8%8A%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult
    elif inputSTR == "工程學群":
        IntroContent = "工程學群將基礎科學的知識與工程技術結合，依生產實務區分為各專門領域，以培育高層技術人才。包括所有與「工程」相關的學系。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E5%B7%A5%E7%A8%8B%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult       
    elif inputSTR == "數理化學群":
        IntroContent = "數理化是所有工程、科學、科技、數位系統運作的基礎知識，數理化學群強調基礎數理化的探究、周密的思考邏輯訓練，輔以系統化的課程，使同學培養基礎科學的知識能力，並建立實務研究的扎實背景。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E6%95%B8%E7%90%86%E5%8C%96%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult        
    elif inputSTR == "醫藥衛生學群":
        IntroContent = "醫藥衛生學群學習維護人類身心健康相關之知識及技術，從個人到整個人群，包括身心健康的維持、疾病或傷害的預防與治療。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E9%86%AB%E8%97%A5%E8%A1%9B%E7%94%9F%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult       
    elif inputSTR == "生命科學學群":
        IntroContent = "生命科學學群著重於動植物生活型態、生命現象的知識探究，包括生命的發生、遺傳、演化、構造、功能、細胞及分子層次機制等。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E7%94%9F%E5%91%BD%E7%A7%91%E5%AD%B8%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult       
    elif inputSTR == "生物資源學群":
        IntroContent = "生物資源學群強調的是動植物等生物資源的栽培改良及病蟲害防治、家畜的品種改良、畜漁產品的加工利用及研發、森林保護與經營管理、生活環境之設計經營、農業機具的製造與相關技術之訓練等，屬於生物資源與科技整合的學門。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E7%94%9F%E7%89%A9%E8%B3%87%E6%BA%90%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult      
    elif inputSTR == "管理學群":
        IntroContent = "管理學群主要處理組織系統內外人事物的各種問題，學習從事溝通協調、領導規劃或系統分析、資源整合等，以促使組織或企業工作流程順暢、工作效率提升、工作環境人性化、合理化，以收最大效益。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E7%AE%A1%E7%90%86%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult        
    elif inputSTR == "財經學群":
        IntroContent = "財經學群主要探究財務金融體制與系統運作機制，以資金為供給與需求探討金融體系的運作形式，可以提供對個人、組織、國家、國際等不同層面，在財務規劃與分析之原理概念，財務實務上的配置與管理技術。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E8%B2%A1%E7%B6%93%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult        
    elif inputSTR == "法政學群":
        IntroContent = "法政學群主要探究人類社會運作中相關法律、政治制度的各項層面，包括瞭解法律、政治運作的過程及政治理論的建構，藉以訓練從事法案制定、社會改革之專業人員。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E6%B3%95%E6%94%BF%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult       
    elif inputSTR == "社會心理學群":
        IntroContent = "社會心理學群著重社會結構及社會現象的觀察、分析批判，關懷人類心智行為形成成因、表現形式、後端影響的系統結構、個體心理狀態的探討，並且提供各種助人專業訓練，以提升眾人、個體的生活福祉。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E7%A4%BE%E6%9C%83%E5%BF%83%E7%90%86%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult        
    elif inputSTR == "外語學群":
        IntroContent = "外語學群主要學習外國語文的聽說讀寫能力，進而瞭解該國的歷史、文學創作及欣賞，並可提升至人類文化、社會政治經濟的深入描述與探究。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E5%A4%96%E8%AA%9E%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult       
    elif inputSTR == "文史哲學群":
        IntroContent = "文史哲學群主要以人類發展的思想、軌跡、符號為探究對象，依據人類發展的思想、軌跡、符號等建構人類的樣貌，並且進行區域、文化、時代間的橫向與縱向比較，文學主要培養探究及欣賞文化、運用語文及創作、賞析的能力；史學在瞭解歷史現象的演進、分析、探究與考據；哲學在訓練思考能力以對自我及世界反省。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E6%96%87%E5%8F%B2%E5%93%B2%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult        
    elif inputSTR == "建築設計學群":
        IntroContent = "建築設計學群主要探究自然社會環境、都市建築規畫、以及室內設計、商業設計等結合人文藝術與工程技術領域，對物體、空間或環境同時能賦予實用與美學之特性。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E5%BB%BA%E7%AF%89%E8%A8%AD%E8%A8%88%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult         
    elif inputSTR == "藝術學群":
        IntroContent = "藝術學群包括各類表達形式及創作過程的學習及賞析，結合各種特定形式來闡述人生中抽象意義層次的理念感受，運用創作者本身意識並配合各項藝術表現的基礎理論，用以詮釋生命的各種可能性。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E8%97%9D%E8%A1%93%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult       
    elif inputSTR == "教育學群":
        IntroContent = "教育學群依據教育原理與對象需求，探究人類對象的教育目標與教育實務方法，並且比較機構間、區域間的教育特性差異，提供各層級、各領域之教師有效的訓練原理與技術。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E6%95%99%E8%82%B2%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult       
    elif inputSTR == "大眾傳播學群":
        IntroContent = "大眾傳播學群主要學習傳播理論，以各種媒體將訊息以聲音、文字、影像等方式傳遞給人群，包括對訊息收集、媒體認識製作、評估訊息傳播的影響、傳播政策之擬定、傳播機構管理及資訊服務訓練等。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E5%A4%A7%E7%9C%BE%E5%82%B3%E6%92%AD%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult       
    elif inputSTR == "遊憩運動學群":
        IntroContent = "遊憩運動學群，以有助於人類身心理活動運作為核心的理論與實務規劃，包含了觀光休閒活動的投入與產出的規劃與管理，運動科學（運動生理、心理、生物力學等）理論與實務管理。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E9%81%8A%E6%86%A9%E9%81%8B%E5%8B%95%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult       
    elif inputSTR == "地球環境學群":
        IntroContent = "地球環境學群主要研究人類生存環境的各種自然現象及人文現象、資源的分佈與特色、污染成因與防治，也研究改變人文與自然環境之科學理論及工程技術等。\n"
        URL = "點擊鏈結進一步探索：" + "https://ioh.tw/learning_categories/%E5%9C%B0%E7%90%83%E7%92%B0%E5%A2%83%E5%AD%B8%E7%BE%A4"
        IntroResult = IntroContent + URL
        return IntroResult

# Discord client setup
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if client.user.mentioned_in(message):
        inputSTR = message.content
        lokiResult = await getLokiResult(inputSTR)
        if len(lokiResult) != 0:
            disciplineClusterResult = await getDisciplineCluster(inputSTR)
            departmentResult = await getDepartment(disciplineClusterResult, inputSTR)
            intro = await Introduction(disciplineClusterResult)
            replySTR = "那" + disciplineClusterResult + "的科系可能會較為適合你，"
            replySTR = replySTR + "尤其是其中的" + departmentResult["results"][0]["lexicon"] + "、" + departmentResult["results"][1]["lexicon"] + " 與" + departmentResult["results"][2]["lexicon"] + "等科系。\n"
            replySTR = replySTR + intro
        elif "使用說明" in inputSTR:
            replySTR = "歡迎使用興趣使然的學群推薦機器人！\n本機器人是一個為那些對升學方向感到迷茫的使用者提供學群與科系推薦的機器人。\n使用者只需輸入自己的興趣，機器人將根據這些興趣提供適合的學群與科系建議。本機器人的資料來自 IOH 網站，旨在幫助使用者更好地了解各學群和科系的選擇。"
        else:    
            replySTR = "該輸入訊息似乎不是興趣句，本機器人是將興趣句作為學群推薦的參考依據的，所以請輸入描述興趣的句子。若需要使用說明請輸入「使用說明」。"
    
        # Send back the result to Discord
        await message.channel.send(replySTR)

# Run the client
if __name__ == "__main__":
    with open("account.info", encoding="utf-8") as f: #讀取account.info
        accountDICT = json.loads(f.read())
    client.run(accountDICT["discord_token"])
