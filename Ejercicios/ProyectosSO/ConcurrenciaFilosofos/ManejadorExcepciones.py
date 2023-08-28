class ManejadorExcepciones:
    @staticmethod
    def handle(e, log_text=None, end_tag='end'):
        print(f"Excepción capturada: {e}")
        if log_text:
            log_text.insert(end_tag, f"Excepción capturada: {e}\n")
            log_text.see(end_tag)
