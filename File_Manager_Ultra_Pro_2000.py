def controllW(w):
    banned_ws = ["Flag", "bandiera", "parolaIllegale!!", "Secret"]

    for bw in banned_ws:
        if bw in w:
            w = w.replace(bw, "")
    
    return w
    
# Se mi seguissi lo avresti visto prima ;)
