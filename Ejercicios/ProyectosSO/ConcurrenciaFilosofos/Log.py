class Log:
    @staticmethod
    def write(message, log_text=None, end_tag='end'):
        print(f"Log: {message}")
        if log_text:
            log_text.insert(end_tag, f"Log: {message}")
            log_text.see(end_tag)
