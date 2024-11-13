# # from colorama import init, Fore, Style
# #
# # init()
#
# def input1():
#     while True:
#         num1 = int(input())
#         num2 = int(input())
#         if 6 <= num1 <= 10 and 6 <= num2 <= 10:
#             return num1, num2
#
# # def rang (num1, num2, results):
# #     for i in range(1, num1 + 1):
# #         for j in range(1, num2 + 1):
# #             if i == 2 or j == 2:
# #                 continue
# #             result = i * j
# #             results.append(result)
# #             if i == 4 or j == 4:
# #                 print(Fore.RED + str(result) + Style.RESET_ALL, end="\t")
# #             else:
# #                 print(Fore.YELLOW + str(result) + Style.RESET_ALL, end="\t")
# #         print()
#
# def re1 (results):
#     return [num for num in results if num % 2 == 0]
#
# def main():
#     num1, num2 = input1()
#     results = []
#     # rang(num1, num2, results)
#     re2 = re1(results)
#     print(re2)
#
# main()