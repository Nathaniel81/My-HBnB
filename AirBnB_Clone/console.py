#!/usr/bin/python3

    """_summary_

    Returns:
        _type_: _description_
    """

import cmd
import models


modLst = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        "Quits the program"
        return True

    def do_EOF(self, args):
        "Quits the program with EOF"
        return True

    def emptyline(self):
        """Makes an empty line + ENTER do nothing"""
        pass

    def do_create(self, args):
        """Creates a new instance,
        saves it (to the JSON file) and prints the id"""

        if len(args) == 0:
            print("** class name missing **")
        elif args not in modLst:
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.review import Review
            from models.amenity import Amenity

            obj = eval(args)()
            obj.save()
            print(obj.id)

    def do_show(self, args):
       """Prints the string representation of an instance
       based on the class name and id"""

       argss = args.split()
       if len(args) == 0:
           print("** class name missing **")
       elif argss[0] not in modLst:
           print("** class doesn't exist **")
       elif len(argss) < 2:
           print("** instance id missing **")
       elif f'{argss[0]}.{argss[1]}' not in models.storage.all():
           print("** no instance found **")
       else:
            k = f'{argss[0]}.{argss[1]}'
            print(models.storage.all()[k])

    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""

        argss = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif argss[0] not in modLst:
            print("** class doesn't exist **")
        elif len(argss) < 2:
            print("** instance id missing **")
        elif f'{argss[0]}.{argss[1]}' not in models.storage.all():
            print("** no instance found **")
        else:
            del models.storage.all()[f'{argss[0]}.{argss[1]}']
            models.storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances
        based or not on the class name."""

        if len(args) == 0:
            nwLst = []
            for obj in models.storage.all().values():
                nwLst.append(str(obj))
            print(nwLst)
        elif args in modLst:
            nwLst = []
            for k, v in models.storage.all().items():
                if k.split('.')[0] == args:
                    nwLst.append(str(v))
            print(nwLst)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)"""

        argss = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif argss[0] not in modLst:
            print("** class doesn't exist **")
        elif len(argss) < 2:
            print("** instance id missing **")
        elif f'{argss[0]}.{argss[1]}' not in models.storage.all():
            print("** no instance found **")
        elif len(argss) < 3:
            print("** attribute name missing **")
        elif len(argss) < 4:
            print("** value missing **")
        elif f'{argss[0]}.{argss[1]}' in models.storage.all():
            obj = models.storage.all()[f'{argss[0]}.{argss[1]}']
            obj.__dict__[argss[2]] = eval(argss[3])
            models.storage.save()
        else:
            pass

    def do_count(self, args):
        """Counts the number of instances of a class"""
        counter = 0
        for obj in models.storage.all().values():
            if args.split('.')[0] == type(obj).__name__:
                counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
