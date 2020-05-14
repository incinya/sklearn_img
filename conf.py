def get_size(box):
    return abs(box[2] - box[0]) , abs(box[3] - box[1])


YUNDA_THRES = 200
BOX_1 = (0, 0, 13, 22)
BOX_2 = (21, 0, 31, 22)
BOX_OP = (13, 0, 21, 22)

SIZE_1 = get_size(BOX_1)
SIZE_2 = get_size(BOX_2)
SIZE_OP = get_size(BOX_OP)

