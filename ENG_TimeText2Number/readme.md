#TimeText2Number

Loki stands for _Linguistic Oriented Keyword Interface_, it comes with a friendly interface with Low-Code requirement to establish NLU-based language applications.

## Quick Start Guide

TimeText2Number provides you ability to convert English natural language temperal expressions texts into standard "**HOUR\_NUMBER:MINUTE\_NUMBER**" format.

For instance, 

```python
from TimeText2Number import runLoki

text = "It is a quarter past eight."
result = runLoki([text])

print(result["time"])
#You get "08:15"
```

NOTE: This module reuqires Loki subscription. If you don't have subscription, a sharing quota (2000 word/hour) will be used for demonstration/evaluation purposes.

