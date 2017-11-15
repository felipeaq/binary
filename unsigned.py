def unsignedToBin(dec):
  if (dec > 1):
    return str(unsignedToBin(dec//2)) +str(dec%2)
  elif(dec==1):
    return 1
  else:
    return 0
