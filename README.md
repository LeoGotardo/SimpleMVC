# MVC Design Pattern Implementation - Documentation

The provided code implements the Model-View-Controller (MVC) design pattern to create a simple product management application using Python and the Tkinter GUI library for the View (V), a MongoDB database for the Model (M), and a Controller (C) to handle the interactions between the View and the Model.

## Model (M)

### Class: Model

- **Description**: This class represents the Model of the MVC pattern. It handles the interaction with the MongoDB database for storing and retrieving product information.
- **Attributes**:
  - `CONNECTION_STRING`: A connection string to connect to the MongoDB database.
  - `client`: A MongoClient object to connect to the MongoDB database.
  - `bd`: A database object representing the "Dug" database in MongoDB.
  - `Products`: A collection object representing the "Products" collection in the "Dug" database.

### Methods:

1. `cad(Nome, Estoque, Pic)`: Inserts a new product into the "Products" collection in the database. It takes the product name, stock quantity, and image file path as input, and stores the image in binary format in the database.
2. `moveFile(pach)`: Opens and converts the image file to bytes format before storing it in the database. It takes the image file path as input and returns the image data in bytes format.
3. `everything()`: Fetches all products from the "Products" collection and returns a list containing all products' data.
4. `everyItem(Item)`: Fetches the specified item ("Nome", "Estoque", or "Picture_data") from all products in the "Products" collection and returns a list containing that specific item's data for all products.
5. `find(Name, do)`: Searches for products with a specific name in the "Products" collection and retrieves the corresponding "Nome", "Estoque", "Picture_data", or "_id" (identifier) based on the input parameter `do`.

## View (V)

### Class: View

- **Description**: This class represents the View of the MVC pattern. It creates the graphical user interface (GUI) using the Tkinter library and allows the user to interact with the product management application.
- **Attributes**:
  - `root`: The main Tkinter window object.
  - `c`: The Controller object responsible for handling interactions between the View and the Model.

### Methods:

1. `mainScreen()`: Creates the main GUI window, containing labels, entry fields, and buttons for product name and stock input, product registration, and clearing the input fields.
2. `create_label(frame, text, font, pady, padx, method)`: Creates and displays a label with the specified text, font, padding, and position (either "pack" or "grid") inside the given frame.
3. `create_entry(frame, justify, bg, borderwidth, width)`: Creates and displays an entry widget with the specified justification, background color, border width, and width inside the given frame. It returns the entry widget.
4. `create_button(frame, text, font, bg, fg, pady, padx, command, method)`: Creates and displays a button with the specified text, font, background color, foreground color, padding, and position (either "pack" or "grid") inside the given frame. It associates the button with a command function provided as input.
5. `alert(Name)`: Displays a warning message box with the given product name as input.
6. `clearFields()`: Clears the entry fields for product name and stock.
7. `cadastrar(nome, estoque, getfile)`: Registers a new product by calling the Controller's `cadastrar` method with the product name, stock quantity, and image file path as input.

## Controller (C)

### Class: Controller

- **Description**: This class represents the Controller of the MVC pattern. It acts as an intermediary between the View and the Model, handling user inputs from the View and updating the Model accordingly.
- **Attributes**:
  - `bd`: The Model object responsible for database interactions.

### Methods:

1. `getFile()`: Opens a file dialog to get the path of an image file selected by the user.
2. `cadastrar(Nome, Stoque, Pic)`: Calls the Model's `cad` method to add a new product with the provided name, stock quantity, and image file path.
3. `exit()`: Exits the program.
  
## Note

- The provided code demonstrates a simple implementation of the MVC design pattern using the Tkinter GUI library for the View and the MongoDB database for the Model. It allows the user to register products with names, stock quantities, and images and then view them.
- The code may require additional error handling and input validation to handle edge cases effectively and ensure the application's robustness in real-world scenarios. For instance, proper validation of user inputs (e.g., empty fields, invalid file paths) and error handling during database operations should be implemented.
- The MongoDB database credentials (root and password) are hard-coded in the Model class. In a real-world application, it's essential to store sensitive information like database credentials securely, for example, using environment variables or configuration files.