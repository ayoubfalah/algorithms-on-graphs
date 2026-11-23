def erase_cycles(walk):
    """
    Erase cycles from a walk

    :param walk: a non-empty sequence of vertices visited by walk
    :return: a path with the same endpoints of walk
    """
    path = []
    visited = set()

    for v in walk:
        if v not in visited:
            path.append(v)
            visited.add(v)
        else:
            while path[-1] != v:
                u = path.pop()
                visited.remove(u)

    return path

if __name__ == "__main__":
    walk = [1, 2, 3, 4, 2, 5, 6, 5, 7]
    print(f"Walk {walk} -> Path {erase_cycles(walk)}")