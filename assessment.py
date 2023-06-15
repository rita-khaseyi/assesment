# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think 
#  how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.
# input 

class Ancestral_Stories:
    def __init__(self,story,storyteller,Translator) :
        self.story=story
        self.storyteller=storyteller
        self.translator=Translator
        

        

# 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.
class Recipe:
    def __init__(self,recipes):
        self.recipes=recipes

class MoroccanRecipe:

    def __init__(self,ingredients,preparationTime,cookingMethod,nutritionalInformation) :
        self.ingredients=ingredients
        self.prepationTime=preparationTime
        self.cookingMethod=cookingMethod
        self.nutritionalInformation=nutritionalInformation
    def recipe(self):
        return f"The Morrocan recipe is prepared using {self.ingredients} and is cooked using {self.cookingMethod} and has {self.nutritionalInformation}"    
class EthiopianRecipe:
    def __init__(self,ingredients,preparationTime,cookingMethod,nutritionalInformation) :
        self.ingredients=ingredients
        self.prepationTime=preparationTime
        self.cookingMethod=cookingMethod
        self.nutritionalInformation=nutritionalInformation
    def recipe(self) :
        return f"the Ethiopian recipe is prepared using {self.ingredients} and is cooked using {self.cookingMethod} and has {self.nutritionalInformation} "   
class NigerianRecipe:
    def __init__(self,ingredients,preparationTime,cookingMethod,nutritionalInformation) :
        self.ingredients=ingredients
        self.prepationTime=preparationTime
        self.cookingMethod=cookingMethod
        self.nutritionalInformation=nutritionalInformation
    def recipe(self) :
        return f"the Ethiopian recipe is prepared using {self.ingredients} and is cooked using {self.cookingMethod} and has {self.nutritionalInformation} "   

recipe1=MoroccanRecipe("wheat","30 minutes","oven","carbs")
print(recipe1.recipe())
recipe2=EthiopianRecipe("maize","1 hour","boling","calcium")
print(recipe2.recipe())
recipe3=NigerianRecipe("bean","20 minutes","heat","calcium")
print(recipe3.recipe())


                
        

# 3. **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to


# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.



        
# 4. **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.

# 5. Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def value(self):
        totalvalue=self.price *self.quantity   
        return totalvalue 
product1=Product("book",50,3) 
print  (product1.value()) 
product2=Product("cup",500,3) 
print  (product1.value()) 
product3=Product("plate",5000,3) 
print  (product1.value()) 
product4=Product("book",700,3) 
print  (product1.value()) 


# 6. Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0


    def passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60
    
student1=Student("rita",20,[50,50,50,50])  
print(student1.average_grade()) 
student2=Student("rita",20,[50,50,50,50])  
print(student2.average_grade())
student3=Student("rita",20,[50,50,50,50])  
print(student3.average_grade()) 



        
        
# 7. Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.


# 8. Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.
class Book:
    def __init__(self,title,author,book) :
        self.title=title
        self.book=book
        self.author=author
        
        
class Catalog:
  def __init__(self):
      self.books=[]
  def addBook(self,title,author,book):
      book=Book(title,author,book)
      self.books.append(Book) 
  def search(self,title):
      for x in self.books:
          if x.title==title:
            return x
          else:
              return "not found"
  def Authour(self,author):
      for x in self.books:
          if x.author==author:
              return x
          else:
              return "not found"
  def details(self):
      print(f"the {self.book} by {self.author} was published in 2020")
            
 
book1=Book("Born A crime","trevor","born")
book2=Catalog()
# book2.addBook('born a crime', 'trevor noah')
# book2.search("born a crime","trevor noah")
book2.details()
book2.Authour()
  
 
  
  
