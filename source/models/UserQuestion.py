class UserQuestion:
    def __init__(self, user_id, question_id, test_status, test_submit, memory, cpu_time):
        self.user_id = user_id
        self.question_id = question_id
        self.test_status = test_status
        self.test_submit = test_submit
        self.memory = memory
        self.cpu_time = cpu_time