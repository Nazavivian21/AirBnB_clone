# HBNB - The Console

<br>

## Table of Contents
Description
Repository Contents by Project Task
Installation
Usage
Commands
Models
File Storage
Testing
Authors
License

<br>

### Description

This repository serves as the initial phase of a student project aimed at replicating the AirBnB website. The backend interface, or console, enables users to manage program data and includes file storage capabilities. The implementation of JSON serialization and deserialization techniques ensures that data remains persistent across different sessions. This means that users can resume their work or retrieve information from where they left off, enhancing the overall usability and functionality of the system. This stage sets the foundation for further development, offering a solid starting point for building an AirBnB clone. The repository sets the groundwork for further development, providing a solid foundation upon which additional features and functionalities can be built to create a comprehensive AirBnB clone.

---

### Repository Contents by Project Task

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors | [AUTHORS](https://github.com/bobuzy/AirBnB_clone/blob/master/AUTHORS) | The list of all contributors to the repository and details |
| 1: Unit Testing | [/tests](https://github.com/bobuzy/AirBnB_clone/tree/master/tests) | All class-defining modules are unittested |
| 2: Models | [/models](https://github.com/bobuzy/AirBnB_clone/tree/master/models) | All class modules are defined |
| 3. BaseModel class | [/models/base_model.py](https://github.com/bobuzy/AirBnB_clone/blob/master/models/base_model.py) | The base class that defines common attributes and methods for other classes |
| 4. FileStorage class | [/models/engine/file_storage.py](https://github.com/bobuzy/AirBnB_clone/blob/master/models/engine/file_storage.py) | This class serializes instances to a JSON file and deserializes JSON file to instances |
| 5. Console | [console.py](https://github.com/bobuzy/AirBnB_clone/blob/master/console.py) | This class defines a command-line interface for a HBNB application. It handles commands like create, show, destroy, all, and update to manage instances of different classes. It also supports quit and clear commands for program control.|
| 6. More Classes | [/models/user.py](https://github.com/bobuzy/AirBnB_clone/tree/master/models/user,py) [/models/place.py](https://github.com/bobuzy/AirBnB_clone/tree/master/models/place.py) [/models/city.py](https://github.com/bobuzy/AirBnB_clone/tree/master/models/city.py) [/models/amenity.py](https://github.com/bobuzy/AirBnB_clone/tree/master/models/amenity.py) [/models/state.py](https://github.com/bobuzy/AirBnB_clone/tree/master/models/state.py) [/models/review.py](https://github.com/bobuzy/AirBnB_clone/tree/master/models/review.py) | Dynamically implements more classes |
<br>
<br>

### Installation

To get started with the Airbnb Clone CLI, follow these steps:

Clone the repository:

cd Airbnb_clone
Ensure you have Python 3 installed on your machine. You can download it from the official Python website.



1. Clone this repository.
```
git clone https://github.com/bobuzy/AirBnB_clone.git
cd Airbnb_clone
```

2. Execute the "console.py" file.
```
./console.py
```
3. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)

Note: Ensure you have Python 3 installed on your machine. You can download it from the official Python website.


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>
