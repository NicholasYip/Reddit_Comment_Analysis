from part1_functions import part1_2
from part2_functions import part2_2, part2_3_1, part2_3_4, part2_3_3, part2_3_2, part2_3_5, part2_3_6

print('Part 2.5: Playing with different splits - 0.6 training, 0.4 testing')
comments = part1_2()

train_batch_items, test_batch_items = part2_2(comments, [0.6, 0.4])

part2_3_1(train_batch_items, test_batch_items)

part2_3_2(train_batch_items, test_batch_items)

part2_3_3(train_batch_items, test_batch_items)

part2_3_4(train_batch_items, test_batch_items)

part2_3_5(train_batch_items, test_batch_items)

part2_3_6(train_batch_items, test_batch_items)