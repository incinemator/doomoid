# H - uint16, h - int16, I - uint32, i - int32, c - char


class Thing:
    # 10 bytes
    __slots__ = [
        'pos',  # pos.x, pos.y - 4h
        'angle',  # 2H
        'type',  # 2H
        'flags'  # 2H
    ]


class Seg:
    # 12 bytes = 2h x 6
    __slots__ = [
        'start_vertex_id',
        'end_vertex_id',
        'angle',
        'linedef_id',
        'direction',
        'offset',
    ]


class SubSector:
    # 4 bytes = 2h + 2h
    __slots__ = [
        'seg_count',
        'first_seg_id'
    ]


class Lindedef:
    # 14 bytes = 2H x 7
    __slots__ = [
        'start_vertex_id',
        'end_vertex_id',
        'flags',
        'line_type',
        'sector_tag',
        'front_sidedef_id',
        'back_sidedef_id'
    ]