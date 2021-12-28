# FinBot: Currency Exchange Bot using Loki

Loki stands for _Linguistic Oriented Keyword Interface_, it comes with a friendly interface with Low-Code requirement to establish NLU-based language applications.

## Quick Start Guide

FinBot is a currency converter that could help you convert between different currencies. 

1. Log into [Loki interface] (https://nlu.droidtown.co/loki/)

<img src=".\img\1_loki_en_login.png" width="450">

2. Build a new project `FinBot` by entering the name `FinBot` and click `Create Project`> click `FinBot` to enter the project

<img src=".\img\2_create_project.png" width="450">

3. Choose `ArticutModel` > browse your computer and choose `ref/change_currency.ref` > click Load Intent > click and enter the `change_currency` intent

<img src=".\img\3_articut_model.png" width="450">

4. Click [Deploy Model (change_currency)] to deploy the model. Then, click the house icon to go back the project page. Copy the project key in `Key`

<img src=".\img\4_deploy_model.png" width="450">

<img src=".\img\4-2_deploy_model.png" width="450">

<img src=".\img\4-3_deploy_model.png" width="450">


5. Edit the `FinBot.py`
	- Enter your Droidtown user email at USERNAME
	- Enter your project key at LOKI_KEY
	- If you would like to use your own Articut to deal with different nlp tasks, please enter your [Articut key]

<img src=".\img\5_enterUSERNAME.png" width="450">

6. Start using `FinBot`
	- Add in new patterns in the `change_currency` intent > copy the python code from TestTool > add that python code to `intent/Loki_change_currency.py`
	- Test different sentences in `FinBot.py` (You could put in your sentence in `inputSTR` at the bottom of this script. 

<img src=".\img\6_add_new_sentence.png" width="450">


For instance, 

```python
    inputSTR = "Could I exchange 300 pennies to NTD"
	
	
	# Output 
	[change_currency] Could I exchange 300 pennies to NTD  ===> Could [I] exchange [300 pesos] [to] [NTD]
	INFO:root:{'src': ' pennies', 'tgt': 'NTD', 'amt': '300'}
	You could exchange 3.0 USD to 82.93 TWD

```

NOTE: This module reuqires Loki subscription. If you don't have subscription, a sharing quota (2000 word/hour) will be used for demonstration/evaluation purposes.

