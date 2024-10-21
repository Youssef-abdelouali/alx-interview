#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def look_next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    box_status = {}
    while True:
        if len(box_status) == 0:
            box_status[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        available_keys = look_next_opened_box(box_status)
        if available_keys:
            for key in available_keys:
                try:
                    if box_status.get(key) and box_status.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    box_status[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in box_status.values()]:
            continue
        elif len(box_status) == len(boxes):
            break
        else:
            return False

    return len(box_status) == len(boxes)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()

