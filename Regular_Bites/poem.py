rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """
INDENTS = 4


def print_hanging_indents(poem):
  lst = poem.split("\n\n")
  # print(lst[2].splitlines(),len(lst[2].splitlines()))
  for part in lst:
    lines = []
    for line in part.splitlines():
      if line.strip():
        line = line.strip()
        lines.append(line)
    print(lines[0])
    for line in lines[1:]:
      print(' ' * INDENTS + line)


# print(rosetti_unformatted)
print_hanging_indents(rosetti_unformatted)
