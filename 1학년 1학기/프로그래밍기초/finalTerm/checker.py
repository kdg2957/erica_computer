##########################################################
#
# [CSE1017] 2023 Programming Fundamantal
#           - Final Exam. Testing Tool
#
# Hyunha Kim @ CSE, HYU, ERICA & SOFTOPIA
# 2023 All rights reserved.
#
##########################################################

class FIN2023:
  check_mode = False

  def __init__(self):
    self.check_mode = False

  def enable(self):
    self.check_mode = True

  def disable(self):
    self.check_mode = False

  def check(self):
    return self.check_mode

  def verbose(self):
    return True

xx = FIN2023()

pp = print

def print(*args, sep=" ", end="\n"):
  if xx.check():
    fst = True
    global buf
    for arg in args:
      if fst:
        fst = False
      else:
        buf += sep
      buf += str(arg)
    buf += end
  elif xx.verbose():
    fst = True
    for arg in args:
      if fst:
        fst = False
      else:
        pp(sep, end="")
      pp(arg, end="")
    pp(end, end="")

def normalize(s):
  return s.replace(' ','') #.replace('\n','')

def pp_value(v):
  if type(v) == str:
    if "'" in v:
      pp('"' + v + '"', end="")
    else:
      pp("'" + v + "'", end="")
  else:
    pp(v, end="")

def run_skelecton(tag, f, test, ans,
                  isTuple=False, isBuf=False, normalizing=False):
  xx.enable()
  rs = []
  if isBuf:
    global buf
  if isTuple:
    for a1, a2 in test:
      if isBuf:
        # global buf
        buf = ""
        f(a1, a2)
        rs.append(buf)
      else:
        rs.append(f(a1, a2))
  else:
    for a in test:
      if isBuf:
        # global buf
        buf = ""
        f(a)
        rs.append(buf)
      else:
        rs.append(f(a))

  total = len(test)
  point = 0
  for i in range(total):
    if normalizing:
      v1, v2 = normalize(rs[i]), normalize(ans[i])
    else:
      v1, v2 = rs[i], ans[i]
    if v1 == v2:
      point += 1
    else:
      pp("[" + tag + "]", f.__name__, "(", end="")
      if isTuple:
        pp_value(test[i][0])
        pp(",", end="")
        pp_value(test[i][1])
      else:
        pp_value(test[i])
      pp(") :\n" + "[Answer] ---")
      if type(ans[i]) == str and not isBuf:
        if "'" in ans[i]:
          pp('"' + ans[i] + '"')
        else:
          pp("'" + ans[i] + "'")
      else:
        pp(ans[i])
      pp("[Your Result] ---")
      pp(rs[i])
  pp("*** ["+tag+"]", f.__name__,":",point,"/",total)
  pp()
  xx.disable()

##########################################################
# 1.1
##########################################################

test1_1 = [(21,19),(23, 22),(100,200)]
ans1_1 = [20, -1, 150]

def run_case1_1(tag, f):
  run_skelecton(tag, f, test1_1, ans1_1, isTuple=True)

##########################################################
# 1.2
##########################################################

test1_2 = [(21,19),(19,21),(21,23),(99,101),(22,18),(23,22)]
ans1_2 = [True, True, False, False, True, False]

def run_case1_2(tag, f):
  run_skelecton(tag, f, test1_2, ans1_2, isTuple=True)

##########################################################
# 1.3
##########################################################

test1_3 = [(21,19),(19,21),(21,23),(99,101),(22,18),(23,22)]
ans1_3 = [
  '21 x 19\n= (20 + 1) x (20 - 1)\n= 20 x 20 - 1 x 1\n= 400 - 1\n= 399\n',
  '19 x 21\n= (20 - 1) x (20 + 1)\n= 20 x 20 - 1 x 1\n= 400 - 1\n= 399\n',
  '21 x 23 = ?\n',
  '99 x 101 = ?\n',
  '22 x 18\n= (20 + 2) x (20 - 2)\n= 20 x 20 - 2 x 2\n= 400 - 4\n= 396\n',
  '23 x 22 = ?\n']

def run_case1_3(tag, f):
  run_skelecton(tag, f, test1_3, ans1_3,
                isTuple=True, isBuf=True, normalizing=True)

##########################################################
# 2.1
##########################################################

test2_1 = ['It', 'high', 'Noon']
ans2_1 = ['it', 'high', 'noon']

def run_case2_1(tag, f):
  run_skelecton(tag, f, test2_1, ans2_1)

##########################################################
# 2.2
##########################################################

test2_2 = [
  "It's High Noon...",
  "Welcome to the summoner's Valley!",
  'You are over scrupulous, surely. I dare say Mr. Bingley will be very glad to see you; and I will send a few lines by you to assure him of my hearty consent to his marrying whichever he chooses of the girls; though I must throw in a good word for my little Lizzy."',
  '"Oh!" said Lydia stoutly, "I am not afraid; for though I _am_ the youngest, I’m the tallest."'
]
ans2_2 = [
  ['it', 'high', 'noon'],
  ['welcome', 'to', 'the', 'summoner', 'valley'],
  ['you', 'are', 'over', 'scrupulous', 'surely', 'dare', 'say', 'mr', 'bingley', 'will', 'be', 'very', 'glad', 'to', 'see', 'you', 'and', 'will', 'send', 'few', 'lines', 'by', 'you', 'to', 'assure', 'him', 'of', 'my', 'hearty', 'consent', 'to', 'his', 'marrying', 'whichever', 'he', 'chooses', 'of', 'the', 'girls', 'though', 'must', 'throw', 'in', 'good', 'word', 'for', 'my', 'little', 'lizzy'],
  ['oh', 'said', 'lydia', 'stoutly', 'am', 'not', 'afraid', 'for', 'though', 'am', 'the', 'youngest', 'the', 'tallest'],
]

def run_case2_2(tag, f):
  run_skelecton(tag, f, test2_2, ans2_2)

##########################################################
# 2.3
##########################################################

test2_3 = [ "sample2.txt" ]
ans2_3 = [
  {'not':1,'all':2,'that':1,'mrs':1,'bennet':1,'however':1,'with':2,'the':4,'assistance':1,'of':4,'her':2,'five':1,'daughters':1,'could':1,'ask':1,'on':1,'subject':1,'was':1,'sufficient':1,'to':2,'draw':1,'from':1,'husband':1,'any':1,'satisfactory':1,'description':1,'mr':1,'bingley':1,'they':2,'attacked':1,'him':1,'in':1,'various':1,'ways':1,'barefaced':1,'questions':1,'ingenious':1,'suppositions':1,'and':2,'distant':1,'surmises':1,'but':1,'he':1,'eluded':1,'skill':1,'them':1,'were':1,'at':1,'last':1,'obliged':1,'accept':1,'second':1,'hand':1,'intelligence':1,'their':1,'neighbour':1,'lady':1}
]

def run_case2_3(tag, f):
  run_skelecton(tag, f, test2_3, ans2_3)

##########################################################
# 2.4
##########################################################

test2_4 = [ ("prideandprejudice.txt", 3), ("prideandprejudice.txt", 5) ]
ans2_4_ws = [('the', 4521), ('to', 4246), ('of', 3735), ('and', 3657), ('her', 2226), ('in', 1939), ('was', 1849), ('she', 1710), ('that', 1595), ('it', 1550)]
ans2_4 = [
  ans2_4_ws[:3],
  ans2_4_ws[:5]
]

def run_case2_4(tag, f):
  run_skelecton(tag, f, test2_4, ans2_4, isTuple=True)

##########################################################
