"""
  SUMMARY

(a*a) + (b*b) = (c*c)

"""

# @ Defination
square = lambda num: num * num

m_list = [index for index in range(13)][1:]
d_list = [index for index in range(32)][1:]

def Main(current_year, n_days=1):
    """
    """
    if n_days == 1:
        for month in m_list:
            for days in d_list:
                sum = square(month) + square(days)
                if sum == square(current_year):
                    print(f'{month} months + {days} days = 20{current_year}')
                    return sum
    else:
        t_list = []

        index = 0

        while index <= 1000:
            if index > 100:
                print('Next century!')
                index = index - 100
            t_year = current_year + index

            for month in m_list:
                for days in d_list:
                    sum = square(month) + square(days)
                    if sum == square(t_year):
                        print(f'{month} months + {days} days = 20{t_year}')
                        t_list.append([sum, t_year])

            index = index + 1

            if len(t_list) >= n_days:
                break

        return t_list

# ? Implementation

if __name__ == "__main__":
    for i in range(100):
        Main(i)