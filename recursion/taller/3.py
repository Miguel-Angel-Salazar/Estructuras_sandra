def superdigito(num):
  if num < 10:
    return num
  if num >= 10 :
    return superdigito((num // 10)) + (num % 10)
print(superdigito(9875))