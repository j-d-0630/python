import dataclasses
import copy
import numpy as np
import random
import string
import time

@dataclasses.dataclass
class counting_class:
  #データの範囲
  key_list: list
  #キーの出現回数
  key_freq: list
  #出現回数の累計
  freq_cumul: list

@dataclasses.dataclass
class data_class:
  #数値
  num_value: list
  #アルファベット
  symbol: list


#counting sort
def counting_sort(data,c_class):
  rslt = data_class([],[])
  [rslt.num_value.append(None) for i in range(len(data.num_value))]
  [rslt.symbol.append(None) for i in range(len(data.symbol))]

  upper_limit = max(data.num_value)
  [c_class.key_list.append(i) for i in range(upper_limit + 1)]
  [c_class.key_freq.append(0) for i in range(upper_limit + 1)]

  for key in data.num_value:
    c_class.key_freq[key] += 1

  c_class.freq_cumul = np.cumsum(c_class.key_freq)

  #ソート処理
  for i in range(0,len(data.num_value)):
    rslt.num_value[c_class.freq_cumul[data.num_value[i]] - c_class.key_freq[data.num_value[i]]] = data.num_value[i]
    rslt.symbol[c_class.freq_cumul[data.num_value[i]] - c_class.key_freq[data.num_value[i]]] = data.symbol[i]
    c_class.key_freq[data.num_value[i]] -= 1

  return rslt


#挿入ソート
def sort_insert(data):
    """
    insert sort 挿入ソート
    ソート済み領域をどんどん拡張していく
    拡張していく中で拡張をする先頭要素を適切な場所に挿入していく
    安定なソート
    """
    rslt = copy.deepcopy(data)
    for i in range(1,len(data.num_value)):
        v = rslt.num_value[i]
        sym = rslt.symbol[i]
        j = i-1
        while((j>=0 and rslt.num_value[j] > v)):
            rslt.num_value[j+1] = rslt.num_value[j]
            rslt.symbol[j+1] = rslt.symbol[j]
            j-=1
        rslt.num_value[j+1] = v
        rslt.symbol[j+1] = sym
    
    return rslt


if __name__ == "__main__":
  counting = counting_class([],[],[])
  input_data = data_class([],[])
  data_num = 5000
  [input_data.num_value.append(random.randint(1,1000)) for i in range(data_num)]
  [input_data.symbol.append(random.choice(string.ascii_uppercase)) for i in range(data_num)]

  time_st = time.time()
  rslt_count = counting_sort(input_data,counting)
  time_en = time.time()
  elapsed_time_count = time_en - time_st

  time_st = time.time()
  rslt_ins = sort_insert(input_data)
  time_en = time.time()
  elapsed_time_ins = time_en - time_st

  # print("counting sort結果：{0}".format(rslt_count))
  # print("insert sort結果：{0}".format(rslt_ins))
  diagnose = rslt_count == rslt_ins
  print("counting sortは安定化？ ⇒ ",diagnose)
  print("counting sortの処理時間は{0}".format(elapsed_time_count))
  print("insert sortの処理時間は{0}".format(elapsed_time_ins))