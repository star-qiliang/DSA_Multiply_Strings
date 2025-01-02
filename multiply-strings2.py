class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def add_two_num(a,b):
            a = a[::-1]
            b = b[::-1]

            # print("a:", a)
            # print("b:", b)

            res_list = []
            stack = 0
            len_a = len(a)
            len_b = len(b)
            for i in range(max(len_a, len_b)):
                if i<len_a and i<len_b:
                    res = int(a[i]) + int(b[i]) + stack
                    if res>=10:
                        res = res%10
                        stack=1
                        res_list.append(res)
                    else:
                        stack=0
                        res_list.append(res)

                elif i<len_a:
                    res = int(a[i]) + stack
                    if res>=10:
                        res = res%10
                        stack=1
                        res_list.append(res)
                    else:
                        stack=0
                        res_list.append(res)

                elif i<len_b:
                    res = int(b[i]) + stack
                    if res>=10:
                        res = res%10
                        stack=1
                        res_list.append(res)
                    else:
                        stack=0
                        res_list.append(res)

            if stack:
                res_list.append(1)
            
            res_list = res_list[::-1]
            res_list = ''.join([str(x) for x in res_list])
            return res_list

        def shilft_position(nums, n):
            if nums=='0':
                return nums

            for i in range(n):
                nums+="0"

            return nums

        # res = add_two_num(num1, num2)

        res = '0'
        for i,i_nums in enumerate(range(len(num1)-1,-1,-1)):
            x = int(num1[i_nums])
            tmp = shilft_position(num2, i)
            # print("i:", i)
            # print("x:",x)
            # print("res:",res)
            # print("tmp:",tmp)

            while x>0:
                res = add_two_num(res, tmp)
                x-=1
                # print("\n")

        return res