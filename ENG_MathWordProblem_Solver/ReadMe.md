# MathWordProblem_Solver
***ENG_MathWordProblem_Solver*** is a English math word problem solver demonstration showing the potentiality of using Loki to solve English Math word problems. It is first released in [**PyConAPAC 2022**](https://tw.pycon.org/2022/zh-hant/conference/talk/233) . The program is developed by Benoit (***benoityen98@gmail.com***) and PeterWolf (***peter.w@droidtown.co***) to show a more advanced approach to natural language understanding technologies.

`#NLU` `#NLP` `#Math word problem` `#AI`

---
#### Directories, Files and Programs
```
├── 2beDiscussed.txt
├── corpus ***Math word problems collected for setting up Loki model***
├── LICENSE
├── Loki
│   ├── intent
│   │   ├── ArticutToolbox
│   │   │   ├ ***Texttools and number tools***
│   │   ├── Loki_bg_setting.py
│   │   ├── Loki_dividend.py
│   │   ├── Loki_divisor.py
│   │   ├── Loki_multiplicand.py
│   │   ├── Loki_multiplier.py
│   │   ├── Loki_negtve_num.py
│   │   ├── Loki_postve_num.py
│   │   ├── Loki_quest_goal.py
│   │   ├── Updater.py
│   │   └── USER_DEFINED.json
│   └── MathWord_Solver.py  ***#Main program***
├── README.md
├── ref  ***.ref files to be imported to your own Loki project when building your own Loki models.***
└── src ***supplementary programs to help operate utterances by Loki API***
    ├── corpus -> ../corpus/
    └── loki_op.py
```
    
#### Installation
You may install this model under your Droidtown account, then do more detailed adjustment on it. This section explains how to do this. It consisits of 5 steps.

1. Sign up an account in Droidtown [[link](https://nlu.droidtown.co)]
2. Git clone (or Download) this repository.
3. Sign in your Droidtown account at [[link](https://nlu.droidtown.co)], then click **[Start Loki]** to start Loki NLU system.
4. **[Create a new project]**, and name it whatever you like. (I use "***MWP***" for example)
5. Click in the **[MWP]** project just created, then click **[Browse...]** in the buttom of the page and select the *.ref files downloaded in [Step 2].
6. Click **[Load Intent]** button and **[Deploy All Models]** button.
7. Click the little house icon on the top left, then click **[Copy]** to get your **[Loki Project Key]**. (almost there)
8. Let's go back to the files you've just downloaded. In the "Loki" directory, Change the name of the ***template_account.info*** file into ***account.info*** , then open it and fill in the account.info. 
The "username" is the email you used to sign in Droidtown.
The "loki-key" is the **[Loki Project Key]** you just copied in [Step 7].
9. You are all set. Now you can execute the "MathWord_Solver.py" to do some math. :)