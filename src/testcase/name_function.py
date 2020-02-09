def get_formatted_name(first, last, middle=''):  # 默认值写最后方
    """生成完整姓名"""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()


class AnoymoisSurey():
    """收集匿名问卷调查"""

    def __init__(self, question):
        """存储一个问题，并为记录答案准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的结果"""
        print("result:")
        for response in self.responses:
            print(response)
