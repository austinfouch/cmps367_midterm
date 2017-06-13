def build_dict(filename="data.txt"):
  input_file = open(filename, 'r')
  d = {}
  i = 0
  for line in input_file:
    my_str = line
    my_str = my_str.replace(',', '')
    tokens = my_str.split()
    key = i
    val = (float(tokens[0]), float(tokens[1]), float(tokens[2]))
    d[key] = val
    i += 1
  return d

tmp = build_dict()
print("-"*30)
sum1 = 0
sum2 = 0
sum3 = 0
for key in tmp.keys():
  sum1 = sum1 + tmp[key][0]
print("Average 1: ", (sum1/30))
for key in tmp.keys():
  sum2 = sum2 + tmp[key][1]
print("Average 2: ", (sum2/30))
for key in tmp.keys():
  sum3 = sum3 + tmp[key][2]
print("Average 3: ", (sum3/30))
print("-"*30)

d = {}
for key in tmp.keys():
  sumKey = tmp[key][0] + tmp[key][1] + tmp[key][2]
  if sumKey in d:
    d[sumKey] = d[sumKey] + 1
  else:
    d[sumKey] = 1

print("Historgram of sums:")
for key in d.keys():
  print(key, " -> ", d[key])
