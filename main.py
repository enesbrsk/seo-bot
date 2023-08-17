from service import open_and_close_page

if __name__ == "__main__":
    target_url = "https://www.google.com"
    iterations = 15000
    open_and_close_page(target_url, iterations)
