#!/usr/bin/python3

if __name__ == "main":
    import hidden_4

    file_names = dir(hidden_4)
    for name in file_names:
        if name[:2] != "__":
            print(name)
