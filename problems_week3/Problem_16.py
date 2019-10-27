def ReconstructStringFromGenomePath(text):
    list_ = text.split("\n")
    output = list_[0]
    for word in list_[1:]:
        output = output + word[-1]
    return output
