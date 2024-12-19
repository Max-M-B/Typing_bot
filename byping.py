from pynput.keyboard import Key, Controller
import time

key = Controller()

response = "Indian|still|now|when|keep|America|river|back|just|eye|page|second|about|she|us|in|an|very|have|mean|back|much|would|because|make|from|been|on|point|come|open|once|head|high|just|people|work|me|also|face|read|earth|two|too|Indian|because|many|car|both|for|enough|light|never|new|without|begin|above|that|her|there|who|learn|river|idea|it|paper|tell|animal|family|something|state|were|both|really|will|father|night|where|important|plant|part|seem|read|most|even|seem|form|only|live|oil|carry|something|good|mother|ask|this|said|group|right|one|away|some|plant|point|watch|me|carry|use|work|along|about|far|world|live|into|than|girl|line|live|white|night|hand|feet|close|then|she|over|also|air|old|could|with|answer|big|its|paper|spell|out|way|is|been|up|until|to|different|day|them|where|my|and|one|something|show|great|after|add|end|such|other|for|also|being|his|sound|stop|change|spell|country|think|could|house|him|to|quick|know|let|many|was|get|night|near|our|side|need|under|not|mother|city|before|home|such|new|just|help|it|once|even|together|still|or|letter|look|man|would|over|been|each|family|back|city|place|does|while|talk|out|its|letter|end|get|to|have|between|first|kind|up|off|here|set|if|show|came|give|after|much|but|don't|between|saw|book|two|tell|leave|show|land|and|word|run|each|house|children|three|how|make|tell|hear|there|sentence|world|while|mountain|are|found|find|the|call|time|song|so|know|girl|land|above|does|it's|with|took|our|see|had|went|around|own|animal|air|close|head|small|country|water|his|begin|set|open|eat|those|no|after|quick|let|any|we|father|question|land|great|walk|its|try|call|around|these|why|put|write|air|hard|way|think|often|plant|had|life|as|run|down|large|part|big|example|mile|hard|list|is|different|high|last|as|long|when|kind|start|go|so|under|put|make|move|if|be|very|first|write|without|left|need|write|said|want|sound|more|see|animal|few|never|might|their|change|almost|state|question|look|must|what|she|but|last|learn|family|men|sentence|abou"
response = response.replace('|', " ")

time.sleep(10)
for c in response:
    key.press(c)
    key.release(c)
    time.sleep(0.01)
