#!/usr/bin/python3

class VerboseList(list):
    def append(self, data):
        print("Added [{}] to the list.".format(data))
        super().append(data)

    def extend(self, data):
        print("Extended the list with [{}] items.".format(len(data)))
        super().extend(data)

    def remove(self, data):
        print("Removed [{}] from the list.".format(data))
        super().remove(data)

    def pop(self, index=-1):
        popped = super().pop(index)
        print("Popped [{}] from the list.".format(popped))
        return popped
