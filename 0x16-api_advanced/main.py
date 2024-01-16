#!/usr/bin/python3
"""
0-main
"""
# import sys

# if __name__ == '__main__':
#     number_of_subscribers = __import__('0-subs').number_of_subscribers
#     if len(sys.argv) < 2:
#         print("Please pass an argument for the subreddit to search.")
#     else:
#         print("{:d}".format(number_of_subscribers(sys.argv[1])))

"""
1-main
"""

# import sys
# if __name__ == '__main__':
#     top_ten = __import__('1-top_ten').top_ten
#     if len(sys.argv) < 2:
#         print("Please pass an argument for the subreddit to search.")
#     else:
#         top_ten(sys.argv[1])


"""
2-main
"""

import sys
if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
