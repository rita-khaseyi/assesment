// **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.
// 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.
class Recipe{
   constructor (this,recipes){
        this.recipes=recipes
      }
    }
class MoroccanRecipe{

    constructor(this,ingredients,preparationTime,cookingMethod,nutritionalInformation) {
        this.ingredients=ingredients
        this.prepationTime=preparationTime
        this.cookingMethod=cookingMethod
        this.nutritionalInformation=nutritionalInformation
    }
    recipe(this){
        return `The Morrocan recipe is prepared using ${this.ingredients} and is cooked using ${this.cookingMethod} and has ${this.nutritionalInformation}`    

    }
}
class EthiopianRecipe{
    constructor (this,ingredients,preparationTime,cookingMethod,nutritionalInformation){
        this.ingredients=ingredients
        this.prepationTime=preparationTime
        this.cookingMethod=cookingMethod
        this.nutritionalInformation=nutritionalInformation
    }
     recipe(this) {
        return `the Ethiopian recipe is prepared using ${this.ingredients} and is cooked using ${this.cookingMethod} and has ${this.nutritionalInformation}`
     }
    }  
class NigerianRecipe{
    constructor(this,ingredients,preparationTime,cookingMethod,nutritionalInformation){
        this.ingredients=ingredients
        this.prepationTime=preparationTime
        this.cookingMethod=cookingMethod
        this.nutritionalInformation=nutritionalInformation
    }
    recipe(this) {
        return `the Ethiopian recipe is prepared using ${this.ingredients} and is cooked using ${this.cookingMethod} and has ${this.nutritionalInformation}`
    }
}

let recipe1= new MoroccanRecipe("wheat","30 minutes","oven","carbs")
console.log(recipe1.recipe())
let recipe2= new EthiopianRecipe("maize","1 hour","boling","calcium")
console.log(recipe2.recipe())
let recipe3= new NigerianRecipe("bean","20 minutes","heat","calcium")
console.log(recipe3.recipe())


// 3. **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.
// 4. **African Music Festival:** You're in charge of organizing a Pan-African music
// festival. Many artists from different countries, each with their own musical style
// and instruments, are scheduled to perform. You need to write a program to
// manage the festival lineup, schedule, and stage arrangements. Think about how
// you might model the `Artist`, `Performance`, and `Stage` classes, and consider
// how you might use inheritance if there are different types of performances or
// stages.
// 5. Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

class Product{
    constructor(this,name,price,quantity){
        this.name=name
        this.price=price
        this.quantity=quantity
    }

     value(this){
        let totalvalue=self.price *self.quantity   
        return totalvalue 
     }
    }
let product1= new Product("book",50,3) 
console.log(product1.value())

let product2= new Product("cup",500,3) 
console.log( product2.value()) 
let product3=Product("plate",5000,3) 
console.log(product1.value()) 

// 6. Implement a class called Student with attributes for name, age, and grades (a
// list of integers). Include methods to calculate the average grade, display the
// student information, and determine if the student has passed (average grade >=
// 60). Create objects for the Student class and demonstrate the usage of these
// methods.

// 7. Create a FlightBooking class that represents a flight booking system. Implement
// methods to search for available flights based on destination and date, reserve
// seats for customers, manage passenger information, and generate booking
// confirmations.

// 8. Create a LibraryCatalog class that handles the cataloging and management of
// books in a library. Implement methods to add new books, search for books by
// title or author, keep track of available copies, and display book details.a
class Book {
    constructor(title, author,book) {
      this.title = title;
      this.author = author;
      this.copies = book;
    }
  }
  
  class Catalog {
    constructor() {
      this.books = [];
    }
  
    addBook(title, author, b00k) {
      const book = new Book(title, author, book);
      this.books.push(book);
    }
  
    search(title) {
      const Books = this.books.filter((book) =>
        book.title.includes(title)
      );
      return Books;
    }
  
    searchAuthor(author) {
      const found= this.books.filter((book) =>
        book.author.includes(author)
      );
      return found;
    }
  
    borrow(title) {
      const book = this.books.find(
        (book) => book.title === title
      );
  
     
    }
  
    return(title) {
      const book = this.books.find(
        (book) => book.title=== title.toLowerCase()
      );
  
      
  
      
    }
  
    Details(title) {
      const book = this.books.find(
        (book) => book.title=== title
      );
  
      if (book) {
        console.log(`Title: ${book.title}`);
        console.log(`Author: ${book.author}`);
        console.log(`Copies available: ${book.copies}`);
      } else {
        console.log(`Book not found.`);
      }
    }
  }
  
  // Example usage:
  const library = new Catalog();
  
  library.addBook('born a crime', 'trevor noah', 5);
  library.addBook('love pursuit', 'jay ', 3);
  library.addBook('originals', 'trishia', 2);
  
  
  const foundBooks = library.search('catcher');
  console.log(foundBooks)
  
  

  

  
  