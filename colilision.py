import server


def collide(a, b):
    a_x, a_y, a_w, a_h = a.get_bounding_box()
    b_x, b_y, b_w, b_h = b.get_bounding_box()
    left_a, bottom_a, right_a, top_a = a_x, a_y, a_x + a_w, a_y + a_h
    left_b, bottom_b, right_b, top_b = b_x, b_y, b_x + b_w, b_y + b_h

    if left_a < right_b and abs(left_a - right_b) < a_w // 2 and abs(a_y - b_y) < a_h // 2:
        a.x += abs(left_a - right_b)
        return False

    if right_a > left_b and abs(right_a - left_b) < a_w // 2 and abs(a_y - b_y) < a_h // 2:
        a.x -= abs(right_a - left_b)
        return False

    if bottom_a < top_b and abs(bottom_a - top_b) < a_h // 2 and abs(a_x - b_x) < a_w // 2:
        a.y += abs(bottom_a - top_b)
        return False

    if top_a > bottom_b and abs(top_a - bottom_b) < a_h // 2 and abs(a_x - b_x) < a_w // 2:
        a.y -= abs(top_a - bottom_b)
        return False

    return True


def clear_in(a, clear_map):
    a_x, a_y, a_w, a_h = a.get_bounding_box()
    b_x, b_y, b_w, b_h = clear_map.get_clear_box()
    left_b, bottom_b, right_b, top_b = b_x, b_y, b_x + b_w, b_y + b_h

    a_center_x = a_x + a_w // 2
    a_center_y = a_y + a_h // 2

    if left_b < a_center_x < right_b and bottom_b < a_center_y < top_b:
        return True

    else:
        return False

