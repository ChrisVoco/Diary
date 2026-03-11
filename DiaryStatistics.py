class DiaryStatistics:
    @staticmethod
    def get_entry_count(diary):
        return len(diary.sissekanded)

    @staticmethod
    def get_average_length(diary):
        count = len(diary.sissekanded)

        if count == 0:
            return 0

        total_chars = sum(len(entry) for entry in diary.sissekanded)
        return total_chars / count

    @staticmethod
    def print_statistics(diary):
        count = DiaryStatistics.get_entry_count(diary)
        avg = DiaryStatistics.get_average_length(diary)

        print("Sissekannete arv:", count)
        print("Keskmine tähemärkide arv:", avg)