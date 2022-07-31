def get_clippings(): 
    with open("Kindlesort/upload/My_Clippings.txt", encoding="utf-8") as f: 
        clippings = f.read().split("==========")

    return clippings 



