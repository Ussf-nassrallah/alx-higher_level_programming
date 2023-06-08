#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names__list = dir(hidden_4)
    for ele in names__list:
        if ele[:2] != "__":
            print(ele)
