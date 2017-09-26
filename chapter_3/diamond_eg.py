import chapter_3.classes.diamond
import chapter_3.classes.diamond_super
from chapter_3.classes.diamond_super import Subclass as sub2

s = chapter_3.classes.diamond.Subclass()
s.call_me()
print(s.num_sub_calls, s.num_left_calls, s.num_right_calls,
      s.num_base_calls)

s2 = sub2()
s2.call_me()
print(s2.num_sub_calls, s2.num_left_calls, s2.num_right_calls,
      s2.num_base_calls)


