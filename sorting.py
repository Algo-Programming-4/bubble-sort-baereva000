
def bubble(list):
  i = 0
  for i in range(len(list)):
    j = i + 1
    for j in range(len(list)):
      if list[i] < list[j]:
        temp = list[j]
        list[j] = list[i]
        list[i] = temp
    j = 0

