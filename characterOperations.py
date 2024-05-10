from msvcrt import getch 
states = ["AL", "AK", "AZ", "AR", "AS", "CA", "CO", "CT", "DE", "DC",
        "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
        "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE",
        "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK",
        "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "TT", "UT",
        "VT", "VA", "VI", "WA", "WV", "WI", "WY"
        ]
def moveUp(index=0):
    if index==0:
        print(states[index])
        return index
    else:
        index-=1
        print(states[index])
        return index

def moveDown(index=0):
    if index==len(states) - 1:
        print(states[index])
        return index
    else:
        index +=1
        print(states[index])
        return index

starting_index=0
while True: 
    keycode = ord(getch()) 
    if keycode == 27: #ESC 
        break 
    elif keycode == 13: #Enter 
        select() 
    elif keycode == 224: #Special keys (arrows, f keys, ins, del, etc.) 
        keycode = ord(getch()) 
        if keycode == 80: #Down arrow 
            starting_index = moveDown(starting_index) 
        elif keycode == 72: #Up arrow 
            starting_index = moveUp(starting_index)
