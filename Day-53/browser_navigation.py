class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = [homepage]
        self.forward_stack = []
        print(f"Homepage: {homepage}")

    def visit(self, url):
        self.forward_stack = []
        self.back_stack.append(url)
        print(f"Visiting: {url}")

    def back(self):
        if len(self.back_stack) > 1:
            current_page = self.back_stack.pop()
            self.forward_stack.append(current_page)
            print(f"Back to: {self.back_stack[-1]}")
        else:
            print("Cannot go back further!")

    def forward(self):
        if self.forward_stack:
            next_page = self.forward_stack.pop()
            self.back_stack.append(next_page)
            print(f"Forward to: {next_page}")
        else:
            print("No forward history!")

my_browser = BrowserHistory("google.com")
my_browser.visit("github.com")
my_browser.visit("leetcode.com")

my_browser.back()
my_browser.back()
my_browser.forward()
my_browser.visit("campusx.in")
my_browser.forward()