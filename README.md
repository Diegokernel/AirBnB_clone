<img src="https://user-images.githubusercontent.com/33245729/41383392-58f3dbb8-6f25-11e8-8215-d7c3832c0ae8.png">

## AirBnB Clone - The Console

### Contents

* [Description](https://github.com/Diegokernel/AirBnB_clone#description)
* [Files](https://github.com/Diegokernel/AirBnB_clone#files-in-this-repository)
* [Usage](https://github.com/Diegokernel/AirBnB_clone#usage)
* [Installation](https://github.com/Diegokernel/AirBnB_clone#installation)
* [Example Usage](https://github.com/Diegokernel/AirBnB_clone#example-usage)
* [Authors](https://github.com/Diegokernel/AirBnB_clone#authors)
---

### Description
We will be creating a clone of the AirBnb application. This repository contains the code for one of the preliminary steps of this whole project: the console. In this part of the project, we have written a command interpreter to manage our AirBNB objects. We have put in place a parent class to take care of the initialization, serialization and deserialization of future instances. We have created the first abstract storage engine of the project and created unittests to validate all our classes and storage engine.


This repository contains several packages that include the various models that will be employed in the application as objects, a file storage schema class, and various tests written using the unittest module of Python.

---

### Files
---
|   **File**   |   **Description**   |
| -------------- | --------------------- |
|console.py | Command interpreter |
|file_storage.py | Instansens are being serialised to a JSON-string and deserialised back |
|base_model.py | Defines all common attributes/methods for other classes |
|amenity.py | A class Amenity that inherits from BaseModel |
|city.py | A class City that inherits from BaseModel |
|place.py | A class Place that inherits from BaseModel |
|review.py | A class Review that inherits from BaseModel |
|state.py | A class State that inherits from BaseModel |
|user.py | A class User that inherits from BaseModel |
|tests\ | Containes Unit Tests for the progect |
|README.md | readme file |
|AUTHORS | autor file |

### Usage

#### Basic Usage of The Console
---
| **Function** | **Description** |
| -------------- | ----------------- |
|EOF | Exit the program |
|quit | Exit the program |
|help | Help function |
|create | Creates a new instance of BaseModel, saves it and prints the id |
|show | Prints the string representation of an instance based on the class name and id |
|destroy | Deletes an instance based on the class name and id |
|all | Prints all string representation of all instances based or not on the class name |
|update | Updates an instance based on the class name and id by adding or updating attribute |

### Installation
```
git clone git@github.com:Diegokernel/AirBnB_clone.git
```
---

### Example Usage

#### Interative Mode:
```
(hbnb) help

Documented commands (type help <topic>):
========================================

EOF  all  count  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) create BaseModel
18bb97af-f3fc-4213-946a-c9a3d77cd508
(hbnb) all BaseModel
(hbnb) [BaseModel] (18bb97af-f3fc-4213-946a-c9a3d77cd508) {'created_at': datetime.datetime(2019, 7, 05, 22, 27, 16, 194963), 'updated_at': datetime.datetime(2017, 7, 05, 22, 27, 16, 195000), 'id': '18bb97af-f3fc-4213-946a-c9a3d77cd508'}
(hbnb) show BaseModel 18bb97af-f3fc-4213-946a-c9a3d77cd508
(hbnb) create User
71a36988-d044-4471-a2b2-ea5f78a7acec
(hbnb) User.all()
[User] (71a36988-d044-4471-a2b2-ea5f78a7acec) {'created_at': datetime.datetime(2019, 7, 05, 22, 27, 56, 902596), 'updated_at': datetime.datetime(2017, 6, 05, 22, 27, 56, 902642), 'id': '71a36988-d044-4471-a2b2-ea5f78a7acec'}
(hbnb) update User 71a36988-d044-4471-a2b2-ea5f78a7acec first_name Mama
(hbnb) User.show(71a36988-d044-4471-a2b2-ea5f78a7acec)
[User] (71a36988-d044-4471-a2b2-ea5f78a7acec) {'id': '71a36988-d044-4471-a2b2-ea5f78a7acec', 'created_at': datetime.datetime(2019, 7, 05, 22, 27, 56, 902596), 'first_name': 'Gato', 'updated_at': datetime.datetime(2019, 7, 05, 22, 45, 20, 107855)}
(hbnb) destroy BaseModel 18bb97af-f3fc-4213-946a-c9a3d77cd508
(hbnb) show BaseModel 18bb97af-f3fc-4213-946a-c9a3d77cd508
** no instance found **
(hbnb) quit
```

#### Non-interactive Mode:
```
echo "User.all()" | ./console.py
(hbnb) [User] (71a36988-d044-4471-a2b2-ea5f78a7acec) {'updated_at': datetime.datetime(2019, 7, 05, 22, 48, 15, 587000), 'id': '71a36988-d044-4471-a2b2-ea5f78a7acec', 'first_name': 'Perro', 'created_at': datetime.datetime(2019, 7, 05, 22, 27, 56, 902596)}
(hbnb)
```

### Authors

Diego Castellanos.

Diego Orejuela.
