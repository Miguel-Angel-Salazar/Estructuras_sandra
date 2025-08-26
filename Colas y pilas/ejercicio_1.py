class animalshelter:

  def __init__(self):
    self.__cats = []
    self.__dogs = []


  def receive(self,e,type):
    if type == 'Cat':
      self.__cats.append(e)
    elif type == 'Dog':
      self.__dogs.append(e)
    else:
      return "Error, animal no es permitido"

    return True

  def adopt(self,type):

    if type == 'Cat':
      if self.is_empty_cats():
        return "Error, no hay gatos para adoptar"
      return self.__cats.pop(0)
    elif type == 'Dog':
      if self.is_empty_dogs():
        return "Error, no hay perros para adoptar"
      return self.__dogs.pop(0)
    else:
      return "Error, no se tiene del tipo de animal solicitado"

  def is_empty_cats(self):
    return len(self.__cats) == 0

  def is_empty_dogs(self):
    return len(self.__dogs) == 0

  def len_cats(self):
    return len(self.__cats)

  def len_dogs(self):
    return len(self.__dogs)


  def __str__(self):
    return '--'.join(map(str,self.__cats)) + ' <<>> ' + '--'.join(map(str,self.__dogs))


animals = animalshelter()
animals.receive("Cat1","Cat")
animals.receive("Cat2","Cat")
animals.receive("Cat3","Cat")
animals.receive("Dog1","Dog")
animals.receive("Dog2","Dog")
print("entregar pez: ",animals.receive("Fish1","Fish"))

print(animals)

print("adoptar gato : ", animals.adopt("Cat"))
print("adoptar gato : ", animals.adopt("Cat"))


print(animals)
    