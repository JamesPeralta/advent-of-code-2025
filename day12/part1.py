input ="""
"""

sections = input.split('\n\n')

shape_library = {}
queries = []

for section in sections:
    lines = section.strip().split('\n')
    header = lines[0].strip()

    if header.endswith(':'):
        shape_id = int(header[:-1])
        base_coords = set()
        for r, line in enumerate(lines[1:]):
            for c, char in enumerate(line):
                if char == '#':
                    base_coords.add((r, c))

        variations = set()
        current_shape = base_coords

        for _ in range(2):
            for _ in range(4):
                if not current_shape:
                    norm_tuple = (frozenset(), 0, 0)
                else:
                    min_r = min(r for r, c in current_shape)
                    min_c = min(c for r, c in current_shape)
                    normalized = frozenset((r - min_r, c - min_c) for r, c in current_shape)
                    h_val = max(r for r, c in normalized) + 1
                    w_val = max(c for r, c in normalized) + 1
                    norm_tuple = (normalized, h_val, w_val)

                variations.add(norm_tuple)

                current_shape = set((c, -r) for r, c in current_shape)

            current_shape = set((r, -c) for r, c in base_coords)

        shape_library[shape_id] = list(variations)

    elif 'x' in header:
        for line in lines:
            parts = line.split(':')
            dims = parts[0].strip().split('x')
            w, h = int(dims[0]), int(dims[1])
            counts = list(map(int, parts[1].strip().split()))
            queries.append({'w': w, 'h': h, 'counts': counts})

successful_regions = 0

for query in queries:
    W, H = query['w'], query['h']

    pieces_to_fit = []
    for s_id, count in enumerate(query['counts']):
        if count > 0 and s_id in shape_library:
            piece_variations = shape_library[s_id]
            for _ in range(count):
                pieces_to_fit.append(piece_variations)

    pieces_to_fit.sort(key=lambda vars: len(vars[0][0]), reverse=True)
    total_area = sum(len(p[0][0]) for p in pieces_to_fit)
    if total_area > W * H:
        continue

    grid = [[False] * W for _ in range(H)]


    def backtrack(idx):
        if idx == len(pieces_to_fit):
            return True

        current_variations = pieces_to_fit[idx]

        for coords, h, w in current_variations:
            for r in range(H - h + 1):
                for c in range(W - w + 1):

                    fits = True
                    for pr, pc in coords:
                        if grid[r + pr][c + pc]:
                            fits = False
                            break

                    if fits:
                        for pr, pc in coords:
                            grid[r + pr][c + pc] = True

                        if backtrack(idx + 1):
                            return True

                        for pr, pc in coords:
                            grid[r + pr][c + pc] = False
        return False


    if backtrack(0):
        successful_regions += 1

print(successful_regions)